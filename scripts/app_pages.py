import os
import json

docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
app_index_fname = os.path.join(docs_dir, '_data', 'app-index.json')


def copy_button(text, label):
    """Inline clipboard button; the click handler lives in
    docs/_includes/footer/custom.html."""
    return (f'<button class="copy-btn" data-clip="{text}" '
            f'title="Copy {label}" aria-label="Copy {label}">\U0001F4CB</button>')


def version_line(version, link):
    """Single-line listing entry for one app version.

    ``link`` is the (relative or absolute) URL to the version's detail page.
    Shows submitter, submission date, and source/image links each followed
    by a copy button (source URL / prebuilt image tag).
    """
    repo = version['repo_url']
    repo_name = repo.rsplit('/', 1)[-1]
    tree_url = f"{repo}/tree/{version['version']}"
    pkg_url = f"{repo}/pkgs/container/{repo_name}/{version['version']}"
    date = version['time'][:10]
    submitter = version['submitter']
    return (
        f"- [{version['version']}]({link}) "
        f"([`@{submitter}`](https://github.com/{submitter}), {date}, "
        f"[source]({tree_url}){copy_button(tree_url, 'source URL')}, "
        f"[image]({pkg_url}){copy_button(version['image'], 'image tag')})\n"
    )


def main():
    apps = json.load(open(app_index_fname))
    for app_uri, app_details in apps.items():
        app_title = app_uri.rsplit('/', 1)[1]
        file_name = os.path.join(docs_dir, '_apps', app_title, 'index.md')
        with open(file_name, "w") as f:
            f.write('---\n')
            f.write("layout: posts\n")
            f.write("classes: wide\n")
            f.write(f"title: {app_title}\n")
            # places these app-level index pages at the bottom of atom feed
            f.write("date: 1970-01-01T00:00:00+00:00\n")
            f.write("---\n")
            f.write(f"{app_details['description']}\n")
            for version in app_details['versions']:
                # version detail pages live at <app>/<version>/, relative here
                f.write(version_line(version, version['version']))


if __name__ == "__main__":
    main()
