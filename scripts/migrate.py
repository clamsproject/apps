import os
import shutil
from pathlib import Path
import sys
import metadata_markdown


def add_front_matter(file_path, title, sidebar, permalink, folder, keywords):
    with open(file_path, 'r') as file:
        content = file.read()

    front_matter = f"---\n"
    front_matter += f"title: {title}\n"
    front_matter += f"sidebar: {sidebar}\n"
    front_matter += f"permalink: {permalink}\n"
    front_matter += f"folder: {folder}\n"
    front_matter += f"keywords: {keywords}\n"
    front_matter += f"---\n"

    content_with_front_matter = front_matter + content

    with open(file_path, 'w') as file:
        file.write(content_with_front_matter)


def migration(directory):
    # iterate over the whole docs file
    # find all the subdirectories contains another subdirectories which start with v under the docs directory
    # copy everything from there to the apps directory, if 'apps' is not existing, create one
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            if '_site' in dirs:
                dirs.remove('_site')
            if 'apps' in dirs:
                dirs.remove('apps')
            full_dir_path = Path(root) / dir
            if any(subdir.name.startswith('v') for subdir in full_dir_path.iterdir() if subdir.is_dir()):
                destination_dir = os.path.join(directory, 'apps')
                if not os.path.isdir(destination_dir):
                    os.makedirs(destination_dir)
                destination_dir = Path(destination_dir) / full_dir_path.relative_to(directory)
                shutil.move(full_dir_path, destination_dir)
        destination_dir = os.path.join(directory, 'apps')

    # in the updated apps folder, for those files end with .mds, add frontmatter looks like
    # ---
    # title: app-aapb-pua-kaldi-wrapper/v1
    # sidebar: apps_sidebar
    # permalink: app-aapb-pua-kaldi-wrapper-v1.html
    # folder: aapb-pua-kaldi-wrapper
    # keywords: AudioDocument, TimeFrame
    # ---

    # Rename index.md files to appname-version.md
    for root, _, files in os.walk(destination_dir):
        for file in files:
            if file == 'index.md':
                dir_path = os.path.dirname(os.path.join(root, file))
                app_name, version = os.path.basename(dir_path).split('-v')
                new_file_name = f"{app_name}-{version}.md"
                new_file_path = os.path.join(dir_path, new_file_name)
                os.rename(os.path.join(root, file), new_file_path)

    for root, _, files in os.walk(destination_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                # Provide the values for front matter
                app_name, version = os.path.splitext(file)[0].split('-v')
                title = f"app-{app_name}/{version}"
                sidebar = 'apps_sidebar'
                permalink = f"app-{app_name}-v{version}.html"
                folder = app_name
                keywords = 'AudioDocument, TimeFrame'
                # Add front matter to the file
                add_front_matter(file_path, title, sidebar, permalink, folder, keywords)

    for root, _, files in os.walk(destination_dir):
        for file in files:
            if file == 'metadata.json':
                metadata_markdown.main(root)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
    else:
        directory = Path(__file__).parent.parent / 'docs'
    migration(directory)
