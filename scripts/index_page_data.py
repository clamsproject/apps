import datetime
import json
import sys
from pathlib import Path
import collections

app_index_fname = 'docs/_data/app-index.json'
apps_fname = 'docs/_data/apps.json'


def process_version(existing_index, existing_versions, existing_apps,
                     metadata, submission, submit_time):
    """Process a single app version and update indexes."""
    app_id = metadata['identifier']
    app_version = metadata['app_version']
    shortid = app_id.rsplit('/', 1)[0]

    if shortid not in existing_index:
        # New app
        existing_index[shortid] = {
            'description': metadata['description'],
            'latest_update': submit_time,
            'versions': [(app_version, submission['submitter'])]
        }
        existing_versions[shortid].add(app_version)
        existing_apps.append(metadata)
    elif app_version not in existing_versions[shortid]:
        # New version of existing app
        existing_index[shortid]['description'] = metadata['description']
        existing_index[shortid]['versions'].insert(
            0, (app_version, submission['submitter']))
        existing_index[shortid]['latest_update'] = submit_time
        existing_versions[shortid].add(app_version)
        existing_apps.append(metadata)


# Check if running in from-scratch mode
from_scratch = not (Path(app_index_fname).exists() and
                     Path(apps_fname).exists())

if from_scratch:
    print("Running in from-scratch mode: rebuilding from all versions")
    existing_index = {}
    existing_apps = []
    existing_versions = collections.defaultdict(set)

    # Find all version directories and their submission times
    version_dirs = []
    for version_dir in Path('docs/_apps').glob('*/v*/'):
        submission_json_f = version_dir / 'submission.json'
        metadata_json_f = version_dir / 'metadata.json'
        if submission_json_f.exists() and metadata_json_f.exists():
            submission = json.load(open(submission_json_f))
            version_dirs.append((
                datetime.datetime.fromisoformat(submission['time']),
                version_dir,
                metadata_json_f,
                submission_json_f
            ))

    # Sort by submission time (oldest first)
    version_dirs.sort(key=lambda x: x[0])

    # Process each version in chronological order
    for submit_time, version_dir, metadata_json_f, submission_json_f in \
            version_dirs:
        print(f'Processing {version_dir}')
        metadata = json.load(open(metadata_json_f))
        submission = json.load(open(submission_json_f))
        process_version(existing_index, existing_versions, existing_apps,
                        metadata, submission, submit_time)
else:
    # Incremental mode: process single new version
    if len(sys.argv) > 1:
        metadata_json_f = Path(sys.argv[1]) / 'metadata.json'
        submission_json_f = Path(sys.argv[1]) / 'submission.json'
    else:
        metadata_json_f = Path('metadata.json')
        submission_json_f = Path('submission.json')

    print(f'Using metadata from {metadata_json_f} and {submission_json_f}')
    metadata = json.load(open(metadata_json_f))
    submission = json.load(open(submission_json_f))

    # Load existing data
    existing_index = json.load(open(app_index_fname))
    existing_apps = json.load(open(apps_fname))

    # Build existing versions set and convert timestamps
    existing_versions = collections.defaultdict(set)
    for appname in existing_index:
        for version in existing_index[appname]['versions']:
            existing_versions[appname].add(version[0])
        existing_index[appname]['latest_update'] = \
            datetime.datetime.fromisoformat(
                existing_index[appname]['latest_update'])

    # Process the new version
    submit_time = datetime.datetime.fromisoformat(submission['time'])
    process_version(existing_index, existing_versions, existing_apps,
                    metadata, submission, submit_time)

sorted_existing_index = {}
for k, v in sorted(existing_index.items(), key=lambda item: item[1]['latest_update'], reverse=True):
    v['latest_update'] = v['latest_update'].isoformat()
    sorted_existing_index[k] = v

with open(app_index_fname, 'w') as f:
    json.dump(sorted_existing_index, f, indent=2)
with open(apps_fname, 'w') as f:
    json.dump(existing_apps, f)
