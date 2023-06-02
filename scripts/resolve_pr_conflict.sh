b=$(git branch 2>/dev/null | grep '\*' | cut -d ' ' -f 2)
app_name_ver=${b#*-}
app_ver=${app_name_ver##*.}
app_name=${app_name_ver%.*}
git fetch --all 
git merge origin/main --no-edit -X theirs
python scripts/index_page_data.py docs/$app_name/$app_ver


