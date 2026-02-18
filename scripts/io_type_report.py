"""Generate I/O type aggregation report for published CLAMS apps.

Iterates all app version directories under ``docs/_apps/``, identifies
the latest version of each app, and groups them by shared input/output
annotation types.  The result is written to a markdown file.

Usage::

    python scripts/io_type_report.py            # writes to docs/app-io-types-report.md
    python scripts/io_type_report.py -o out.md  # writes to custom path
"""

import argparse
import json
import re
import textwrap
from collections import defaultdict
from datetime import datetime
from pathlib import Path


APPS_DIR = Path('docs/_apps')
DEFAULT_OUTPUT = Path('docs/app-io-types-report.md')


# ── helpers ──────────────────────────────────────────────────────────

def version_sort_key(version_str: str) -> tuple:
    """Return a tuple suitable for sorting version strings like v1, v2.1, v15."""
    v = version_str.lstrip('v')
    parts = re.split(r'[.\-]', v)
    result = []
    for p in parts:
        try:
            result.append(int(p))
        except ValueError:
            result.append(0)
    return tuple(result)


def extract_type_uri(item) -> str | tuple:
    """Extract the ``@type`` URI from an I/O spec entry.

    An entry can be:
      - a dict with ``@type``
      - a plain string (older metadata format)
      - a list of dicts (OR‑alternatives)
    """
    if isinstance(item, dict):
        return item.get('@type', '')
    if isinstance(item, str):
        return item
    if isinstance(item, list):
        return tuple(extract_type_uri(i) for i in item)
    return str(item)


def base_type_name(type_uri: str | tuple) -> str:
    """Extract a human‑readable *base* type name from a full URI.

    Examples:
      ``http://mmif.clams.ai/vocabulary/TimeFrame/v5``  -> ``TimeFrame``
      ``http://vocab.lappsgrid.org/Token``               -> ``Token``
      ``http://vocab.lappsgrid.org/Token#pos``           -> ``Token#pos``
    """
    if isinstance(type_uri, tuple):
        return ' | '.join(base_type_name(t) for t in type_uri)

    # property sub‑types  (Token#pos, Token#lemma)
    if '#' in type_uri:
        base_part, prop = type_uri.rsplit('#', 1)
        return f'{base_type_name(base_part)}#{prop}'

    parts = type_uri.rstrip('/').split('/')
    # walk backwards; the first segment that looks like a version tag means
    # the previous segment is the type name
    for i in range(len(parts) - 1, 0, -1):
        segment = parts[i]
        if re.match(r'^v\d', segment):
            return parts[i - 1]
    # no version tag – last segment *is* the type name (LAPPS style)
    return parts[-1] if parts else type_uri


def vocab_source(type_uri: str | tuple) -> str:
    """Return ``MMIF`` or ``LAPPS`` depending on the URI namespace."""
    if isinstance(type_uri, tuple):
        sources = sorted({vocab_source(t) for t in type_uri})
        return '/'.join(sources)
    if 'mmif.clams.ai' in type_uri:
        return 'MMIF'
    if 'lappsgrid.org' in type_uri:
        return 'LAPPS'
    return 'other'


def short_app_name(identifier: str) -> str:
    """``http://apps.clams.ai/whisper-wrapper/v15`` -> ``whisper-wrapper``"""
    # strip version suffix, then take last path component
    base = identifier.rsplit('/', 1)[0]
    return base.rstrip('/').rsplit('/', 1)[-1]


# ── data loading ─────────────────────────────────────────────────────

def load_latest_apps() -> list[dict]:
    """Walk ``docs/_apps/*/v*/metadata.json`` and return latest version
    metadata for each app."""
    apps = defaultdict(list)
    for metadata_f in APPS_DIR.glob('*/v*/metadata.json'):
        with open(metadata_f) as fh:
            meta = json.load(fh)
        app_dir_name = metadata_f.parent.parent.name
        apps[app_dir_name].append(meta)

    latest = []
    for app_dir_name, versions in sorted(apps.items()):
        versions.sort(key=lambda m: version_sort_key(m.get('app_version', '')))
        latest.append(versions[-1])       # highest version
    return latest


# ── report generation ────────────────────────────────────────────────

def build_io_maps(apps: list[dict]):
    """Return dicts mapping base‑type‑name -> list of app dicts, for both
    input and output types."""
    out_map: dict[str, list[dict]] = defaultdict(list)
    in_map: dict[str, list[dict]] = defaultdict(list)

    for app in apps:
        for o in app.get('output', []):
            uri = extract_type_uri(o)
            name = base_type_name(uri)
            out_map[name].append(app)

        for i in app.get('input', []):
            uri = extract_type_uri(i)
            name = base_type_name(uri)
            in_map[name].append(app)

    return out_map, in_map


def _format_io_list(items, direction: str) -> str:
    """Return a comma‑separated list of base type names for one app's
    input or output list."""
    names = []
    for item in items:
        uri = extract_type_uri(item)
        names.append(base_type_name(uri))
    return ', '.join(names) if names else '(none)'


def generate_report(apps: list[dict]) -> str:
    out_map, in_map = build_io_maps(apps)

    lines: list[str] = []
    w = lines.append          # shorthand

    w('# CLAMS App I/O Types Report')
    w('')
    w(f'*Auto‑generated by `scripts/io_type_report.py` on '
      f'{datetime.now().strftime("%Y-%m-%d")}*')
    w('')
    w('This report lists the input/output annotation types declared by the '
      'latest version of every published CLAMS app and groups apps that share '
      'the same types.')
    w('')

    # ── summary ──────────────────────────────────────────────────────
    w('## Summary')
    w('')
    w(f'| Metric | Count |')
    w(f'|--------|------:|')
    w(f'| Published apps (latest versions) | {len(apps)} |')
    w(f'| Distinct output types | {len(out_map)} |')
    w(f'| Distinct input types | {len(in_map)} |')
    w('')

    # ── grouped by output type ───────────────────────────────────────
    w('## Apps Grouped by Shared Output Type')
    w('')

    for type_name, type_apps in sorted(out_map.items(),
                                       key=lambda kv: (-len(kv[1]), kv[0])):
        # collect a sample URI so we can show the vocab source
        sample_uri = None
        for app in type_apps:
            for o in app.get('output', []):
                uri = extract_type_uri(o)
                if base_type_name(uri) == type_name:
                    sample_uri = uri
                    break
            if sample_uri:
                break
        source_tag = f' ({vocab_source(sample_uri)})' if sample_uri else ''

        w(f'### `{type_name}`{source_tag} — {len(type_apps)} app(s)')
        w('')
        w('| App | Version | Inputs |')
        w('|-----|---------|--------|')
        for app in sorted(type_apps, key=lambda a: a.get('name', '').lower()):
            name = app.get('name', '?')
            ver = app.get('app_version', '?')
            inputs = _format_io_list(app.get('input', []), 'input')
            w(f'| {name} | {ver} | {inputs} |')
        w('')

    # ── grouped by input type ────────────────────────────────────────
    w('## Apps Grouped by Shared Input Type')
    w('')

    for type_name, type_apps in sorted(in_map.items(),
                                       key=lambda kv: (-len(kv[1]), kv[0])):
        sample_uri = None
        for app in type_apps:
            for i in app.get('input', []):
                uri = extract_type_uri(i)
                if base_type_name(uri) == type_name:
                    sample_uri = uri
                    break
            if sample_uri:
                break
        source_tag = f' ({vocab_source(sample_uri)})' if sample_uri else ''

        w(f'### `{type_name}`{source_tag} — {len(type_apps)} app(s)')
        w('')
        w('| App | Version | Outputs |')
        w('|-----|---------|---------|')
        for app in sorted(type_apps, key=lambda a: a.get('name', '').lower()):
            name = app.get('name', '?')
            ver = app.get('app_version', '?')
            outputs = _format_io_list(app.get('output', []), 'output')
            w(f'| {name} | {ver} | {outputs} |')
        w('')

    # ── full reference table ─────────────────────────────────────────
    w('## Full App I/O Reference')
    w('')
    w('| App | Version | Input Types | Output Types |')
    w('|-----|---------|-------------|--------------|')
    for app in sorted(apps, key=lambda a: a.get('name', '').lower()):
        name = app.get('name', '?')
        ver = app.get('app_version', '?')
        inputs = _format_io_list(app.get('input', []), 'input')
        outputs = _format_io_list(app.get('output', []), 'output')
        w(f'| {name} | {ver} | {inputs} | {outputs} |')
    w('')

    # ── pipeline compatibility ───────────────────────────────────────
    w('## Pipeline Compatibility')
    w('')
    w('Shows which apps can feed their outputs into other apps\' inputs, '
      'based on matching annotation types.')
    w('')

    connections: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for producer in apps:
        p_name = producer.get('name', '?')
        p_ver = producer.get('app_version', '?')
        for o in producer.get('output', []):
            o_base = base_type_name(extract_type_uri(o))
            for consumer in apps:
                if consumer['identifier'] == producer['identifier']:
                    continue
                for i in consumer.get('input', []):
                    i_base = base_type_name(extract_type_uri(i))
                    if o_base == i_base:
                        c_name = consumer.get('name', '?')
                        pair = (c_name, o_base)
                        if pair not in connections[p_name]:
                            connections[p_name].append(pair)

    for producer, targets in sorted(connections.items()):
        w(f'**{producer}** can feed into:')
        w('')
        for consumer, via_type in sorted(targets):
            w(f'- {consumer} (via `{via_type}`)')
        w('')

    return '\n'.join(lines)


# ── main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Generate I/O type aggregation report for CLAMS apps.')
    parser.add_argument(
        '-o', '--output', type=Path, default=DEFAULT_OUTPUT,
        help=f'Output markdown path (default: {DEFAULT_OUTPUT})')
    args = parser.parse_args()

    latest_apps = load_latest_apps()
    print(f'Loaded {len(latest_apps)} apps (latest versions) '
          f'from {APPS_DIR}')

    report = generate_report(latest_apps)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print(f'Report written to {args.output} '
          f'({len(report)} bytes, {report.count(chr(10))} lines)')


if __name__ == '__main__':
    main()
