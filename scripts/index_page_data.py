import yaml
import sys
import json
from pathlib import Path
from collections import OrderedDict

# if len(sys.argv) > 1:
#     metadata_json_f = Path(sys.argv[1]) / 'metadata.json'
# else:
#     metadata_json_f = Path('metadata.json')
# metadata = json.load(open(metadata_json_f))
# app_id = metadata['identifier']
# app_version = metadata['app_version']
# # shortid is `http...` minus version string
# shortid = app_id.rsplit('/', 1)[0]

def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode('tag:yaml.org,2002:map', value)


yaml.add_representer(OrderedDict, represent_ordereddict)

folders = [OrderedDict([
    ("title", "Overview"),
    ("output", "web, pdf"),
    ("folderitems", [
        OrderedDict([
            ("title", "Using CLAMS App"),
            ("url", "/index.html"),
            ("output", "web, pdf"),
            ("type", "homepage")
        ])
    ])
])]

for d in (Path(__file__).parent.parent / "docs" / "apps").glob("*"):
    if d.name == ".DS_Store":
        continue
    folderitems = []
    for v in sorted(d.glob("*"), reverse=True):
        if v.name == ".DS_Store":
            continue
        folderitems.append(OrderedDict([
            ("title", v.name),
            ("url", f"{d.name}-{v.name}.html"),
            ("output", "web, pdf")
        ]))

    folders.append(OrderedDict([
        ("title", d.name),
        ("output", "web, pdf"),
        ("folderitems", folderitems)
    ]))

sidebar_entry = OrderedDict([
    ("title", "sidebar"),
    ("product", "App Directory"),
    ("version", "1.0"),
    ("folders", folders)
])

entries = {"entries": [sidebar_entry]}

'''
Example sidebar

entries:
- title: sidebar
  product: App Directory
  version: 1.0
  folders:

  - title: Overview
    output: web, pdf
    fodleritems:

    - title: Using CLAMS App
      url: /index.html
      output: web, pdf
      type: homepage

  - title: aapb-pua-kaldi-wrapper
    output: web, pdf
    folderitems:

    - title: v1
      url: /app-aapb-pua-kaldi-wrapper-v1.html
      output: web, pdf

    - title: v2
      url: /app-aapb-pua-kaldi-wrapper-v2.html
      output: web, pdf
'''

sidebar = yaml.dump(entries)

print(sidebar)


apps_fname = 'docs/_data/apps.json'
app_sidebar_fname = 'docs/_data/sidebars/apps_sidebar_script.yml'

with open(app_sidebar_fname, 'w') as f:
    yaml.dump(sidebar)



# existing_sidebar = yaml.load(open(app_sidebar_fname))
# existing_apps = json.load(open(apps_fname))

#
#
# if shortid not in existing_sidebar:
#     existing_sidebar[shortid] = []
# if app_version not in existing_sidebar[shortid]:
#     existing_sidebar[shortid].append(app_version)
#     existing_apps.append(metadata)
#
#     with open(app_sidebar_fname, 'w') as f:
#         yaml.dump(existing_sidebar, f, indent=2)
#     with open(apps_fname, 'w') as f:
#         json.dump(existing_apps, f)
