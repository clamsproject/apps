
* Submitter: [MrSqually](https://github.com/MrSqually)
* Submission Time: 2023-07-12T15:55:42+00:00
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

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|timeUnit|the unit for annotation output|string|False|**_`seconds`_**, `milliseconds`|
|lengthThreshold|minimum length threshold (in ms)|integer|False||
|sampleSize|length for each segment of samples to be compared|integer|False||
|stopAt|stop point for audio processing (in ms). Defaults to the length of the file|integer|False||
|tolerance|threshold value for a "match" within audio processing|number|False||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|False|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### frameType=tone
