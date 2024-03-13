---
layout: posts
classes: wide
title: "docTR Wrapper (v1.0)"
date: 2024-03-13T17:23:33+00:00
---
## About this version

* Submitter: [snewman-aa](https://github.com/snewman-aa)
* Submission Time: 2024-03-13T17:23:33+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-doctr-wrapper:v1.0](https://github.com/clamsproject/app-easyocr-wrapper/pkgs/container/app-easyocr-wrapper/v1.0)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**End to end OCR for extracting text from timeframes**

* App ID: [http://apps.clams.ai/doctr-wrapper/v1.0](http://apps.clams.ai/doctr-wrapper/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-easyocr-wrapper](https://github.com/clamsproject/app-easyocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-easyocr-wrapper/tree/v1.0))
* Analyzer Version: 0.8.1
* Analyzer License: Apache 2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/TimeFrame/v3](http://mmif.clams.ai/vocabulary/TimeFrame/v3)  (required)
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
* [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence) 
(any properties)
* [http://vocab.lappsgrid.org/Paragraph](http://vocab.lappsgrid.org/Paragraph) 
(any properties)
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
(any properties)
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/BoundingBox/v2](http://mmif.clams.ai/vocabulary/BoundingBox/v2) 
(any properties)
