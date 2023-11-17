---
layout: single
title: "Few Shot Classifier (v1.0)"
---
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-08-01T22:57:12+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-fewshotclassifier:v1.0](https://github.com/clamsproject/app-fewshotclassifier/pkgs/container/app-fewshotclassifier/v1.0)


### Few Shot Classifier (v1.0) [metadata.json](metadata.json)
###### This tool uses a vision model to classify video segments. Currenly supports "chyron" frame type.

* App ID: [http://apps.clams.ai/fewshotclassifier/v1.0](http://apps.clams.ai/fewshotclassifier/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-fewshotclassifier](https://github.com/clamsproject/app-fewshotclassifier) ([source tree of the submitted version](https://github.com/clamsproject/app-fewshotclassifier/tree/v1.0))
* Analyzer Version: 1.0
* Analyzer License: MIT


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|Unit for output timeframe|string|N|frames|**_`frames`_**, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|N|30||
|minFrameCount|Minimum number of frames required for a timeframe to be included in the output with a minimum value of 1|integer|N|60||
|threshold|Threshold from 0-1, lower accepts more potential labels.|number|N|0.8||
|finetunedFrameType|Name of fine-tuned model to use. All pre-installed models are named after the frame type they were fine-tuned for.<br/><br/>If an empty value is passed, the app will look for fewshots.csv file in the same directory as the app.py and create a new fine-tuned model based on the examples in that file.<br/><br/>At the moment, a model fine-tuned on "chyron" frame type is shipped as pre-installed.|string|N|chyron||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### frameType=string
