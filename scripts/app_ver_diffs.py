import json
import sys

from pathlib import Path

import deepdiff

app_directory = sys.argv[1]
vers = Path(app_directory).glob("v*")
metadata_by_vers = {}
for ver in vers:
    metadata_by_vers[ver.name] = json.load(open(ver / "metadata.json"))


print('###', app_directory)
vs = sorted(metadata_by_vers.keys(), reverse=True)
if len(vs) > 1:
    for nv, ov in zip(vs[:-1], vs[1:]):
        print('####', nv, ov)
        print(deepdiff.DeepDiff(metadata_by_vers[nv], metadata_by_vers[ov], ignore_order=True).to_json(indent=2))
