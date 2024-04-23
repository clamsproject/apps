---
layout: posts
classes: wide
title: "CLAMS docTR Wrapper (v1.0)"
date: 2024-04-22T18:46:07+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2024-04-22T18:46:07+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-doctr-wrapper:v1.0](https://github.com/clamsproject/app-doctr-wrapper/pkgs/container/app-doctr-wrapper/v1.0)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**CLAMS app wraps the docTR, End-to-End OCR model, available at https://pypi.org/project/python-doctr . The model is capable of detecting text regions in the input image and recognizing text in the regions. The text-localized regions are organized hierarchically by the model into "pages" > "blocks" > "lines" > "words", and this CLAMS app translates them into `TextDocument`, `Paragraphs`, `Sentence`, and `Token` annotations to represent recognized text contents, then aligns them to `BoundingBox` annotations that represent the detected geometries. This hierarchical structure is also represented in the `TextDocument` annotation output as two newlines (`\n\n`) between "paragraphs", one newline (`\n`) between the "lines", and one space (" ") between the "words". For the text recognition, the model is internally configured to use the "parseq" recognition model, and only works with English text at the moment.**

* App ID: [http://apps.clams.ai/doctr-wrapper/v1.0](http://apps.clams.ai/doctr-wrapper/v1.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-doctr-wrapper](https://github.com/clamsproject/app-doctr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-doctr-wrapper/tree/v1.0))
* Analyzer Version: 0.8.1
* Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)  (required)
    * _representatives_ = "?"


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|tfLabel|The label of the TimeFrame annotation to be processed. By default (`[]`), all TimeFrame annotations will be processed, regardless of their `label` property values.|string|Y|[]||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
    * _@lang_ = "en"
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
    * _text_ = "*"
    * _word_ = "*"
* [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence) 
    * _text_ = "*"
* [http://vocab.lappsgrid.org/Paragraph](http://vocab.lappsgrid.org/Paragraph) 
    * _text_ = "*"
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/BoundingBox/v4](http://mmif.clams.ai/vocabulary/BoundingBox/v4) 
    * _label_ = "text"
