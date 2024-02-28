---
layout: posts
classes: wide
title: "Easyocr Wrapper (v2.0)"
date: 2024-02-28T18:17:27+00:00
---
## About this version

* Submitter: [snewman-aa](https://github.com/snewman-aa)
* Submission Time: 2024-02-28T18:17:27+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-easyocr-wrapper:v2.0](https://github.com/clamsproject/app-easyocr-wrapper/pkgs/container/app-easyocr-wrapper/v2.0)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Using EasyOCR to extract text from timeframes**

* App ID: [http://apps.clams.ai/easyocr-wrapper/v2.0](http://apps.clams.ai/easyocr-wrapper/v2.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-easyocr-wrapper](https://github.com/clamsproject/app-easyocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-easyocr-wrapper/tree/v2.0))
* Analyzer Version: 1.7.0
* Analyzer License: Apache 2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)  (required)
(any properties)


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/TimePoint/v1](http://mmif.clams.ai/vocabulary/TimePoint/v1) 
(any properties)
