import json
import sys
import urllib.request

import requests
from github import Github

# using an access token
CLAMS_BOT_PAT = sys.argv[1]
ORG = 'clamsproject'
g = Github(CLAMS_BOT_PAT)
o = g.get_organization(ORG)
# model_labels = {l.name: l for l in o.get_repo('.github').get_labels()}

app_repos = []
app_json = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/clamsproject/apps/main/docs/_data/apps.json').read().decode('utf8'))
registered_repos = set(app['url'] for app in app_json)
sys.stdout.write('repo,status,main_branch,last_commit\n')
for r in o.get_repos():
    if r.name.startswith('app-'):
        mainb = 'main'
        if r.archived:
            status = 'DISCONTINUED'
        else:
            res = requests.get(f'https://raw.githubusercontent.com/clamsproject/{r.name}/main/requirements.txt')
            if res.status_code > 400:
                res = requests.get(f'https://raw.githubusercontent.com/clamsproject/{r.name}/master/requirements.txt')
                mainb = 'master'
            req = res.text
            # print(req)
            for line in req.split('\n'):
                # print(line)
                if 'clams-' in line:
                    if '1.0.' in line:
                        if r.html_url in registered_repos:
                            status = 'REGISTERED'
                        else:
                            status = 'UPDATED'
                    else:
                        status = 'OUTDATED'

            if r.get_commits()[0].commit.message == 'added GHA to auto add issues to apps GHP':
                updated = r.get_commits()[1].commit.committer.date
            else:
                updated = r.get_commits()[0].commit.committer.date
        sys.stdout.write(f'https://github.com/clamsproject/{r.name},{status},{mainb},{updated}\n')
