import io
import json
import string
import sys
from pathlib import Path

app_template = """
### ${name} (${app_version}) [metadata.json](metadata.json)
###### ${description}

* App ID: [${identifier}](${identifier})
* App License: ${app_license}
* Source Repository: [${url}](${url}) ([source tree of the submitted version](${url}/tree/${app_version}))
"""

submission_template = """
* Submitter: [${submitter}](https://github.com/${submitter})
* Submission Time: ${time}
* Prebuilt Container Image: [${image}](${image_webpage})

"""

# it's important to have no empty lines at the beginning of the frontmatter template
frontmatter_template = """---
layout: single
title: "${name} (${app_version})"
collection: apps
permalink: ${apps_link}/${app_version}
---"""


def convert_to_markdown(app_metadata, submission_metadata):
    def markdown_link(url):
        return f"[{url}]({url})"

    markdown = io.StringIO()
    markdown.write(string.Template(frontmatter_template).substitute(app_metadata, apps_link=app_metadata["identifier"].rsplit("/")[-2]))
    if submission_metadata:
        image_webpage = f'{app_metadata["url"]}/pkgs/container/{app_metadata["url"].rsplit("/", 1)[-1]}/{app_metadata["app_version"]}'
        markdown.write(string.Template(submission_template).substitute(**submission_metadata, image_webpage=image_webpage))
    markdown.write(string.Template(app_template).substitute(app_metadata))

    if 'analyzer_version' in app_metadata and app_metadata['analyzer_version']:
        markdown.write(f"* Analyzer Version: {app_metadata['analyzer_version']}\n")
    if 'analyzer_license' in app_metadata and app_metadata['analyzer_license']:
        markdown.write(f"* Analyzer License: {app_metadata['analyzer_license']}\n")
    if 'more' in app_metadata and app_metadata['more']:
        markdown.write(f"* More Info: {app_metadata['more']}\n")
        
    def io_to_markdown(io_spec):
        props = ', '.join(f'{k}={v}' for k, v in io_spec['properties'].items()) \
            if 'properties' in io_spec and io_spec['properties'] \
            else ""
        return f"* {markdown_link(io_spec['@type'])} {'(required)' if 'required' in io_spec and io_spec['required'] else ''}\n###### {props if props else 'ANY'}\n"

    markdown.write('\n\n#### Inputs\n')
    for input_ in app_metadata['input']:
        if isinstance(input_, list):
            markdown.write('One of the following is required: [\n')
            markdown.write(''.join(io_to_markdown(i) for i in input_))
            markdown.write(']\n')
        else:
            markdown.write(io_to_markdown(input_))

    markdown.write('\n\n#### Configurable Parameters\n')
    markdown.write('###### Multivalued parameters can have two or more values.\n\n')

    if 'parameters' in app_metadata and app_metadata['parameters']:
        markdown.write('|Name|Description|Type|Multivalued|Choices|\n')
        markdown.write('|----|-----------|----|-----------|-------|\n')
        for param in app_metadata['parameters']:
            if 'default' in param:
                if param['type'] == 'boolean':
                    if param['default'] == 0:
                        default_value = 'false'
                    elif param['default'] in (True, False):
                        default_value = str(param['default']).lower()
                    else:
                        default_value = 'true'
                else:
                    default_value = param['default']
            else:
                default_value = ''
            if 'choices' in param:
                cs = param['choices']
            elif param['type'] == 'boolean':
                cs = ['false', 'true']
            else:
                cs = []
            choices = ', '.join(f'**_`{c}`_**' if c == default_value else f'`{c}`' for c in cs)
            markdown.write(f"|{param['name']}|{param['description']}|{param['type']}|{param['multivalued']}|{choices}|\n")
    else:
        markdown.write('##### N/A\n')
        
    markdown.write('\n\n#### Outputs\n')
    markdown.write('###### Note that not all output annotations are always generated.\n')
    for output in app_metadata['output']:
        markdown.write(io_to_markdown(output))
    
    return markdown


def main(directory_w_metadata=None):
    if directory_w_metadata is not None:
        cwd = Path(directory_w_metadata)
        out_f = open(cwd / 'index.md', 'w')
    else:
        cwd = Path.cwd()
        out_f = sys.stdout
    app_metadata = json.load(open(cwd / 'metadata.json'))
    submission_metadata = {}
    if (cwd / 'submission.json').exists():
        submission_metadata = json.load(open(cwd / 'submission.json'))
    markdown = convert_to_markdown(app_metadata, submission_metadata)
    out_f.write(markdown.getvalue())
    out_f.close()
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main(None)
