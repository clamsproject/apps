---
layout: posts
classes: wide
title: "Slate Detection (v1.0)"
date: 2023-06-15T03:53:26+00:00
---
## About this version

* Submitter: [kelleyl](https://github.com/kelleyl)
* Submission Time: 2023-06-15T03:53:26+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-slatedetection:v1.0](https://github.com/clamsproject/app-slatedetection/pkgs/container/app-slatedetection/v1.0)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This tool detects slates.**

* App ID: [http://apps.clams.ai/slatedetection/v1.0](http://apps.clams.ai/slatedetection/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-slatedetection](https://github.com/clamsproject/app-slatedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-slatedetection/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|Unit for output typeframe|string|N|frames|**_`frames`_**, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|N|30||
|stopAt|Frame number to stop processing|integer|N|540000||
|stopAfterOne|When True, processing stops after first timeframe is found|boolean|N|1|`false`, `true`|
|minFrameCount|Minimum number of frames required for a timeframe to be included in the output|integer|N|10||
|threshold|Threshold from 0-1, lower accepts more potential slates.|number|N|0||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
    * _properties_ = a complex object with the following keys:
        * _frameType_ = "string"
