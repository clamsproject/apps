---
layout: posts
classes: wide
title: "Pyscenedetect Wrapper (v5)"
date: 2026-06-21T23:16:52+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-06-21T23:16:52+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-pyscenedetect-wrapper:v5](https://github.com/clamsproject/app-pyscenedetect-wrapper/pkgs/container/app-pyscenedetect-wrapper/v5)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-pyscenedetect-wrapper:v5" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > Update scenedetect version (to 0.7) and clams SDK version (to 1.7.1)

## About this app (See raw [metadata.json](metadata.json))

**CLAMS app wraps PySceneDetect and performs shot boundary detection on input videos**

- App ID: [http://apps.clams.ai/pyscenedetect-wrapper/v5](http://apps.clams.ai/pyscenedetect-wrapper/v5)
- App License: Apache2
- Source Repository: [https://github.com/clamsproject/app-pyscenedetect-wrapper](https://github.com/clamsproject/app-pyscenedetect-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-pyscenedetect-wrapper/tree/v5)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-pyscenedetect-wrapper/tree/v5" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: 0.7.0
- Analyzer License: BSD-3


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://clams.ai/vocabulary/type/VideoDocument/v2](http://clams.ai/vocabulary/type/VideoDocument/v2) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `mode`: optional, defaults to `content`

    - Type: string
    - Multivalued: False
    - Choices: **_`content`_**, `threshold`, `adaptive`


    > pick a scene detector algorithm, see http://scenedetect.com/projects/Manual/en/latest/cli/detectors.html
- `threshold`: optional, defaults to `27`

    - Type: number
    - Multivalued: False


    > threshold value to use in the detection algorithm. Note that the meaning of this numerical value differs for different detector algorithms.
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
    - _label_ = "shot"
    - _timeUnit_ = "frame"

