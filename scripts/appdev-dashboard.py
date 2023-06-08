import enum
import json
import sys
import urllib.request
from datetime import datetime

import requests
from github import Github

# using an access token
CLAMS_BOT_PAT = sys.argv[1]
ORG = 'clamsproject'
g = Github(CLAMS_BOT_PAT)
o = g.get_organization(ORG)
# model_labels = {l.name: l for l in o.get_repo('.github').get_labels()}


class AppStatus(enum.Enum):
    REGISTERED = 0
    UPDATED = 1
    OUTDATED = 2
    DISCONTINUED = 3
    

class AppRepo(object):
    name: str
    status: AppStatus
    main_branch: str
    last_commit: datetime
    
    def __init__(self, n, s, b, time):
        self.name = n
        self.status = s
        self.main_branch = b
        self.last_commit = time
    
    def __lt__(self, other):
        if self.status.value < other.status.value:
            return True
        elif self.status.value == other.status.value:
            return self.last_commit > other.last_commit
        else:
            return False


app_repos = []
app_json = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/clamsproject/apps/main/docs/_data/apps.json').read().decode('utf8'))
registered_repos = set(app['url'] for app in app_json)
sys.stdout.write('repo,status,main_branch,last_commit\n')
for r in o.get_repos():
    if r.name.startswith('app-'):
        mainb = 'main'
        if r.archived:
            status = AppStatus.DISCONTINUED
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
                            status = AppStatus.REGISTERED
                        else:
                            status = AppStatus.UPDATED
                    else:
                        status = AppStatus.OUTDATED

            commits = r.get_commits()
            
            if commits[0].commit.message == 'added GHA to auto add issues to apps GHP':
                most_relevant_commit = commits[1]
            else:
                most_relevant_commit = commits[0]
            updated = most_relevant_commit.commit.committer.date
        app_repos.append(AppRepo(r.name, status, mainb, updated))
for app in sorted(app_repos):
    sys.stdout.write(f'https://github.com/clamsproject/{app.name},{app.status},{app.main_branch},{app.last_commit}\n')
