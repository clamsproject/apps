---
layout: posts
classes: wide
title: "EAST Text Detection (v1.0)"
date: 2023-07-24T07:53:28+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-24T07:53:28+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-east-textdetection:v1.0](https://github.com/clamsproject/app-east-textdetection/pkgs/container/app-east-textdetection/v1.0)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**OpenCV-based text localization app that used EAST text detection model. Please visit the source code repository for full documentation.**

* App ID: [http://apps.clams.ai/east-textdetection/v1.0](http://apps.clams.ai/east-textdetection/v1.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-east-textdetection](https://github.com/clamsproject/app-east-textdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-east-textdetection/tree/v1.0))


#### Inputs
One of the following is required: [
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/ImageDocument/v1](http://mmif.clams.ai/vocabulary/ImageDocument/v1)  (required)
(any properties)


]
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
(any properties)


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|Unit for time points in the output. Only works with VideoDocument input.|string|N|frames|**_`frames`_**, `seconds`, `milliseconds`|
|frameType|Segments of video to run on. Only works with VideoDocument input and TimeFrame input. Empty value means run on the every frame types.|string|Y||**_``_**, `slate`, `chyron`, `rolling-credit`|
|sampleRatio|Frequency to sample frames. Only works with VideoDocument input, and without TimeFrame input. (when `TimeFrame` annotation is found, this parameter is ignored.)|integer|N|30||
|stopAt|Frame number to stop running. Only works with VideoDocument input. The default is roughly 2 hours of video at 30fps.|integer|N|2 * 60 * 60 * 30||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) 
    * _bboxtype_ = "text"
