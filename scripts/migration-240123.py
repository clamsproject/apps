import json
import subprocess
import sys
import tempfile
import metadata_markdown
from pathlib import Path


def migrate(apps_dir):
    cloned = {}
    for app_dir in apps_dir.glob('[A-Za-z]*'):
        for ver_dir in app_dir.glob('v*'):
            with open(ver_dir / 'metadata.json') as f:
                app_repo_url = json.load(f)['url']
            if app_repo_url not in cloned:
                cloned[app_repo_url] = tempfile.TemporaryDirectory().name
                subprocess.run(['git', 'clone', app_repo_url, cloned[app_repo_url]], capture_output=True)
            tag_type = subprocess.run(['git', f'--git-dir={cloned[app_repo_url]}/.git',
                                             'cat-file', '-t', ver_dir.name], capture_output=True).stdout.decode('utf-8').strip()
            tag_notes = ''
            if tag_type == 'tag':
                tag_notes = subprocess.run(['git', f'--git-dir={cloned[app_repo_url]}/.git',
                                              'tag', '-l', '--format=\'%(contents)\'', ver_dir.name], 
                                             capture_output=True).stdout.decode('utf-8').strip()
                if tag_notes.startswith("'"):
                    tag_notes = tag_notes[1:]
                if tag_notes.endswith("'"):
                    tag_notes = tag_notes[:-1]
            with open(ver_dir / 'submission.json', 'r') as f:
                submission_metadata = json.load(f)
            if len(tag_notes) > 0:
                submission_metadata['releasenotes'] = tag_notes
            else:
                submission_metadata.pop('releasenotes', None)
            with open(ver_dir / 'submission.json', 'w') as f:
                json.dump(submission_metadata, f, indent=2)
            metadata_markdown.main(ver_dir)
            

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path(__file__).parent.parent / 'docs' / '_apps'
    migrate(directory)
