---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v5.1)"
date: 2024-06-27T23:05:21+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-06-27T23:05:21+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v5.1](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v5.1)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits.**

- App ID: [http://apps.clams.ai/swt-detection/v5.1](http://apps.clams.ai/swt-detection/v5.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v5.1))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `startAt`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to start processing
- `stopAt`: optional, defaults to `9223372036854775807`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to stop processing
- `sampleRate`: optional, defaults to `1000`

    - Type: integer
    - Multivalued: False


    > Milliseconds between sampled frames
- `minFrameScore`: optional, defaults to `0.01`

    - Type: number
    - Multivalued: False


    > Minimum score for a still frame to be included in a TimeFrame
- `minTimeframeScore`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > Minimum score for a TimeFrame
- `minFrameCount`: optional, defaults to `2`

    - Type: integer
    - Multivalued: False


    > Minimum number of sampled frames required for a TimeFrame
- `modelName`: optional, defaults to `20240626-205715.convnext_lg`

    - Type: string
    - Multivalued: False
    - Choices: `20240626-205803.convnext_tiny`, **_`20240626-205715.convnext_lg`_**


    > model name to use for classification
- `useStitcher`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the stitcher after classifying the TimePoints
- `allowOverlap`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Allow overlapping time frames
- `map`: optional, defaults to `['B:bars', 'S:slate', 'I:chyron', 'N:chyron', 'Y:chyron', 'C:credits', 'R:credits', 'W:other_opening', 'L:other_opening', 'O:other_opening', 'M:other_opening', 'E:other_text', 'K:other_text', 'G:other_text', 'T:other_text', 'F:other_text']`

    - Type: map
    - Multivalued: True


    > Mapping of a label in the input annotations to a new label. Must be formatted as IN_LABEL:OUT_LABEL (with a colon). To pass multiple mappings, use this parameter multiple times. By default, all the input labels are passed as is, including any negative labels (with default value being no remapping at all). However, when at least one label is remapped, all the other "unset" labels are discarded as a negative label.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/TimePoint/v4](http://mmif.clams.ai/vocabulary/TimePoint/v4)
    - _timeUnit_ = "milliseconds"
    - _labelset_ = a list of ["B", "S", "W", "L", "O", "M", "I", "N", "E", "P", "Y", "K", "G", "T", "F", "C", "R"]

