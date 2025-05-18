import datetime
import json
import sys
from pathlib import Path
import collections

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
existing_versions = collections.defaultdict(set)
for appname in existing_index:
    for version in existing_index[appname]['versions']:
        existing_versions[appname].add(version[0])
    existing_index[appname]['latest_update'] = datetime.datetime.fromisoformat(existing_index[appname]['latest_update'])

existing_apps = json.load(open(apps_fname))

# totally new app 
if shortid not in existing_index:
    existing_index[shortid] = {
        'description': metadata['description'], 
        'latest_update': datetime.datetime.fromisoformat(submission['time']),
        'versions': [(app_version, submission['submitter'])]
    }
    existing_versions[shortid].add(app_version)
    existing_apps.append(metadata)
elif app_version not in existing_versions[shortid]:
    existing_index[shortid]['description'] = metadata['description']
    existing_index[shortid]['versions'].insert(0, (app_version, submission['submitter']))
    existing_index[shortid]['latest_update'] = datetime.datetime.fromisoformat(submission['time'])
    existing_versions[shortid].add(app_version)
    existing_apps.append(metadata)

sorted_existing_index = {}
for k, v in sorted(existing_index.items(), key=lambda item: item[1]['latest_update'], reverse=True):
    v['latest_update'] = v['latest_update'].isoformat()
    sorted_existing_index[k] = v

with open(app_index_fname, 'w') as f:
    json.dump(sorted_existing_index, f, indent=2)
with open(apps_fname, 'w') as f:
    json.dump(existing_apps, f)
