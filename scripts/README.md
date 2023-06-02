This directory contains scripts that are used to generate the HTML files 
aggregated json files for programmatic access of the entire metadata collection.

* `metadata_markdown.py` - generates markdown files for each app
  * (GHA way) run this without an argument from where `metadata.json` + `submission.json` files are located or
  * (manual way) run this with `docs/<appname>/<appversion>` argument (directory name where json files are located)
* `index_page_data.py` - generates aggregated json files
  * (GHA way) run this without an argument from the project root, where `metadata.json` for the new app is present in the root
  * (manual way) run this with `docs/<appname>/<appversion>` argument (directory name where json file is located)
* `resolve_pr_conflict.sh` - resolves conflicts in the PRs
  * if multiple app submission PRs are open, merging one of them will cause a conflict in the other
  * when this happens, locally check out the PR branch (`register/xx-<appname>.<appversion>`)
  * and run this from the project root without any argument 
  * then finally check new commits and push the new head to the remote repo