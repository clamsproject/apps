import os
import shutil
from pathlib import Path
import sys
import metadata_markdown

def migration(directory):
    # iterate over the whole docs file
    # find all the subdirectories contains another subdirectories which start with v 
    # copy everything from there to the _apps directory, if '_apps' is not existing, create one
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            if dir.startswith('_'):
                continue
            full_dir_path = Path(root) / dir
            if any(subdir.name.startswith('v') for subdir in full_dir_path.iterdir() if subdir.is_dir()):
                destination_dir = os.path.join(directory, '_apps')
                if not os.path.isdir(destination_dir):
                    os.makedirs(destination_dir)
                destination_dir = Path(destination_dir) / full_dir_path.relative_to(directory)
                shutil.move(full_dir_path, destination_dir)
        destination_dir = os.path.join(directory, '_apps')
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
