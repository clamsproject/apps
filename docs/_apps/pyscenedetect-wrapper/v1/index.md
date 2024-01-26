---
layout: posts
classes: wide
title: "Pyscenedetect Wrapper (v1)"
date: 2023-06-16T06:50:24+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-16T06:50:24+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-pyscenedetect-wrapper:v1](https://github.com/clamsproject/app-pyscenedetect-wrapper/pkgs/container/app-pyscenedetect-wrapper/v1)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**(no description provided by the developer)**

* App ID: [http://apps.clams.ai/pyscenedetect-wrapper/v1](http://apps.clams.ai/pyscenedetect-wrapper/v1)
* App License: Apache2
* Source Repository: [https://github.com/clamsproject/app-pyscenedetect-wrapper](https://github.com/clamsproject/app-pyscenedetect-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-pyscenedetect-wrapper/tree/v1))
* Analyzer Version: 0.6.1
* Analyzer License: BSD-3


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|mode|pick a scene detector algorithm, see http://scenedetect.com/projects/Manual/en/latest/cli/detectors.html|string|N|content|**_`content`_**, `threshold`, `adaptive`|
|threshold|threshold value to use in the detection algorithm. Note that the meaning of this numerical value differs for different detector algorithms.|number|N|27||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
    * _frameType_ = "shot"
    * _timeUnit_ = "frame"
