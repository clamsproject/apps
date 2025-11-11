---
layout: posts
classes: wide
title: "Spoken Language Identification (v0.3)"
date: 2025-11-11T00:51:26+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-11-11T00:51:26+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-spoken-lid:v0.3](https://github.com/clamsproject/app-spoken-lid/pkgs/container/app-spoken-lid/v0.3)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Chunk-level language ID over audio based on OpenAI Whisper**

- App ID: [http://apps.clams.ai/spoken-lid/v0.3](http://apps.clams.ai/spoken-lid/v0.3)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-spoken-lid](https://github.com/clamsproject/app-spoken-lid) ([source tree of the submitted version](https://github.com/clamsproject/app-spoken-lid/tree/v0.3))
- Analyzer Version: v20250625
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

- `model`: optional, defaults to `tiny`

    - Type: string
    - Multivalued: False
    - Choices: **_`tiny`_**, `base`, `small`, `medium`, `large`, `turbo`


    > Whisper model size
- `chunk`: optional, defaults to `30`

    - Type: number
    - Multivalued: False


    > chunk/window length in seconds
- `top`: optional, defaults to `3`

    - Type: integer
    - Multivalued: False


    > top-k language scores
- `batchSize`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > number of windows processed in a batch
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

- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6)
    - _timeUnit_ = "seconds"
    - _labalSet_ = "https://raw.githubusercontent.com/openai/whisper/refs/tags/v20250625/whisper/tokenizer.py"

