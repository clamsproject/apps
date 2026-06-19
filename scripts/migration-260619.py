"""
Migration 2026-06-19 (apps issue #247).

Surfaces source/image/submission-time on the main listing and per-app
pages. This requires re-shaping ``docs/_data/app-index.json``: each
version entry used to be a ``[version, submitter]`` pair and is now a
dict (see ``index_page_data.version_entry``). This script:

  1. removes the stale app-index.json / apps.json so they rebuild fresh,
  2. regenerates them from every version's metadata/submission,
  3. regenerates the per-app index pages with the new single-line format,
  4. regenerates the per-version detail pages so the source/image lines
     get the new clipboard buttons.

The main listing (docs/index.md) is a Jekyll template rendered at build
time, so it needs no regeneration here.

Run from the repository root::

    python scripts/migration-260619.py
"""
import os
import sys
from pathlib import Path

# index_page_data / app_pages use repo-root-relative paths; make this
# script robust to the invocation directory.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / 'scripts'))

import index_page_data
import app_pages
import metadata_markdown


def migrate():
    os.chdir(REPO_ROOT)
    for fname in (index_page_data.app_index_fname, index_page_data.apps_fname):
        p = Path(fname)
        if p.exists():
            p.unlink()
            print(f'removed {fname}')
    index_page_data.main([])   # data files gone -> from-scratch rebuild
    app_pages.main()           # re-render per-app pages with the new format

    # re-render per-version detail pages (clipboard buttons on the
    # source-repository and prebuilt-image lines)
    for ver_dir in sorted(Path('docs/_apps').glob('*/v*/')):
        if (ver_dir / 'metadata.json').exists():
            metadata_markdown.main(str(ver_dir))
    print('regenerated per-version detail pages')


if __name__ == "__main__":
    migrate()
