import os
import json

app_par_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', '_apps')

apps = [app for app in os.listdir(app_par_dir) if os.path.isdir(os.path.join(app_par_dir, app)) and not app.startswith('_')]

for app in apps:
    app_dir = os.path.join(app_par_dir, app)
    app_vers = [app_ver for app_ver in os.listdir(app_dir) if os.path.isdir(os.path.join(app_dir, app_ver))]
    app_submitters = dict()
    app_descriptions = {app_ver: tuple() for app_ver in app_vers}
    app_vers_sorted = list()
    for app_ver in app_vers:
        app_ver_dir = os.path.join(app_dir, app_ver)
        json_files = [json_file for json_file in os.listdir(app_ver_dir) if json_file[-5:] == '.json']
        for json_file in json_files:
            json_file_path = os.path.join(app_ver_dir, json_file)
            if json_file == 'metadata.json':
                with open(json_file_path) as metadata_file:
                    metadata = json.load(metadata_file)
                    app_title = metadata['name']
                    ver_num = metadata['app_version']
                    app_descriptions[app_ver] = metadata['description']
            elif json_file == 'submission.json':
                with open(json_file_path) as submission_file:
                    app_submission = json.load(submission_file)
                    app_submitter = app_submission['submitter']
                    submission_time = app_submission['time']
                    app_submitters[app_ver] = app_submitter
                    app_vers_sorted.append({'app_ver': app_ver, 'submission_time': submission_time})

    app_vers_sorted.sort(key=lambda x: x['submission_time'], reverse=True)
    app_description = app_descriptions[app_vers_sorted[0]['app_ver']]

    file_name = os.path.join(app_par_dir, app, 'index.md')

    f = open(file_name, "w")

    f.write('---\n')
    f.write("layout: posts\n")
    f.write("classes: wide\n")
    f.write(f"title: {app_title}\n")
    f.write("---\n")
    f.write(f"{app_description}\n")

    clams_url = "{{ url }}"

    for app_ver in app_vers_sorted:
        ver_num = app_ver['app_ver']
        app_submitter = app_submitters[ver_num]
        f.write(f"- [{ver_num}]({clams_url}/{app}/{ver_num}) ([`{app_submitter}`](https://github.com/{app_submitter}))\n")

    f.close()
