---
layout: posts
classes: wide
title: "Whisper Wrapper (v6)"
date: 2024-02-12T19:47:39+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2024-02-12T19:47:39+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v6](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v6)
* Release Notes

    > v6 fixes a bug running en-only large models since there is no en-only large model

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.**

* App ID: [http://apps.clams.ai/whisper-wrapper/v6](http://apps.clams.ai/whisper-wrapper/v6)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v6))
* Analyzer Version: 20231117
* Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


]


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|modelSize|The size of the model to use. When `modelLand=en` is given, for non-`large` models, English-only models will be used instead of multilingual models for speed and accuracy. (For `large` models, English-only models are not available.)|string|N|tiny|**_`tiny`_**, `True`, `base`, `b`, `small`, `s`, `medium`, `m`, `large`, `l`, `large-v2`, `l2`, `large-v3`, `l3`|
|modelLang|Language of the model to use, accepts two- or three-letter ISO 639 language codes, however Whisper only supports a subset of languages. If the language is not supported, error will be raised.For the full list of supported languages, see https://github.com/openai/whisper/blob/20231117/whisper/tokenizer.py . In addition to the langauge code, two-letter region codes can be added to the language code, e.g. "en-US" for US English. Note that the region code is only for compatibility and recording purpose, and Whisper neither detects regional dialects, nor use the given one for transcription. When the langauge code is not given, Whisper will run in langauge detection mode, and will use first few seconds of the audio to detect the language.|string|N|||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
(any properties)
* [http://mmif.clams.ai/vocabulary/TimeFrame/v2](http://mmif.clams.ai/vocabulary/TimeFrame/v2) 
    * _timeUnit_ = "millisecond"
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
(any properties)
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
(any properties)
* [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence) 
(any properties)
