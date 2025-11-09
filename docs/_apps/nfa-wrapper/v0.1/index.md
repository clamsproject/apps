---
layout: posts
classes: wide
title: "CLAMS NFA Wrapper (v0.1)"
date: 2025-11-09T18:36:09+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-11-09T18:36:09+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-nfa-wrapper:v0.1](https://github.com/clamsproject/app-nfa-wrapper/pkgs/container/app-nfa-wrapper/v0.1)
- Release Notes

    > experiment first release of the app

## About this app (See raw [metadata.json](metadata.json))

**Wraps the [NVIDIA NeMo Forced Aligner tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/nemo_forced_aligner.html) to temporally align transcribed text with its audio source. **

- App ID: [http://apps.clams.ai/nfa-wrapper/v0.1](http://apps.clams.ai/nfa-wrapper/v0.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-nfa-wrapper](https://github.com/clamsproject/app-nfa-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-nfa-wrapper/tree/v0.1))
- Analyzer Version: 454fabc
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



]
- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
(of any properties)

    > Text content transcribed from audio input with no existing annotations.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `model`: optional, defaults to `fc_hybrid`

    - Type: string
    - Multivalued: False
    - Choices: **_`fc_hybrid`_**, `parakeet`, `conformer`, `fc_ctc`


    > NeMo ASR model to use. Choices: fc_hybrid, parakeet, conformer, fc_ctc. By default, the fc_hybrid model will be used.
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

- [http://mmif.clams.ai/vocabulary/Token/v1](http://mmif.clams.ai/vocabulary/Token/v1)
(of any properties)

    > Token from original text split on whitespace. `text` property stores the string value of the token. `start` and `end` properties indicate position of token in entire text. `document` property identifies source text document.
- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6)
    - _frameType_ = "speech"
    - _timeUnit_ = "milliseconds"

    > TimeFrame annotation representing the source audio segment corresponding to a given transcribed token, with `start` and `end` times given in milliseconds.
- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

    > Alignment between `Token` and `TimeFrame` annotations.
