
* Submitter: [MrSqually](https://github.com/MrSqually)
* Submission Time: 2023-06-06T13:36:41+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-tonedetection:v1.0](http://mmif.clams.ai/apps/tonesdetection/v1/pkgs/container/v1/v1.0)


### Tone_Detector (v1.0) [metadata.json](metadata.json)
###### Detects spans of monotonic audio within an audio file

* App ID: [http://apps.clams.ai/tonesdetection/v1.0](http://apps.clams.ai/tonesdetection/v1.0)
* App License: Apache 2.0
* Source Repository: [http://mmif.clams.ai/apps/tonesdetection/v1](http://mmif.clams.ai/apps/tonesdetection/v1) ([source tree of the submitted version](http://mmif.clams.ai/apps/tonesdetection/v1/tree/v1.0))
* Analyzer Version: 0.4.9
* Analyzer License: GPLv3


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
