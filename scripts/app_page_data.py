import os
import json

directory = '../docs/_apps'

apps = [app for app in os.listdir(directory) if os.path.isdir(os.path.join(directory, app)) and not app.startswith('_')]

for app in apps:
    app_dir = os.path.join(directory, app)
    app_vers = [app_ver for app_ver in os.listdir(app_dir) if os.path.isdir(os.path.join(app_dir, app_ver))]
    sorted_app_info = sorted([app_ver.lstrip('v') for app_ver in app_vers], reverse=True)  # sort versions from latest to earliest
    app_info_dict = {'v' + app_ver: tuple() for app_ver in sorted_app_info}
    for app_ver in app_vers:
        app_ver_dir = os.path.join(app_dir, app_ver)
        json_files = [json_file for json_file in os.listdir(app_ver_dir) if json_file[-5:] == '.json']
        for json_file in json_files:
            json_file_path = os.path.join(app_ver_dir, json_file)
            if json_file == 'metadata.json':
                with open(json_file_path) as metadata_file:
                    metadata = json.load(metadata_file)
                    title = metadata['name']
                    ver_num = metadata['app_version']
                    if ver_num.lstrip('v') == sorted_app_info[0]:
                        description = metadata['description']  # get description for the latest app version
            elif json_file == 'submission.json':
                with open(json_file_path) as submission_file:
                    submission = json.load(submission_file)
                    submitter = submission['submitter']

        app_info_dict[app_ver] = (ver_num, submitter)

    file_name = os.path.join(directory, app, 'index.md')

    f = open(file_name, "w")

    f.write('---\n')
    f.write("layout: posts\n")
    f.write("classes: wide\n")
    f.write(f"title: {title}\n")
    f.write("---\n")
    f.write(f"{description}\n")

    for app_info in app_info_dict:
        ver_num = app_info_dict[app_info][0]
        submitter = app_info_dict[app_info][1]
        f.write(f"- [{ver_num}](http://apps.clams.ai/{app}/{ver_num}) ([`{submitter}`](https://github.com/{submitter}))\n")

    f.close()
