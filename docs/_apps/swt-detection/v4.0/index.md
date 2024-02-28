---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v4.0)"
date: 2024-02-27T21:53:26+00:00
---
## About this version

* Submitter: [marcverhagen](https://github.com/marcverhagen)
* Submission Time: 2024-02-27T21:53:26+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v4.0](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v4.0)
* Release Notes

    > Version 4.0

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits.**

* App ID: [http://apps.clams.ai/swt-detection/v4.0](http://apps.clams.ai/swt-detection/v4.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v4.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|startAt|Number of milliseconds into the video to start processing|integer|N|0||
|stopAt|Number of milliseconds into the video to stop processing|integer|N|10000000||
|sampleRate|Milliseconds between sampled frames|integer|N|1000||
|minFrameScore|Minimum score for a still frame to be included in a TimeFrame|number|N|0.01||
|minTimeframeScore|Minimum score for a TimeFrame|number|N|0.5||
|minFrameCount|Minimum number of sampled frames required for a TimeFrame|integer|N|2||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/TimeFrame/v2](http://mmif.clams.ai/vocabulary/TimeFrame/v2) 
    * _timeUnit_ = "milliseconds"
    * _labelset_ = a list of ["bars", "slate", "chyron", "credits", "NEG"]
* [http://mmif.clams.ai/vocabulary/TimePoint/v1](http://mmif.clams.ai/vocabulary/TimePoint/v1) 
    * _timeUnit_ = "milliseconds"
    * _labelset_ = a list of ["bars", "slate", "chyron", "credits", "NEG"]
