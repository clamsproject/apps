
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-20T02:49:35+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-inaspeechsegmenter-wrapper:v1.0](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/pkgs/container/app-inaspeechsegmenter-wrapper/v1.0)


### inaSpeechSegmenter Wrapper (v1.0) [metadata.json](metadata.json)
###### inaSpeechSegmenter is a CNN-based audio segmentation toolkit. The original software can be found at https://github.com/ina-foss/inaSpeechSegmenter .

* App ID: [http://apps.clams.ai/inaspeechsegmenter-wrapper/v1.0](http://apps.clams.ai/inaspeechsegmenter-wrapper/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-inaspeechsegmenter-wrapper](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v1.0))
* Analyzer Version: 0.7.6
* Analyzer License: MIT


#### Inputs
One of the following is required: [
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
]


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### timeunit=milliseconds
