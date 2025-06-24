import os
import json

docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')

apps = json.load(open(os.path.join(docs_dir, '_data', 'app-index.json')))

for app_uri, app_details in apps.items():
    app_title = app_uri.rsplit('/', 1)[1]
    app_submitters = {ver: submitter for ver, submitter in app_details['versions']}
    app_description = app_details['description']

    file_name = os.path.join(docs_dir, '_apps', app_title, 'index.md')

    f = open(file_name, "w")

    f.write('---\n')
    f.write("layout: posts\n")
    f.write("classes: wide\n")
    f.write(f"title: {app_title}\n")
    # this will effectively make these app-level index pages placed at the bottom of atom feed
    f.write(f"date: 1970-01-01T00:00:00+00:00\n")
    f.write("---\n")
    f.write(f"{app_description}\n")

    for app_ver, app_submitter in app_submitters.items():
        f.write(f"- [{app_ver}]({app_ver}) ([`@{app_submitter}`](https://github.com/{app_submitter}))\n")

    f.close()
