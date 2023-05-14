import os
import sys

apprepo = None
apptag = None
appcontainer = None
for line in sys.stdin:
    line = line.strip()
    if line.startswith('NAME'):
        apprepo = line.split(":", 1)[1].strip()
        gh_baseurl = 'https://github.com/'
        if apprepo.startswith(gh_baseurl):
            apprepo = apprepo[len(gh_baseurl):]
    if line.startswith('TAG'):
        apptag = line.split(":", 1)[1].strip()
    if line.startswith('CONTAINER'):
        appcontainer = line.split(":", 1)[1].strip()
        
if None in (apprepo, apptag):
    print('ERROR: missing apprepo or apptag')
    sys.exit(1)

env_file = os.getenv('GITHUB_ENV')

with open(env_file, 'a') as github_env:
    github_env.write(f'apprepo={apprepo}\n')
    github_env.write(f'apptag={apptag}\n')
    if appcontainer:
        github_env.write(f'appcontainer={appcontainer}\n')
