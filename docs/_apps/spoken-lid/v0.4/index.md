---
layout: posts
classes: wide
title: "Spoken Language Identification (v0.4)"
date: 2026-07-12T22:39:02+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-07-12T22:39:02+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-spoken-lid:v0.4](https://github.com/clamsproject/app-spoken-lid/pkgs/container/app-spoken-lid/v0.4)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-spoken-lid:v0.4" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > updated to the latest SDK

## About this app (See raw [metadata.json](metadata.json))

**Chunk-level language ID over audio based on OpenAI Whisper**

- App ID: [http://apps.clams.ai/spoken-lid/v0.4](http://apps.clams.ai/spoken-lid/v0.4)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-spoken-lid](https://github.com/clamsproject/app-spoken-lid) ([source tree of the submitted version](https://github.com/clamsproject/app-spoken-lid/tree/v0.4)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-spoken-lid/tree/v0.4" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: v20250625
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://clams.ai/vocabulary/type/AudioDocument/v2](http://clams.ai/vocabulary/type/AudioDocument/v2) (required)
(of any properties)

- [http://clams.ai/vocabulary/type/VideoDocument/v2](http://clams.ai/vocabulary/type/VideoDocument/v2) (required)
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

- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6)
    - _timeUnit_ = "seconds"
    - _labalSet_ = "https://raw.githubusercontent.com/openai/whisper/refs/tags/v20250625/whisper/tokenizer.py"

