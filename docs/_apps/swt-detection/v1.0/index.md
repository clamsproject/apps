---
layout: single
classes: wide
title: "Scene-with-text Detection (v1.0)"
---
## About this version

* Submitter: [marcverhagen](https://github.com/marcverhagen)
* Submission Time: 2023-11-22T15:13:53+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v1.0](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v1.0)
* Release Notes

    > Version 1.0 of the app

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits.**

* App ID: [http://apps.clams.ai/swt-detection/v1.0](http://apps.clams.ai/swt-detection/v1.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v1.0))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|model|the model to use, not implemented yet|string|N|vgg16||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
(any properties)
