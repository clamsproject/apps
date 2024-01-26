import datetime
import json
import sys
from pathlib import Path

if len(sys.argv) > 1:
    metadata_json_f = Path(sys.argv[1]) / 'metadata.json'
    submission_json_f = Path(sys.argv[1]) / 'submission.json'
else:
    metadata_json_f = Path('metadata.json')
    submission_json_f = Path('submission.json')
metadata = json.load(open(metadata_json_f))
submission = json.load(open(submission_json_f))
app_id = metadata['identifier']
app_version = metadata['app_version']
# shortid is `http...` minus version string
shortid = app_id.rsplit('/', 1)[0]

app_index_fname = 'docs/_data/app-index.json'
apps_fname = 'docs/_data/apps.json'
existing_index = json.load(open(app_index_fname))
existing_apps = json.load(open(apps_fname))

if shortid not in existing_index:
    existing_index[shortid] = {
        'description': metadata['description'], 
        'time': datetime.datetime.fromisoformat(submission['time']),
        'versions': [(app_version, submission['submitter'])]
    }
if app_version not in existing_index[shortid]:
    existing_index[shortid]['versions'].insert(0, (app_version, submission['submitter']))
    existing_index[shortid]['time'] = datetime.datetime.fromisoformat(submission['time'])
    existing_apps.append(metadata)
    
    for k, v in sorted(existing_index.items(), key=lambda item: item[1]['time'], reverse=True):
        v['time'] = v['time'].isoformat()
        v['versions'].sort(reverse=True)
    sorted_existing_index = {k: v for k, v in sorted(existing_index.items(), key=lambda item: item[1]['time'], reverse=True)}

    with open(app_index_fname, 'w') as f:
        json.dump(sorted_existing_index, f, indent=2)
    with open(apps_fname, 'w') as f:
        json.dump(existing_apps, f)
