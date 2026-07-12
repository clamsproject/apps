---
layout: posts
classes: wide
title: "Tonedetection (v2.1)"
date: 2026-07-12T22:43:09+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-07-12T22:43:09+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-tonedetection:v2.1](https://github.com/clamsproject/app-tonedetection/pkgs/container/app-tonedetection/v2.1)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-tonedetection:v2.1" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > updated to the latest SDK

## About this app (See raw [metadata.json](metadata.json))

**Detects spans of monotonic audio within an audio file**

- App ID: [http://apps.clams.ai/tonedetection/v2.1](http://apps.clams.ai/tonedetection/v2.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-tonedetection](https://github.com/clamsproject/app-tonedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-tonedetection/tree/v2.1)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-tonedetection/tree/v2.1" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)


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

- `minToneDuration`: optional, defaults to `2000`

    - Type: integer
    - Multivalued: False


    > minimum length threshold (in ms)
- `stopAt`: optional, defaults to `3600000`

    - Type: integer
    - Multivalued: False


    > stop point for audio processing (in ms). Defaults to the length of the file
- `tolerance`: optional, defaults to `1`

    - Type: number
    - Multivalued: False


    > threshold value for a "match" within audio processing
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
    - _label_ = "tone"

