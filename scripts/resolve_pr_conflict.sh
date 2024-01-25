app_name_ver=$(git show $(git --no-pager log --oneline --no-color  | grep "adding metadata" | head -n 1 | cut -d ' ' -f 1) --name-only | grep metadata.json)
app_name=$(echo $app_name_ver | cut -d '/' -f 2)
app_ver=$(echo $app_name_ver | cut -d '/' -f 3)
git fetch --all 
# bring all files from main branch
git merge origin/main --no-commit --no-ff -X theirs
# and then, exclude all files not under `docs` dir,
# because a new submission branch MUST have files only under `docs dir. 
git restore --staged -- :^docs/*
git checkout -- *
# and finally bring all _data files back to `main` branch for re-generation later
git checkout origin/main -- docs/_data
# make an intermediate commit with semi-"merge" with main
git commit --no-edit
# regenerate submission files
python3 scripts/index_page_data.py docs/_apps/$app_name_ver
git add docs/_data
git commit -m 'regenerated aggregated metadata json files after conflict resolution'

