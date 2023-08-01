
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

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|Unit of time to use in output.|string|N|frames|**_`frames`_**, `seconds`, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|N|30||
|stopAt|Frame number to stop processing|integer|N|9000||
|stopAfterOne|When True, processing stops after first timeframe is found|boolean|N|true|`false`, **_`true`_**|
|minFrameCount|Minimum number of frames required for a timeframe to be included in the output|integer|N|10||
|threshold|Threshold from 0-1, lower accepts more potential slates.|number|N|0.7||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### properties={'frameType': 'slate'}
