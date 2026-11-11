---
layout: posts
classes: wide
title: "MMS Spoken LID (v0.1)"
date: 2026-11-11T22:23:34+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-11-11T22:23:34+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-mms-spoken-lid:v0.1](https://github.com/clamsproject/app-mms-spoken-lid/pkgs/container/app-mms-spoken-lid/v0.1)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-mms-spoken-lid:v0.1" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > first experimental release, copying params from other sLID apps

## About this app (See raw [metadata.json](metadata.json))

**Spoken language identification over fixed-length windows of an audio track, using the MMS language identification models. Consecutive windows with the same language can be merged into one TimeFrame.**

- App ID: [http://apps.clams.ai/mms-spoken-lid/v0.1](http://apps.clams.ai/mms-spoken-lid/v0.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-mms-spoken-lid](https://github.com/clamsproject/app-mms-spoken-lid) ([source tree of the submitted version](https://github.com/clamsproject/app-mms-spoken-lid/tree/v0.1)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-mms-spoken-lid/tree/v0.1" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer License: CC-BY-NC-4.0


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

- `model`: optional, defaults to `facebook/mms-lid-4017`

    - Type: string
    - Multivalued: False
    - Choices: `facebook/mms-lid-126`, `facebook/mms-lid-256`, `facebook/mms-lid-512`, `facebook/mms-lid-1024`, `facebook/mms-lid-2048`, **_`facebook/mms-lid-4017`_**


    > MMS LID model, by the number of languages it labels.
- `windowMs`: optional, defaults to `10000`

    - Type: integer
    - Multivalued: False


    > Window length in milliseconds.
- `minLastWindowMs`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Shortest final window to keep, in milliseconds. 0 keeps any final window.
- `tfMerge`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Join consecutive windows with the same label into one TimeFrame. When false, each window becomes its own TimeFrame, with one score.
- `labelMap`: optional, defaults to `[]`

    - Type: string
    - Multivalued: True


    > Labels to keep, as "IN:OUT" (rename IN to OUT) or "IN" (keep IN as it is). Other labels become "-". Empty keeps every label of the model. See README.md in the app repository for how the label is chosen.
- `minLabelScore`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > Minimum score for a label from labelMap to be kept; a window whose best mapped label scores less becomes "-". Only applies with labelMap.
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

    > Each TimeFrame covers consecutive windows that MMS labels with the language `label`. Language labels are canonicalized to BCP 47 tags, and `labelMap` can reduce them; see README.md in the app repository for details. `labelset` lists all labels the view can have. `scores` lists, in time order, the MMS probability of `label` in each of those windows, one float in [0, 1] per window. Window i starts at `start` + i * `windowMs`; the last window ends at `end` and can be shorter. The probabilities are not calibrated.
