import json
import sys
import datetime
from pathlib import Path

import metadata_markdown


def migrate(apps_dir):
    migrate_app_pages(apps_dir)
    migrate_app_index()
    

def migrate_app_pages(apps_dir):
    for app_dir in apps_dir.glob('[A-Za-z]*'):
        for ver_dir in app_dir.glob('v*'):
            metadata_markdown.main(ver_dir)
            
            
def migrate_app_index():
    all_apps = json.load(open(Path('docs') / '_data' / 'apps.json'))
    app_index = {}
    for metadata in all_apps:
        app_id = metadata['identifier']
        app_version = metadata['app_version']
        shortid = app_id.rsplit('/', 1)[0]
        veryshortid = shortid.rsplit('/', 1)[1]
        submission = json.load(open(Path('docs') / '_apps' / veryshortid / app_version / 'submission.json'))
        if shortid not in app_index:
            app_index[shortid] = {
                'description': metadata['description'],
                'latest_update': datetime.datetime.fromisoformat(submission['time']),
                'versions': []
            }
        app_index[shortid]['versions'].append((app_version, submission['submitter']))
        new_time = datetime.datetime.fromisoformat(submission['time'])
        if new_time > app_index[shortid]['latest_update']:
            app_index[shortid]['latest_update'] = new_time

    new_app_index = {}
    for k, v in sorted(app_index.items(), key=lambda item: item[1]['latest_update'], reverse=True):
        v['latest_update'] = v['latest_update'].isoformat()
        v['versions'].sort(reverse=True)
        new_app_index[k] = v
    with open(Path('docs') / '_data' / 'app-index.json', 'w') as f:
        json.dump(new_app_index, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path(__file__).parent.parent / 'docs' / '_apps'
    migrate(directory)
