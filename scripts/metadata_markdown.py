import io
import json
import re
import string
import sys
from pathlib import Path

if len(sys.argv) > 1:
    cwd = Path(sys.argv[1])
    if not cwd.exists():
        print(f'Path {cwd} does not exist.')
        sys.exit(1)
    out_f = open(cwd / 'index.md', 'w')
else:
    cwd = Path.cwd()
    out_f = sys.stdout

asterisk_note = '"*" as a property value means that the property is required but can be any value.'
multivalued_note = "_Multivalued_ means the parameter can have one or more values."
app_template = """
## About this app (See raw [metadata.json](metadata.json))

**${description}**

- App ID: [${identifier}](${identifier})
- App License: ${app_license}
- Source Repository: [${url}](${url}) ([source tree of the submitted version](${url}/tree/${app_version}))
"""

submission_template = """
## About this version

- Submitter: [${submitter}](https://github.com/${submitter})
- Submission Time: ${time}
- Prebuilt Container Image: [${image}](${image_webpage})
- Release Notes
"""

frontmatter_template = """---
layout: posts
classes: wide
title: "${name} (${app_version})"
date: ${time}
---"""

indentation = '    '


def convert_to_markdown(app_metadata, submission_metadata):
    markdown = io.StringIO()

    def markdown_link(url):
        return f"[{url}]({url})"

    def add_note(note):
        markdown.write(f"(**Note**: {note})\n\n")

    markdown.write(string.Template(frontmatter_template).substitute(**app_metadata, **submission_metadata))
    if not app_metadata['description']:
        app_metadata['description'] = '(no description provided by the developer)'
    else:
        app_metadata['description'] = re.sub(r'\n', '<br/>', app_metadata['description'])
        
    if submission_metadata:
        image_webpage = f'{app_metadata["url"]}/pkgs/container/{app_metadata["url"].rsplit("/",1)[-1]}/{app_metadata["app_version"]}'
        notes = f'{indentation}(no notes provided by the developer)'
        if 'releasenotes' in submission_metadata and submission_metadata['releasenotes']:
            # print(submission_metadata['releasenotes'])
            notes = '  \n'.join([f'{indentation}> {line}' for line in submission_metadata['releasenotes'].split('\n') if line])
        markdown.write(string.Template(submission_template).substitute(**submission_metadata, image_webpage=image_webpage))
        markdown.write(f'\n{notes}\n')
    markdown.write(string.Template(app_template).substitute(app_metadata))

    if 'analyzer_version' in app_metadata and app_metadata['analyzer_version']:
        markdown.write(f"- Analyzer Version: {app_metadata['analyzer_version']}\n")
    if 'analyzer_license' in app_metadata and app_metadata['analyzer_license']:
        markdown.write(f"- Analyzer License: {app_metadata['analyzer_license']}\n")
    if 'more' in app_metadata and app_metadata['more']:
        markdown.write(f"- More Info: {app_metadata['more']}\n")
    
    def io_to_markdown(io_spec):
        heading = f"- {markdown_link(io_spec['@type'])}{' (required)' if 'required' in io_spec and io_spec['required'] else ''}"
        desc = f'\n    > {io_spec["description"]}' if 'description' in io_spec else ''
        props = []
        if 'properties' in io_spec and io_spec['properties']:
            for k, v in io_spec['properties'].items():
                if isinstance(v, list):
                    props.append(f'{indentation}- _{k}_ = a list of {json.dumps(v)}')
                elif isinstance(v, dict):
                    props.append(f'{indentation}- _{k}_ = a complex object with the following keys:')
                    for k_in, v_in in v.items():
                        props.append(f'{indentation*2}- _{k_in}_ = {json.dumps(v_in)}')
                else:
                    props.append(f'    - _{k}_ = "{v}"')
        if props:
            props = '\n'.join(props)
        else:
            props = '(of any properties)'
            
        return f"{heading}\n{props}\n{desc}\n"

    def param_to_markdown(param_spec):

        if 'default' in param_spec:
            if param_spec['type'] == 'boolean':
                if param_spec['default'] == 0:
                    default_value = 'false'
                elif param_spec['default'] in (True, False):
                    default_value = str(param_spec['default']).lower()
                else:
                    default_value = 'true'
            else:
                default_value = param_spec['default']
        else:
            default_value = ''
            
        if 'choices' in param_spec:
            cs = param_spec['choices']
        elif param_spec['type'] == 'boolean':
            cs = ['false', 'true']
        else:
            cs = []
        choices = ', '.join(f'**_`{c}`_**' if c == default_value else f'`{c}`' for c in cs)
        req_or_def = 'required' if len(str(default_value)) == 0 else f"optional, defaults to `{default_value}`"
        heading = f"- `{param_spec['name']}`: {req_or_def}"
        safe_desc = re.sub(r"\n", "<br/>", param_spec["description"]) if 'description' in param_spec else ''
        desc = f'\n    > {safe_desc}'
        specs = f'\n    - Type: {param_spec["type"]}\n    - Multivalued: {param_spec["multivalued"]}\n'
        if choices:
            specs += f'    - Choices: {choices}\n'

        return f"{heading}\n{specs}\n{desc}\n"

    markdown.write('\n\n#### Inputs\n')
    add_note(asterisk_note)

    for input_ in app_metadata['input']:
        if isinstance(input_, list):
            markdown.write('One of the following is required: [\n')
            markdown.write(''.join(io_to_markdown(i) for i in input_))
            markdown.write('\n\n]\n')
        else:
            markdown.write(io_to_markdown(input_))

    markdown.write('\n\n#### Configurable Parameters\n')
    add_note(multivalued_note)

    if 'parameters' in app_metadata and app_metadata['parameters']:
        for param in app_metadata['parameters']:
            markdown.write(param_to_markdown(param))
    else:
        markdown.write('##### N/A\n')
    
    markdown.write('\n\n#### Outputs\n')
    add_note(asterisk_note)
    add_note("Not all output annotations are always generated.")

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
