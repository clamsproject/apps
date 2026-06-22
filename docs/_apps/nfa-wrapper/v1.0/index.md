---
layout: posts
classes: wide
title: "CLAMS NFA Wrapper (v1.0)"
date: 2026-06-22T19:56:15+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-06-22T19:56:15+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-nfa-wrapper:v1.0](https://github.com/clamsproject/app-nfa-wrapper/pkgs/container/app-nfa-wrapper/v1.0)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-nfa-wrapper:v1.0" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > First stable release

## About this app (See raw [metadata.json](metadata.json))

**Wraps the [NVIDIA NeMo Forced Aligner tool](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tools/nemo_forced_aligner.html) to temporally align transcribed text with its audio source. **

- App ID: [http://apps.clams.ai/nfa-wrapper/v1.0](http://apps.clams.ai/nfa-wrapper/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-nfa-wrapper](https://github.com/clamsproject/app-nfa-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-nfa-wrapper/tree/v1.0)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-nfa-wrapper/tree/v1.0" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: 2.7.3
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://clams.ai/vocabulary/type/AudioDocument/v2](http://clams.ai/vocabulary/type/AudioDocument/v2) (required)
(of any properties)

- [http://clams.ai/vocabulary/type/VideoDocument/v2](http://clams.ai/vocabulary/type/VideoDocument/v2) (required)
(of any properties)



]
- [http://clams.ai/vocabulary/type/TextDocument/v2](http://clams.ai/vocabulary/type/TextDocument/v2) (required)
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
- `runningTime`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata
- `tfSamplingMode`: optional, defaults to `representatives`

    - Type: string
    - Multivalued: False
    - Choices: **_`representatives`_**, `single`, `all`


    > Sampling mode for TimeFrame annotations. Has no effect when the app does not process TimeFrames. "representatives" uses all representative timepoints if present, otherwise skips the TimeFrame. "single" uses the middle representative if present, otherwise extracts an image from the midpoint of the start/end interval (midpoint is calculated by floor division of the sum of start and end). "all" uses all target timepoints if present, otherwise extracts all images from the time interval.


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://clams.ai/vocabulary/type/Token/v1](http://clams.ai/vocabulary/type/Token/v1)
(of any properties)

    > Token from original text split on whitespace. `text` property stores the string value of the token. `start` and `end` properties indicate position of token in entire text. `document` property identifies source text document.
- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6)
    - _frameType_ = "speech"
    - _timeUnit_ = "milliseconds"

    > TimeFrame annotation representing the source audio segment corresponding to a given transcribed token, with `start` and `end` times given in milliseconds.
- [http://clams.ai/vocabulary/type/Alignment/v1](http://clams.ai/vocabulary/type/Alignment/v1)
(of any properties)

    > Alignment between `Token` and `TimeFrame` annotations.
