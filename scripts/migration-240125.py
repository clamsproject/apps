import json
import subprocess
import sys
import tempfile
import metadata_markdown
from pathlib import Path


def migrate(apps_dir):
    for app_dir in apps_dir.glob('[A-Za-z]*'):
        for ver_dir in app_dir.glob('v*'):
            metadata_markdown.main(ver_dir)
            

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path(__file__).parent.parent / 'docs' / '_apps'
    migrate(directory)
