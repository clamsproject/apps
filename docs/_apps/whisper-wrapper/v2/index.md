---
layout: single
title: "Whisper Wrapper (v2)"
---
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-01T23:46:46+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v2](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v2)


### Whisper Wrapper (v2) [metadata.json](metadata.json)
###### A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.

* App ID: [http://apps.clams.ai/whisper-wrapper/v2](http://apps.clams.ai/whisper-wrapper/v2)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v2))
* Analyzer Version: 20230314
* Analyzer License: MIT


#### Inputs
One of the following is required: [
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
]


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

##### N/A


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
###### ANY
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### timeUnit=seconds
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
###### ANY
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
###### ANY
