
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-23T18:57:36+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-barsdetection:v1](https://github.com/clamsproject/app-barsdetection/pkgs/container/app-barsdetection/v1)


### Bars Detection (v1) [metadata.json](metadata.json)
###### This tool detects SMPTE Bars.

* App ID: [http://apps.clams.ai/bars-detection/v1](http://apps.clams.ai/bars-detection/v1)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-barsdetection](https://github.com/clamsproject/app-barsdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-barsdetection/tree/v1))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|timeUnit|Unit for output typeframe.|string|False|**_`frames`_**, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|False||
|stopAt|Frame number to stop processing.|integer|False||
|stopAfterOne|When True, processing stops after first timeframe is found.|boolean|False|`false`, `true`|
|minFrameCount|minimum number of frames required for a timeframe to be included in the output.|integer|False||


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### typeSpecificProperty={'frameType': 'string'}
