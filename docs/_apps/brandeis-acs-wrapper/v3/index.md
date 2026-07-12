---
layout: posts
classes: wide
title: "Brandeis ACS Wrapper (v3)"
date: 2026-07-12T22:29:38+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-07-12T22:29:38+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-brandeis-acs-wrapper:v3](https://github.com/clamsproject/app-brandeis-acs-wrapper/pkgs/container/app-brandeis-acs-wrapper/v3)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-brandeis-acs-wrapper:v3" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > updated to the latest SDK

## About this app (See raw [metadata.json](metadata.json))

**Brandeis Acoustic Classification & Segmentation (ACS) is a audio segmentation tool developed at Brandeis Lab for Linguistics and Computation. The original software can be found at https://github.com/brandeis-llc/acoustic-classification-segmentation .**

- App ID: [http://apps.clams.ai/brandeis-acs-wrapper/v3](http://apps.clams.ai/brandeis-acs-wrapper/v3)
- App License: Apache2.0
- Source Repository: [https://github.com/clamsproject/app-brandeis-acs-wrapper](https://github.com/clamsproject/app-brandeis-acs-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-brandeis-acs-wrapper/tree/v3)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-brandeis-acs-wrapper/tree/v3" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: 1.11
- Analyzer License: Apache2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://clams.ai/vocabulary/type/AudioDocument/v2](http://clams.ai/vocabulary/type/AudioDocument/v2) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

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
    - _labelset_ = a list of ["speech", "non-speech"]

