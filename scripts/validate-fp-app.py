import json
import sys

from pathlib import Path

app_directory = sys.argv[1]
app_metadata_json = Path(app_directory) / "metadata.json"
app_metadata = json.load(open(app_metadata_json))


def validate_app_license(license_string):
    if license_string in ["MIT", "GPLv3", "Apache 2.0"]:
        return True
    else:
        print("Invalid license string: {}".format(license_string))
        return False


def validate_codebase_url(codebase_url, identifier_string):
    gho_prefix = "https://github.com/clamsproject/"
    apps_pref = "http://apps.clams.ai/"
    if not codebase_url.startswith(gho_prefix):
        print("Invalid GH org: {}".format(codebase_url))
        return False
    if codebase_url[len(gho_prefix):] != f'app-{identifier_string[len(apps_pref):].split("/")[0]}':
        print(f"Invalid GH repo: {codebase_url} vs {identifier_string}")
        return False

print('===', app_metadata["name"])
validate_codebase_url(app_metadata["url"], app_metadata["identifier"])
validate_app_license(app_metadata["app_license"])
