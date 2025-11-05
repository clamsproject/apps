---
layout: posts
classes: wide
title: "Whisper Wrapper (v14)"
date: 2025-11-05T20:18:24+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-11-05T20:18:24+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v14](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v14)
- Release Notes

    > Major update includes ...  
    > - `modelSize` parameter is now `model`  
    > - `modelLang` parameter is now `language`  
    > (above changes to match openai's CLI argument names)  
    > - fixed app crashing when word-level timestamping outputs hallucinations

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.**

- App ID: [http://apps.clams.ai/whisper-wrapper/v14](http://apps.clams.ai/whisper-wrapper/v14)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v14))
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

- `model`: optional, defaults to `turbo`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) name of the Whisper model to use
- `language`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) language spoken in the audio, specify None to perform language detection
- `task`: optional, defaults to `transcribe`

    - Type: string
    - Multivalued: False
    - Choices: **_`transcribe`_**, `translate`


    > (from openai-whisper CLI) whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')
- `initialPrompt`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) optional text to provide as a prompt for the first window.
- `conditionOnPreviousText`: optional, defaults to `True`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) if True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to getting stuck in a failure loop
- `noSpeechThreshold`: optional, defaults to `0.6`

    - Type: number
    - Multivalued: False


    > (from openai-whisper CLI) if the probability of the <|nospeech|> token is higher than this value AND the decoding has failed due to `logprob_threshold`, consider the segment as silence
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

- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)

- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

