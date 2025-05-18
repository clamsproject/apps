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
    UNKNOWN = 0   # cannot infer status from the latest commit to the app codebase
    UPDATED = 1   # the HEAD matches major/minor version of the latest SDK release
    OUTDATED = 2  # the HEAD is behind the latest SDK release
    DISCONTINUED = 3  # app repo is public but archived
    

class AppRepo(object):
    name: str
    status: AppStatus
    main_branch: str
    last_commit: datetime
    clams_version: str
    
    def __init__(self, n, r, s, b, ctime, mtime, ver):
        self.name = n
        self.registered = r
        self.status = s
        self.main_branch = b
        self.creation = ctime
        self.last_commit = mtime
        self.clams_version = ver
    
    def __repr__(self):
        return f'https://github.com/clamsproject/{self.name},{self.registered},{self.clams_version},{self.status},{self.main_branch},{self.last_commit},{self.creation}'
    
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
latest_sdk_ver = json.loads(urllib.request.urlopen(
    'https://api.github.com/repos/clamsproject/clams-python/tags?per_page=1'
).read().decode('utf8'))[0]['name']
lmjr, lmnr, lpat = list(map(int, latest_sdk_ver.split('.')))
sys.stdout.write(f'repo,in_appdir,sdk-in-use,sdk-status (latest: {latest_sdk_ver}),main_branch,last_commit,start_date\n')
for r in o.get_repos():
    if r.name.startswith('app-'):
        
        branches = [b.name for b in r.get_branches()]
        if r.archived:
            mainb = 'N/A'
        elif 'main' in branches:
            mainb = 'main'
        elif 'master' in branches:
            mainb = 'master'
        elif len(branches) == 1:
            mainb = branches[0]
        else:
            mainb = 'main'
        req = requests.get(f'https://raw.githubusercontent.com/clamsproject/{r.name}/{mainb}/requirements.txt').text
        # print(req)
        ver = 'UNKNOWN'
        mjr = mnr = pat = 0
        registered = False
        for line in req.split('\n'):
            # print(line)
            if 'clams-python' in line and not line.startswith('#'):
                ver_m = re.search(r'\d+\.\d+\.\d+$', line)
                #  print(r.name, line, ver_m)
                if ver_m is not None:
                    ver = ver_m.group(0)
                    mjr, mnr, pat = list(map(int, ver.split('.')))
                if r.html_url in registered_repos:
                    registered = True
                if mjr >= lmjr and mnr >= lmnr and pat >= lpat:
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
        app_repos.append(AppRepo(r.name, registered, status, mainb, r.created_at, updated, ver))
for app in sorted(app_repos):
    sys.stdout.write(f'{app}\n')
