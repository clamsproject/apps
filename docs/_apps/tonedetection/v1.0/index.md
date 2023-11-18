---
layout: single
classes: wide
title: "Tone_Detector (v1.0)"
---
* Submitter: [MrSqually](https://github.com/MrSqually)
* Submission Time: 2023-07-24T17:50:36+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-tonedetection:v1.0](https://github.com/clamsproject/app-tonedetection/pkgs/container/app-tonedetection/v1.0)


### Tone_Detector (v1.0) [metadata.json](metadata.json)
###### Detects spans of monotonic audio within an audio file

* App ID: [http://apps.clams.ai/tonedetection/v1.0](http://apps.clams.ai/tonedetection/v1.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-tonedetection](https://github.com/clamsproject/app-tonedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-tonedetection/tree/v1.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|the unit for annotation output|string|N|seconds|**_`seconds`_**, **_`seconds`_**, `milliseconds`|
|lengthThreshold|minimum length threshold (in ms)|integer|N|2000||
|sampleSize|length for each segment of samples to be compared|integer|N|512||
|stopAt|stop point for audio processing (in ms). Defaults to the length of the file|integer|N|None||
|tolerance|threshold value for a "match" within audio processing|number|N|1.0||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### frameType=tone
