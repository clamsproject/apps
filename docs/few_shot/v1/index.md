
* Submitter: [kelleyl](https://github.com/kelleyl)
* Submission Time: 2023-07-17T16:56:39+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-fewshotclassifier:v1](https://github.com/clamsproject/app-fewshotclassifier/pkgs/container/app-fewshotclassifier/v1)


### Few Shot Classification (v1) [metadata.json](metadata.json)
###### This tool uses a vision model to classify video segments by comparing them to examples

* App ID: [http://apps.clams.ai/few_shot/v1](http://apps.clams.ai/few_shot/v1)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-fewshotclassifier](https://github.com/clamsproject/app-fewshotclassifier) ([source tree of the submitted version](https://github.com/clamsproject/app-fewshotclassifier/tree/v1))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|timeUnit|Unit for output timeframe|string|False|`frames`, **_`milliseconds`_**|
|sampleRatio|Frequency to sample frames.|integer|False||
|minFrameCount|Minimum number of frames required for a timeframe to be included in the outputwith a minimum value of 1|integer|False||
|threshold|Threshold from 0-1, lower accepts more potential labels.|number|False||


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### frameType=string
