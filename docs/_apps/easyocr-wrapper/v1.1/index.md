---
layout: single
classes: wide
title: "Easyocr Wrapper (v1.1)"
---
* Submitter: [snewman-aa](https://github.com/snewman-aa)
* Submission Time: 2024-01-18T18:34:19+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-easyocr-wrapper:v1.1](https://github.com/clamsproject/app-easyocr-wrapper/pkgs/container/app-easyocr-wrapper/v1.1)


### Easyocr Wrapper (v1.1) [metadata.json](metadata.json)
###### Using EasyOCR to extract text from timeframes

* App ID: [http://apps.clams.ai/easyocr-wrapper/v1.1](http://apps.clams.ai/easyocr-wrapper/v1.1)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-easyocr-wrapper](https://github.com/clamsproject/app-easyocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-easyocr-wrapper/tree/v1.1))
* Analyzer Version: 1.7.0
* Analyzer License: Apache 2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|sampleFrames|Number of frames to sample from timeframe|integer|N|1||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
###### ANY
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
###### ANY
* [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) 
###### ANY
* [http://mmif.clams.ai/vocabulary/TimePoint/v1](http://mmif.clams.ai/vocabulary/TimePoint/v1) 
###### ANY
