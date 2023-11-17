---
layout: single
title: "Chyron Detection (v1.0)"
---
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-24T21:50:08+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-chyron-detection:v1.0](https://github.com/clamsproject/app-chyron-detection/pkgs/container/app-chyron-detection/v1.0)


### Chyron Detection (v1.0) [metadata.json](metadata.json)
###### This tool detects chyrons, generates time segments.

* App ID: [http://apps.clams.ai/chyron-detection/v1.0](http://apps.clams.ai/chyron-detection/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-chyron-detection](https://github.com/clamsproject/app-chyron-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-chyron-detection/tree/v1.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|unit for output timeframe|string|N|frames|**_`frames`_**, `seconds`, `milliseconds`|
|sampleRatio|Frequency to sample frames|integer|N|5||
|minFrameCount|Minimum number of frames required for a timeframe to be included|integer|N|10||
|threshold|Threshold from 0-1, lower accepts more potential chyrons|number|N|0.5||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### properties={'frameType': 'chyron'}
