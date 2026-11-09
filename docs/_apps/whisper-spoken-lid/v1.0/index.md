---
layout: posts
classes: wide
title: "Whisper Spoken LID (v1.0)"
date: 2026-11-09T02:49:31+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-11-09T02:49:31+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-spoken-lid:v1.0](https://github.com/clamsproject/app-whisper-spoken-lid/pkgs/container/app-whisper-spoken-lid/v1.0)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-whisper-spoken-lid:v1.0" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > first public release

## About this app (See raw [metadata.json](metadata.json))

**Spoken language identification over fixed-length windows of an audio track, using the language detection of OpenAI Whisper. Consecutive windows with the same most probable language become one TimeFrame.**

- App ID: [http://apps.clams.ai/whisper-spoken-lid/v1.0](http://apps.clams.ai/whisper-spoken-lid/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-whisper-spoken-lid](https://github.com/clamsproject/app-whisper-spoken-lid) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-spoken-lid/tree/v1.0)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-whisper-spoken-lid/tree/v1.0" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: 20250625
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


    > Whisper model size.
- `windowMs`: optional, defaults to `30000`

    - Type: integer
    - Multivalued: False


    > Window length in milliseconds, at most 30000.
- `minLastWindowMs`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Shortest final window to keep, in milliseconds. 0 keeps any final window.
- `mergeWindows`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Join consecutive windows with the same most probable language into one TimeFrame. When false, each window becomes its own TimeFrame.
- `batchSize`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > Number of windows passed to the model at once.
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
    - _timeUnit_ = "milliseconds"
    - _document_ = "*"
    - _labelset_ = "*"
    - _label_ = "*"
    - _scores_ = "*"

    > Each TimeFrame covers consecutive windows whose most probable language is `label`, a whisper language code. `labelset` lists all language codes of the whisper model in use. `scores` lists, in time order, the probability whisper gave `label` in each of those windows, one float in [0, 1] per window. Window i starts at `start` + i * `windowMs`; the last window ends at `end` and can be shorter. The probabilities are not calibrated.
