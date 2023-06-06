
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-06T01:53:14+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-inaspeechsegmenter-wrapper:v1](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/pkgs/container/app-inaspeechsegmenter-wrapper/v1)


### inaSpeechSegmenter Wrapper (v1) [metadata.json](metadata.json)
###### inaSpeechSegmenter is a CNN-based audio segmentation toolkit. The original software can be found at https://github.com/ina-foss/inaSpeechSegmenter .

* App ID: [http://apps.clams.ai/inaaudiosegmenter-wrapper/v1](http://apps.clams.ai/inaaudiosegmenter-wrapper/v1)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-inaspeechsegmenter-wrapper](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v1))
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

##### N/A


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### timeunit=milliseconds
