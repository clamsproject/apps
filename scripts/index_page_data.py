import json
import sys

fullid = sys.argv[1]
shortid, version = fullid.rsplit('/', 1)


app_index_fname = 'docs/_data/app-index.json'
apps_fname = 'docs/_data/apps.json'
existing_index = json.load(open(app_index_fname))
existing_apps = json.load(open(apps_fname))

# this relies on the fact the GH actions that runs this script
# places the metadata.json file in the current working directory
# then copy it to the app specific directory later
cur_app_metadata = json.load(open('metadata.json'))

if shortid not in existing_index:
    existing_index[shortid] = []
if version not in existing_index[shortid]:
    existing_index[shortid].append(version)
    existing_apps.append(cur_app_metadata)

    with open(app_index_fname, 'w') as f:
        json.dump(existing_index, f, indent=2)
    with open(apps_fname, 'w') as f:
        json.dump(existing_apps, f)
