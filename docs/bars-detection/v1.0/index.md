
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-24T08:27:02+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-barsdetection:v1.0](https://github.com/clamsproject/app-barsdetection/pkgs/container/app-barsdetection/v1.0)


### Bars Detection (v1.0) [metadata.json](metadata.json)
###### This tool detects SMPTE color bars.

* App ID: [http://apps.clams.ai/bars-detection/v1.0](http://apps.clams.ai/bars-detection/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-barsdetection](https://github.com/clamsproject/app-barsdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-barsdetection/tree/v1.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|timeUnit|Unit for output typeframe.|string|False|**_`frames`_**, `seconds`, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|False||
|stopAt|Frame number to stop processing.|integer|False||
|stopAfterOne|When True, processing stops after first timeframe is found.|boolean|False|`false`, **_`true`_**|
|minFrameCount|minimum number of frames required for a timeframe to be included in the output.|integer|False||
|threshold|Threshold from 0-1, lower accepts more potential slates.|number|False||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|False|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### typeSpecificProperty={'frameType': 'bars'}
