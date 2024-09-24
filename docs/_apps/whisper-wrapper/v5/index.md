---
layout: posts
classes: wide
title: "Whisper Wrapper (v5)"
date: 2024-02-09T12:28:02+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-02-09T12:28:02+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v5](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v5)
- Release Notes

    > This version include addition of `modelLang` param and many other changes  
    > * **(BIG CHANGE)** timeunit is now millisecond (integer)  
    > * `modelLang` parameter is added for selecting language to instruct Whisper to use, Whisper will run in language detection mode if this parameter is not given.  
    > * When `modelLang` is set to `en`, load english only models instead of multilingual ones for speed and performance  
    > * skips empty segments from whisper when generating output MMIF  
    > * updated to clams-python 1.1.1

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.**

- App ID: [http://apps.clams.ai/whisper-wrapper/v5](http://apps.clams.ai/whisper-wrapper/v5)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v5))
- Analyzer Version: 20231117
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



]


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `modelSize`: optional, defaults to `tiny`

    - Type: string
    - Multivalued: False
    - Choices: **_`tiny`_**, `base`, `small`, `medium`, `large`


    > The size of the model to use. Can be "tiny", "base", "small", "medium", or "large".
- `modelLang`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > Language of the model to use, accepts two- or three-letter ISO 639 language codes, however Whisper only supports a subset of languages. If the language is not supported, error will be raised.For the full list of supported languages, see https://github.com/openai/whisper/blob/20231117/whisper/tokenizer.py . In addition to the langauge code, two-letter region codes can be added to the language code, e.g. "en-US" for US English. Note that the region code is only for compatibility and recording purpose, and Whisper neither detects regional dialects, nor use the given one for transcription. When the langauge code is not given, Whisper will run in langauge detection mode, and will use first few seconds of the audio to detect the language.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _timeUnit_ = "millisecond"

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)

- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

