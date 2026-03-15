"""Generate I/O type aggregation report for published CLAMS apps.

Iterates all app version directories under ``docs/_apps/``, identifies
the latest version of each app, and groups them by shared input/output
annotation types.  The result is written to a markdown file.

Usage::

    python scripts/io_type_report.py > report.md
"""

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


APPS_DIR = Path('docs/_apps')


# ── anchor taxonomy ──────────────────────────────────────────────────

TEMPORAL_ANCHORS = frozenset({'TimeFrame', 'TimePoint'})
IMAGE_ANCHORS = frozenset({'BoundingBox'})
TEXTUAL_ANCHORS = frozenset({           # LAPPS Span subtypes
    'Token', 'Sentence', 'Paragraph', 'NounChunk',
    'NamedEntity', 'Markable', 'Span',
})
DOCUMENT_TYPES = frozenset({
    'TextDocument', 'AudioDocument', 'VideoDocument', 'ImageDocument',
})
AUDIO_CAPABLE = frozenset({'AudioDocument', 'VideoDocument'})

OUTPUT_PATTERN_ORDER = [
    'TextDocument + TimeFrame (+ Alignment)',
    'TextDocument + BoundingBox (+ Alignment)',
    'TextDocument from visual input (no BoundingBox)',
    'TimeFrame',
    'NamedEntity',
    'BoundingBox (no TextDocument)',
    'TimePoint',
    'Unclassified',
]


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


def _flatten_type_names(items: list) -> set[str]:
    """Return the set of all base type names from an I/O list,
    expanding OR-alternative sub-lists into individual names."""
    names = set()
    for item in items:
        uri = extract_type_uri(item)
        if isinstance(uri, tuple):
            for u in uri:
                names.add(base_type_name(u))
        else:
            names.add(base_type_name(uri))
    return names


def anchor_category(type_name: str) -> str | None:
    """Classify a base type name as an anchor category.

    :returns: ``'temporal'``, ``'image'``, ``'textual'``,
              ``'document'``, or ``None`` if not an anchor.
    """
    if type_name in TEMPORAL_ANCHORS:
        return 'temporal'
    if type_name in IMAGE_ANCHORS:
        return 'image'
    if type_name in TEXTUAL_ANCHORS:
        return 'textual'
    if type_name in DOCUMENT_TYPES:
        return 'document'
    return None


def infer_output_pattern(app: dict) -> str | None:
    """Classify an app by its output type signature.

    Rules applied in priority order:

    - ``TextDocument + BoundingBox``: output has both
    - ``TextDocument + TimeFrame``: output has both; or TextDocument
      with audio input; or TimeFrame output with text + audio inputs
      (forced alignment)
    - ``TextDocument from visual input``: output has TextDocument (no BB),
      input includes visual media but not pre-located BoundingBox
    - ``NamedEntity``: output has NamedEntity
    - ``BoundingBox`` (no TextDocument): output has BoundingBox only
    - ``TimeFrame``: output has TimeFrame (no TextDocument)
    - ``TimePoint``: output has TimePoint only

    :returns: Pattern string from ``OUTPUT_PATTERN_ORDER``, or ``None``.
    """
    out = _flatten_type_names(app.get('output', []))
    inp = _flatten_type_names(app.get('input', []))

    def has_out(*types): return any(t in out for t in types)
    def has_inp(*types): return any(t in inp for t in types)

    if has_out('TextDocument') and has_out('BoundingBox'):
        return 'TextDocument + BoundingBox (+ Alignment)'
    if has_out('TextDocument') and has_out('TimeFrame'):
        return 'TextDocument + TimeFrame (+ Alignment)'
    if has_out('TextDocument'):
        if has_inp('AudioDocument'):
            return 'TextDocument + TimeFrame (+ Alignment)'
        # recognition-only: consumes pre-located BB regions
        if has_inp('BoundingBox'):
            return None
        # visual media input → TD from visual source, no BB
        if has_inp('VideoDocument') or has_inp('ImageDocument'):
            return 'TextDocument from visual input (no BoundingBox)'
        return None  # text-processing utility or unclassified
    if has_out('NamedEntity'):
        return 'NamedEntity'
    if has_out('BoundingBox'):
        return 'BoundingBox (no TextDocument)'
    # Forced alignment: TimeFrame output + text + audio inputs
    if (has_out('TimeFrame')
            and has_inp('TextDocument')
            and AUDIO_CAPABLE & inp):
        return 'TextDocument + TimeFrame (+ Alignment)'
    if has_out('TimeFrame'):
        return 'TimeFrame'
    if has_out('TimePoint'):
        return 'TimePoint'
    return None


# ── alignment description parsing ────────────────────────────────────

def _parse_alignment_pairs(desc: str) -> list[tuple[str, str]]:
    """Extract ``(left_type, right_type)`` pairs from a free-text
    Alignment ``description`` field.

    Handles numbered-list format::

        1) `A` <-> `B`/`C`, 2) `D` <-> `E`

    and prose format::

        Alignment between `A` and `B` annotations.
    """
    pairs = []
    clauses = re.split(r'\d+\)', desc)
    for clause in clauses:
        halves = re.split(r'<->|↔|\band\b', clause, maxsplit=1)
        if len(halves) < 2:
            continue
        left_types = re.findall(r'`([^`]+)`', halves[0])
        right_types = re.findall(r'`([^`]+)`', halves[1])
        if not left_types or not right_types:
            continue
        for ltype in left_types:
            for rtype in right_types:
                pairs.append((ltype.strip(), rtype.strip()))
    return pairs


def _is_alignment(o: dict) -> bool:
    return isinstance(o, dict) and 'lignment' in o.get('@type', '')


def alignment_anchor_info(
        app: dict) -> tuple[list[tuple[str, str]], str]:
    """Return ``(pairs, source)`` describing an app's Alignment output.

    ``pairs`` is a list of ``(left_type, right_type)`` base-name strings.
    ``source`` is one of ``'described'``, ``'inferred'``,
    ``'underdeclared'``, or ``'n/a'``.

    Source precedence:

    - ``described``: extracted from the ``description`` field
    - ``inferred``: deduced from co-occurring anchor types in output
    - ``underdeclared``: Alignment present but insufficient anchor
      information to determine pairing
    """
    align_entry = next(
        (o for o in app.get('output', []) if _is_alignment(o)), None)
    if align_entry is None:
        return [], 'n/a'

    desc = align_entry.get('description', '')
    if desc:
        pairs = _parse_alignment_pairs(desc)
        if pairs:
            return pairs, 'described'

    # Infer from co-occurring anchor types in output
    by_cat: dict[str, list[str]] = defaultdict(list)
    for o in app.get('output', []):
        if o is align_entry:
            continue
        n = base_type_name(extract_type_uri(o)) if isinstance(o, dict) \
            else str(o)
        cat = anchor_category(n)
        if cat and n not in by_cat[cat]:
            by_cat[cat].append(n)

    cats = sorted(by_cat)
    if len(cats) >= 2:
        pairs = []
        for i, c1 in enumerate(cats):
            for c2 in cats[i + 1:]:
                for n1 in by_cat[c1]:
                    for n2 in by_cat[c2]:
                        pairs.append((n1, n2))
        return pairs, 'inferred'
    if len(cats) == 1:
        return [(n, '?') for n in by_cat[cats[0]]], 'underdeclared'
    return [], 'underdeclared'


def _pair_classification(left: str, right: str) -> str:
    """Classify an alignment pair by anchor categories."""
    lcat = anchor_category(left)
    rcat = anchor_category(right) if right != '?' else None
    if right == '?' or rcat is None:
        lc = lcat or 'unknown'
        return f'single-anchor ({lc}) ⚠'
    if lcat is None or rcat is None:
        return 'other'
    if lcat == rcat:
        return f'same-modal ({lcat}) ⚠'
    cats = tuple(sorted([lcat, rcat]))
    return f'{cats[0]}↔{cats[1]}'


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


# ── report section generators ─────────────────────────────────────────

def _pattern_section(apps: list[dict]) -> list[str]:
    """Return lines for the output type pattern grouping section."""
    by_pattern: dict[str, list[dict]] = defaultdict(list)
    for app in apps:
        key = infer_output_pattern(app) or 'Unclassified'
        by_pattern[key].append(app)

    lines: list[str] = []
    w = lines.append
    w('## Apps Grouped by Output Type Pattern')
    w('')
    w('Grouped by the combination of output annotation types, '
      'inferred from declared I/O metadata.')
    w('')
    for pattern in OUTPUT_PATTERN_ORDER:
        if pattern not in by_pattern:
            continue
        group = sorted(
            by_pattern[pattern], key=lambda a: a.get('name', '').lower())
        w(f'### {pattern} ({len(group)})')
        w('')
        w('| App | Version | Output Types |')
        w('|-----|---------|--------------|')
        for app in group:
            name = app.get('name', '?')
            ver = app.get('app_version', '?')
            outputs = _format_io_list(app.get('output', []), 'output')
            w(f'| {name} | {ver} | {outputs} |')
        w('')
    return lines


def _anchor_section(apps: list[dict]) -> list[str]:
    """Return lines for the anchor type and Alignment analysis section."""
    lines: list[str] = []
    w = lines.append
    w('## Anchor Type and Alignment Analysis')
    w('')
    w('Anchor types establish coordinate systems that other annotations '
      'reference. Temporal anchors: `TimeFrame`, `TimePoint`. '
      'Image anchors: `BoundingBox`. '
      'Textual anchors: LAPPS `Span` subtypes '
      '(`Token`, `Sentence`, `Paragraph`, `NamedEntity`, …).')
    w('')

    w('### Anchor Types Produced per App')
    w('')
    w('| App | Temporal | Image | Textual | Alignment |')
    w('|-----|----------|-------|---------|-----------|')
    for app in sorted(apps, key=lambda a: a.get('name', '').lower()):
        name = app.get('name', '?')
        temporal, image, textual = [], [], []
        has_align = False
        for o in app.get('output', []):
            if _is_alignment(o):
                has_align = True
                continue
            n = base_type_name(extract_type_uri(o)) \
                if isinstance(o, dict) else str(o)
            cat = anchor_category(n)
            if cat == 'temporal':
                temporal.append(n)
            elif cat == 'image':
                image.append(n)
            elif cat == 'textual' and n not in textual:
                textual.append(n)
        t = ', '.join(temporal) or '—'
        i = ', '.join(image) or '—'
        x = ', '.join(sorted(textual)) or '—'
        a = 'yes' if has_align else '—'
        w(f'| {name} | {t} | {i} | {x} | {a} |')
    w('')

    w('### Alignment Anchor Pairs')
    w('')
    w('Source/target anchor pairs extracted from the `description` '
      'metadata field (*described*) or inferred from co-occurring '
      'anchor types in the same output list (*inferred*). '
      '*Underdeclared*: `Alignment` is declared but anchor types '
      'are insufficient to determine pairing.')
    w('')
    w('| App | Left | Right | Classification | Source |')
    w('|-----|------|-------|----------------|--------|')
    for app in sorted(apps, key=lambda a: a.get('name', '').lower()):
        pairs, source = alignment_anchor_info(app)
        if source == 'n/a':
            continue
        name = app.get('name', '?')
        if not pairs:
            w(f'| {name} | — | — | underdeclared | — |')
            continue
        for left, right in pairs:
            cls = _pair_classification(left, right)
            w(f'| {name} | `{left}` | `{right}` | {cls} | {source} |')
    w('')
    return lines


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

    # ── proposed pattern grouping ─────────────────────────────────────
    lines.extend(_pattern_section(apps))

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
    w('| App | Version | Output Pattern | Input Types | Output Types |')
    w('|-----|---------|----------------|-------------|--------------|')
    for app in sorted(apps, key=lambda a: a.get('name', '').lower()):
        name = app.get('name', '?')
        ver = app.get('app_version', '?')
        pattern = infer_output_pattern(app) or '—'
        inputs = _format_io_list(app.get('input', []), 'input')
        outputs = _format_io_list(app.get('output', []), 'output')
        w(f'| {name} | {ver} | {pattern} | {inputs} | {outputs} |')
    w('')

    # ── anchor type and alignment analysis ───────────────────────────
    lines.extend(_anchor_section(apps))

    return '\n'.join(lines)


# ── main ─────────────────────────────────────────────────────────────

def main():
    import sys
    latest_apps = load_latest_apps()
    print(f'Loaded {len(latest_apps)} apps (latest versions) '
          f'from {APPS_DIR}', file=sys.stderr)

    print(generate_report(latest_apps))


if __name__ == '__main__':
    main()
