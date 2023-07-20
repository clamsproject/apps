
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-20T15:07:44+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-slatedetection:v2.0](https://github.com/clamsproject/app-slatedetection/pkgs/container/app-slatedetection/v2.0)


### Slate Detection (v2.0) [metadata.json](metadata.json)
###### This tool detects slates.

* App ID: [http://apps.clams.ai/slatedetection/v2.0](http://apps.clams.ai/slatedetection/v2.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-slatedetection](https://github.com/clamsproject/app-slatedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-slatedetection/tree/v2.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|timeUnit|Unit of time to use in output.|string|False|**_`frames`_**, `seconds`, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|False||
|stopAt|Frame number to stop processing|integer|False||
|stopAfterOne|When True, processing stops after first timeframe is found|boolean|False|`false`, **_`true`_**|
|minFrameCount|Minimum number of frames required for a timeframe to be included in the output|integer|False||
|threshold|Threshold from 0-1, lower accepts more potential slates.|number|False||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|False|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### properties={'frameType': 'slate'}
