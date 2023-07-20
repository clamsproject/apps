import re
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
    clams_version: str
    
    def __init__(self, n, s, b, time, ver):
        self.name = n
        self.status = s
        self.main_branch = b
        self.last_commit = time
        self.clams_version = ver
    
    def __repr__(self):
        return f'https://github.com/clamsproject/{self.name},{self.status},{self.clams_version},{self.main_branch},{self.last_commit}'
    
    def __lt__(self, other):
        if self.status.value < other.status.value:
            return True
        elif self.status.value == other.status.value:
            if AppStatus.DISCONTINUED in (self.status, other.status):
                return self.clams_version > other.clams_version
            return self.last_commit > other.last_commit
        else:
            return False


app_repos = []
app_json = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/clamsproject/apps/main/docs/_data/apps.json').read().decode('utf8'))
registered_repos = set(app['url'] for app in app_json)
sys.stdout.write('repo,status,SDK-ver,main_branch,last_commit\n')
for r in o.get_repos():
    if r.name.startswith('app-'):
        res = requests.get(f'https://raw.githubusercontent.com/clamsproject/{r.name}/main/requirements.txt')
        if r.archived:
            mainb = 'N/A'
        elif res.status_code >= 400:
            res = requests.get(f'https://raw.githubusercontent.com/clamsproject/{r.name}/master/requirements.txt')
            mainb = 'master'
        else:
            mainb = 'main'
        req = res.text
        # print(req)
        ver = 'UNKNOWN'
        for line in req.split('\n'):
            # print(line)
            if 'clams-python' in line and not line.startswith('#'):
                ver_m = re.search(r'\d+\.\d+\.\d+$', line)
                #  print(r.name, line, ver_m)
                if ver_m is not None:
                    ver = ver_m.group(0)
                if '1.0.' in line:
                    if r.html_url in registered_repos:
                        status = AppStatus.REGISTERED
                    else:
                        status = AppStatus.UPDATED
                else:
                    status = AppStatus.OUTDATED
        if r.archived:
            status = AppStatus.DISCONTINUED

        commits = r.get_commits()
        
        if commits[0].commit.message == 'added GHA to auto add issues to apps GHP':
            most_relevant_commit = commits[1]
        else:
            most_relevant_commit = commits[0]
        updated = 'N/A' if r.archived else most_relevant_commit.commit.committer.date
        app_repos.append(AppRepo(r.name, status, mainb, updated, ver))
for app in sorted(app_repos):
    sys.stdout.write(f'{app}\n')
