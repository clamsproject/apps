---
layout: posts
classes: wide
title: "Distil Whisper Wrapper (v1.1)"
date: 2024-07-22T21:52:47+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-07-22T21:52:47+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-distil-whisper-wrapper:v1.1](https://github.com/clamsproject/app-distil-whisper-wrapper/pkgs/container/app-distil-whisper-wrapper/v1.1)
- Release Notes

    > Now based on SDK 1.3.0 with more universal parameters

## About this app (See raw [metadata.json](metadata.json))

**The wrapper of Distil-Whisper, avaliable models: distil-large-v3, distil-large-v2, distil-medium.en, distil-small.en. The default model is distil-small.en.**

- App ID: [http://apps.clams.ai/distil-whisper-wrapper/v1.1](http://apps.clams.ai/distil-whisper-wrapper/v1.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-distil-whisper-wrapper](https://github.com/clamsproject/app-distil-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-distil-whisper-wrapper/tree/v1.1))
- Analyzer Version: 1.0
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

- `modelSize`: optional, defaults to `distil-small.en`

    - Type: string
    - Multivalued: False
    - Choices: `distil-large-v3`, `distil-large-v2`, `distil-medium.en`, **_`distil-small.en`_**, `small`, `s`, `medium`, `m`, `large-v2`, `l2`, `large-v3`, `l3`


    > The size of the model to use. There are four size of model to use distil-large-v3, distil-large-v2, distil-medium.en, distil-small.en. You can also enter the abbreviation of the model as parameter. 'small' and 's' for distil-small.en; 'medium' and  'm' for distil-medium.en; 'large-v2' and 'l2' for distil-large-v2; 'large-v3' and 'l3' for distil-large-v3. The default model is distil-medium.en.)
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
    - _@lang_ = "en"

    > Fully serialized text content of the recognized text in the input audio/video.
- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

    > Alignments between 1) `TimeFrame` <-> `SENTENCE`, 2) `audio/video document` <-> `TextDocument`
- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

    > The smallest recognized unit of distil-whisper. Normally a complete sentence.
