---
layout: single
classes: wide
title: "Scenes-with-text Detection (v2.0)"
---
* Submitter: [marcverhagen](https://github.com/marcverhagen)
* Submission Time: 2024-01-16T17:15:09+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v2.0](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v2.0)


### Scenes-with-text Detection (v2.0) [metadata.json](metadata.json)
###### Detects scenes with text, like slates, chyrons and credits.

* App ID: [http://apps.clams.ai/swt-detection/v2.0](http://apps.clams.ai/swt-detection/v2.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v2.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|sampleRate|Milliseconds between sampled frames|integer|N|1000||
|minFrameScore|Minimum score for a still frame to be included in a TimeFrame|number|N|0.01||
|minTimeframeScore|Minimum score for a TimeFrame|number|N|0.25||
|minFrameCount|Minimum number of sampled frames required for a TimeFrame|integer|N|2||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### ANY
