---
layout: posts
classes: wide
title: "Whisper Wrapper (v12)"
date: 2024-10-16T16:03:25+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-10-16T16:03:25+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v12](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v12)
- Release Notes

    > added support for arm64 container image

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.**

- App ID: [http://apps.clams.ai/whisper-wrapper/v12](http://apps.clams.ai/whisper-wrapper/v12)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v12))
- Analyzer Version: 20240930
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
    - Choices: **_`tiny`_**, `True`, `base`, `b`, `small`, `s`, `medium`, `m`, `large`, `l`, `large-v2`, `l2`, `large-v3`, `l3`, `turbo`, `tu`


    > The size of the model to use. When `modelLang=en` is given, for non-`large` models, English-only models will be used instead of multilingual models for speed and accuracy. (For `large` models, English-only models are not available.) (also can be given as alias: tiny=t, base=b, small=s, medium=m, large=l, large-v2=l2, large-v3=l3, turbo=tu)
- `modelLang`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > Language of the model to use, accepts two- or three-letter ISO 639 language codes, however Whisper only supports a subset of languages. If the language is not supported, error will be raised.For the full list of supported languages, see https://github.com/openai/whisper/blob/20240930/whisper/tokenizer.py . In addition to the langauge code, two-letter region codes can be added to the language code, e.g. "en-US" for US English. Note that the region code is only for compatibility and recording purpose, and Whisper neither detects regional dialects, nor use the given one for transcription. When the langauge code is not given, Whisper will run in langauge detection mode, and will use first few seconds of the audio to detect the language.
- `task`: optional, defaults to `transcribe`

    - Type: string
    - Multivalued: False
    - Choices: **_`transcribe`_**, `translate`


    > (from whisper CLI) whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')
- `initialPrompt`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > (from whisper CLI) optional text to provide as a prompt for the first window.
- `conditionOnPreviousText`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > (from whisper CLI) if True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to getting stuck in a failure loop
- `noSpeechThreshold`: optional, defaults to `0.6`

    - Type: number
    - Multivalued: False


    > (from whisper CLI) if the probability of the <|nospeech|> token is higher than this value AND the decoding has failed due to `logprob_threshold`, consider the segment as silence
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation
- `runningTime`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)

- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

