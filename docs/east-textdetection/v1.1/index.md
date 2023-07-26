
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-26T19:06:10+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-east-textdetection:v1.1](https://github.com/clamsproject/app-east-textdetection/pkgs/container/app-east-textdetection/v1.1)


### EAST Text Detection (v1.1) [metadata.json](metadata.json)
###### OpenCV-based text localization app that used EAST text detection model. Please visit the source code repository for full documentation.

* App ID: [http://apps.clams.ai/east-textdetection/v1.1](http://apps.clams.ai/east-textdetection/v1.1)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-east-textdetection](https://github.com/clamsproject/app-east-textdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-east-textdetection/tree/v1.1))


#### Inputs
One of the following is required: [
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/ImageDocument/v1](http://mmif.clams.ai/vocabulary/ImageDocument/v1) (required)
###### ANY
]
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|timeUnit|Unit for time points in the output. Only works with VideoDocument input.|string|False|**_`frames`_**, `seconds`, `milliseconds`|
|frameType|Segments of video to run on. Only works with VideoDocument input and TimeFrame input. Empty value means run on the every frame types.|string|True|**_``_**, `slate`, `chyron`, `rolling-credit`|
|sampleRatio|Frequency to sample frames. Only works with VideoDocument input, and without TimeFrame input. (when `TimeFrame` annotation is found, this parameter is ignored.)|integer|False||
|stopAt|Frame number to stop running. Only works with VideoDocument input. The default is roughly 2 hours of video at 30fps.|integer|False||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|False|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) 
###### bboxtype=text
