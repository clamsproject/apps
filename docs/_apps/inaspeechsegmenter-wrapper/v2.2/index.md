---
layout: posts
classes: wide
title: "inaSpeechSegmenter Wrapper (v2.2)"
date: 2026-06-22T00:41:02+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-06-22T00:41:02+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-inaspeechsegmenter-wrapper:v2.2](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/pkgs/container/app-inaspeechsegmenter-wrapper/v2.2)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-inaspeechsegmenter-wrapper:v2.2" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > Updated SDK version to 1.7

## About this app (See raw [metadata.json](metadata.json))

**inaSpeechSegmenter is a CNN-based audio segmentation toolkit. The original software can be found at https://github.com/ina-foss/inaSpeechSegmenter .**

- App ID: [http://apps.clams.ai/inaspeechsegmenter-wrapper/v2.2](http://apps.clams.ai/inaspeechsegmenter-wrapper/v2.2)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-inaspeechsegmenter-wrapper](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v2.2)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v2.2" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: 0.8.0
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

- `minTFDuration`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > minimum duration of a TimeFrame in milliseconds
- `silenceRatio`: optional, defaults to `3`

    - Type: integer
    - Multivalued: False


    > percentage ratio (0-100) of audio energy to to determine silence, ratio to mean every of the input audio.
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
    - _timeunit_ = "milliseconds"
    - _labelset_ = a list of ["silence", "speech", "noise", "music"]

    > The INA semgmenter uses 5-way classification (['noEnergy', 'female', 'male', 'noise', 'music']) and this wrapper remaps the labels to ['silence', 'speech', 'noise', 'music'], by 1) renaming `noEnergy` to `silence` 2) collapsing `female` and `male` into `speech` (leaving additional `gender` property). Note that the time frame annotations do not exhaustively cover the input audio, but only the segments.
