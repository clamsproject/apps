---
layout: single
title: About
author_profile: true
toc: true
toc_sticky: true
permalink: /about/
---

The CLAMS App Directory is a public registry for free and open CLAMS apps, available at [https://clamsproject.github.io/apps](https://clamsproject.github.io/apps).

# Contributing to the App Directory

## What apps can be submitted?

The App Directory accepts submissions of CLAMS apps. All submitted apps must follow the CLAMS app interface specification.
In a nutshell, at the minimum, 

1. The app should be released as a pre-built container image, at a public container registry (e.g., Docker Hub, GitHub Container Registry, etc.).
2. The app should expose an HTTP API that follows [the CLAMS app interface specification](https://clamsproject.github.io/clams-python).
3. The app developer should provide correct and up-to-date app metadata - the app metadata will be the front page for your app. 
4. The app developer should maintain an issue tracking system on their own. The CLAMS App Directory does not provide issue tracking for the individual apps.

## How to submit an app?

First and foremost note that, at the moment, all the submissions are manually reviewed by the CLAMS team, hence the process can take some time.

Here is a step-by-step guide on how an app submission works:

- App submission and the associated review process are all done via the GitHub pull request system. 
- In essence, a _submission_ is a PR to the App Directory repository. 
- After the team reviewed the PR, the app will be _registered_ on the directory by merging the PR.
- However, we don't accept an app submission via a regular PR sent from a fork. 
    - Forked PRs for app directory feature development and bug fixes are alOther remarks
ways welcome, though!
- Instead, there are two ways to submit an app (i.e., to open a submission PR) to the directory:

### If you are a part of the CLAMS team (using the `clamsproject` GitHub organization)

If you started developing the app using the `clams develop` cookie cutter, the app submission process is very simple.
**Push a git tag to your app code repository** organized under the `clamsproject` GitHub organization.
If you want to leave a release note make the tag annotated and write the note in markdown syntax as the tag message.
The App Directory will use the tag name as the app version, and the tag message as the app release note.

Once you push the tag, a GH actions workflow included in the cookie cutter will automatically 

1. build a container image from the tagged app code and push to `clamsproject` GitHub Container Registry
2. call another GH actions worklow on the App Directory repository to create a PR with the app metadata and the container image URL.

More on the git tag.

- If you are not familiar with git tags, you should read the [official git documentation](https://git-scm.com/book/en/v2/Git-Basics-Tagging) first. "Git tags" ARE NOT "github releases". 
- The tag name should be a numerical form with `v` prefix (e.g., `v1`, `v2.0`, `v240630`). As long as the tag name is unique and numerical, you can use any form you like.

### If you are an external contributor (using your own GitHub organization)

If you are an external contributor, you can submit an app to the directory by manually opening an issue on the App Directory repository.

1. Prepare a git-based reference point for the following step. This reference will be used to _download_ your app code. Your code must provide `metadata.py` script in the project root that generates app metadata JSON string when directly run (`python metadata.py`). 
   1. Recommended way is to follow the same steps above to create a git tag (annotated tag to include a release note) and push it to your app code repository. 
   2. Alternative, you can use the git commit hash. This way, you're losing a way to provide a release note. Regardless, it is highly recommended to maintain an external changelog in the app repository.
2. Then, open an issue on the App Directory repository. **Pick an issue template for app submission**, and fill out the form. ([direct link to the app submission form](https://github.com/clamsproject/apps/issues/new?template=app_submission.md&title=CLAMS+App+Submission))

## What happens after the submission?

After the submission, the CLAMS team will review the app and the metadata. If the app is accepted, the team will merge the PR, and the app will be listed on the directory. 
If the app is rejected (mostly for mis-aligned app metadata), the team will close the PR with a reason for rejection. In such a case, the developer can re-submit the app after fixing the issues.
Note that, while the PR is open (i.e., the app is under review), a developer cannot re-submit the same app (the GitHub action we use to create an app submission PR will produce errors when duplicate app submission is detected).
If the developer wants to fix any problems or update the app, they can close the PR (if they are a part of the CLAMS team) or ask the CLAMS team to close the PR (if they are an external contributor). 

The re-submission process is simply to delete the tag from the remote app code repository and re-create the tag on the updated git commit. 
If the original submission was via a GH issue, the re-submission process is to create a new issue with the updated tag/commit and container image URL.

