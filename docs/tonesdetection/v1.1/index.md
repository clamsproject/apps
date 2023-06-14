
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-14T14:10:47+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-tonedetection:v1.1](https://github.com/clamsproject/app-tonedetection/pkgs/container/app-tonedetection/v1.1)


### Tone_Detector (v1.1) [metadata.json](metadata.json)
###### Detects spans of monotonic audio within an audio file

* App ID: [http://apps.clams.ai/tonesdetection/v1.1](http://apps.clams.ai/tonesdetection/v1.1)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-tonedetection](https://github.com/clamsproject/app-tonedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-tonedetection/tree/v1.1))


#### Inputs
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|time_unit|the unit for annotation output|string|False|**_`seconds`_**, `milliseconds`|
|length_threshold|minimum length threshold (in ms)|integer|False||
|sample_size|length for each segment of samples to be compared|integer|False||
|stop_at|stop point for audio processing (in ms). Defaults to the length of the file|integer|False||
|tolerance|threshold value for a "match" within audio processing|number|False||


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### ANY
