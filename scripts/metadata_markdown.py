import io
import json
import string
import sys
from pathlib import Path

if len(sys.argv) > 1:
    cwd = Path(sys.argv[1])
    out_f = open(cwd / 'index.html', 'w')
else:
    cwd = Path.cwd()
    out_f = sys.stdout
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


def markdown_link(url):
    return f"[{url}]({url})"

markdown = io.StringIO()
appmetadata = json.load(open(cwd / 'metadata.json'))
if (cwd / 'submission.json').exists():
    submitmetadata = json.load(open(cwd / 'submission.json'))
    image_webpage = f'{appmetadata["url"]}/pkgs/container/{appmetadata["url"].rsplit("/",1)[-1]}/{appmetadata["app_version"]}'
    markdown.write(string.Template(submission_template).substitute(**submitmetadata, image_webpage=image_webpage))
markdown.write(string.Template(app_template).substitute(appmetadata))

if 'analyzer_version' in appmetadata and appmetadata['analyzer_version']:
    markdown.write(f"* Analyzer Version: {appmetadata['analyzer_version']}\n")
if 'analyzer_license' in appmetadata and appmetadata['analyzer_license']:
    markdown.write(f"* Analyzer License: {appmetadata['analyzer_license']}\n")
if 'more' in appmetadata and appmetadata['more']:
    markdown.write(f"* More Info: {appmetadata['more']}\n")
    
    
def io_to_markdown(io_spec):
    props = ', '.join(f'{k}={v}' for k, v in io_spec['properties'].items()) \
        if 'properties' in io_spec and io_spec['properties'] \
        else ""
    return f"* {markdown_link(io_spec['@type'])} {'(required)' if 'required' in io_spec and io_spec['required'] else ''}\n###### {props if props else 'ANY'}\n"


markdown.write('\n\n#### Inputs\n')
for input_ in appmetadata['input']:
    if isinstance(input_, list):
        markdown.write('One of the following is required: [\n')
        markdown.write(''.join(io_to_markdown(i) for i in input_))
        markdown.write(']\n')
    else:
        markdown.write(io_to_markdown(input_))

markdown.write('\n\n#### Configurable Parameters\n')
markdown.write('###### Multivalued parameters can have two or more values.\n\n')

if 'parameters' in appmetadata and appmetadata['parameters']:
    markdown.write('|Name|Description|Type|Multivalued|Choices|\n')
    markdown.write('|----|-----------|----|-----------|-------|\n')
    for param in appmetadata['parameters']:
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
for output in appmetadata['output']:
    markdown.write(io_to_markdown(output))

out_f.write(markdown.getvalue())
out_f.close()
