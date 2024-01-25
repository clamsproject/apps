---
layout: single
classes: wide
title: "Whisper Wrapper (v4)"
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2024-01-24T05:40:09+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v4](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v4)
* Release Notes

    > * updated to the latest whisper models  
    > * now ouputs `Sentence` annotations based on whisper's segmentation

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.**

* App ID: [http://apps.clams.ai/whisper-wrapper/v4](http://apps.clams.ai/whisper-wrapper/v4)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v4))
* Analyzer Version: 20231117
* Analyzer License: MIT


#### Inputs
One of the following is required: [
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


]


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|modelSize|The size of the model to use. Can be "tiny", "base", "small", "medium", or "large".|string|N|tiny|**_`tiny`_**, `base`, `small`, `medium`, `large`|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
    * _timeUnit_ = "seconds"
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
(any properties)
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
(any properties)
