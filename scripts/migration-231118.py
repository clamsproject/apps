import sys
from pathlib import Path


def migrate(apps_dir):
    for app_dir in apps_dir.glob('[A-Za-z]*'):
        for ver_dir in app_dir.glob('v*'):
            with open(ver_dir / 'index.md') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line == 'layout: single\n':
                        lines.insert(i+1, 'classes: wide\n')
                        break
            with open(ver_dir / 'index.md', 'w') as f:
                f.writelines(lines)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path(__file__).parent.parent / 'docs' / '_apps'
    migrate(directory)
