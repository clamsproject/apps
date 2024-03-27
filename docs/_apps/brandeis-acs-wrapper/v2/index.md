---
layout: posts
classes: wide
title: "Brandeis ACS Wrapper (v2)"
date: 2023-07-24T05:42:05+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-24T05:42:05+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-brandeis-acs-wrapper:v2](https://github.com/clamsproject/app-brandeis-acs-wrapper/pkgs/container/app-brandeis-acs-wrapper/v2)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Brandeis Acoustic Classification & Segmentation (ACS) is a audio segmentation tool developed at Brandeis Lab for Linguistics and Computation. The original software can be found at https://github.com/brandeis-llc/acoustic-classification-segmentation .**

* App ID: [http://apps.clams.ai/brandeis-acs-wrapper/v2](http://apps.clams.ai/brandeis-acs-wrapper/v2)
* App License: Apache2.0
* Source Repository: [https://github.com/clamsproject/app-brandeis-acs-wrapper](https://github.com/clamsproject/app-brandeis-acs-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-brandeis-acs-wrapper/tree/v2))
* Analyzer Version: 1.11
* Analyzer License: Apache2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1)  (required)
(any properties)


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
    * _timeunit_ = "milliseconds"
