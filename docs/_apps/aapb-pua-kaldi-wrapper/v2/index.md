---
layout: single
classes: wide
title: "AAPB-PUA Kaldi Wrapper (v2)"
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-14T00:42:26+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-aapb-pua-kaldi-wrapper:v2](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper/pkgs/container/app-aapb-pua-kaldi-wrapper/v2)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Kaldi-based ASR software originally developed by PopUpArchive and hipstas, and later updated by Kyeongmin Rim at Brandeis University. Wrapped software can be found at https://github.com/brandeis-llc/aapb-pua-kaldi-docker . **

* App ID: [http://apps.clams.ai/aapb-pua-kaldi-wrapper/v2](http://apps.clams.ai/aapb-pua-kaldi-wrapper/v2)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper/tree/v2))
* Analyzer Version: v4
* Analyzer License: UNKNOWN


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
|use_speech_segmentation|When true, the app looks for existing TimeFrame { "frameType": "speech" } annotations, and runs ASR only on those frames, instead of entire audio files.|boolean|N|true|`false`, **_`true`_**|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
    * _timeUnit_ = "milliseconds"
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
(any properties)
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
(any properties)
