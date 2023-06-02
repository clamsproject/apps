import json
import sys
from pathlib import Path

if len(sys.argv) > 1:
    metadata_json_f = Path(sys.argv[1]) / 'metadata.json'
else:
    metadata_json_f = Path('metadata.json')
metadata = json.load(open(metadata_json_f))
app_id = metadata['identifier']
app_version = metadata['app_version']
# shortid is `http...` minus version string
shortid = app_id.rsplit('/', 1)[0]

app_index_fname = 'docs/_data/app-index.json'
apps_fname = 'docs/_data/apps.json'
existing_index = json.load(open(app_index_fname))
existing_apps = json.load(open(apps_fname))

if shortid not in existing_index:
    existing_index[shortid] = []
if app_version not in existing_index[shortid]:
    existing_index[shortid].append(app_version)
    existing_apps.append(metadata)

    with open(app_index_fname, 'w') as f:
        json.dump(existing_index, f, indent=2)
    with open(apps_fname, 'w') as f:
        json.dump(existing_apps, f)
