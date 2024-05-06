---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v4.2)"
date: 2024-03-11T16:26:00+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-03-11T16:26:00+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v4.2](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v4.2)
- Release Notes

    > Includes bugfix and performance optimization  
    > * fixed bug startAt/stopAt params were not honored  
    > * faster video iteration for still image extraction

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits.**

- App ID: [http://apps.clams.ai/swt-detection/v4.2](http://apps.clams.ai/swt-detection/v4.2)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v4.2))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)

 (any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `startAt`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to start processing
- `stopAt`: optional, defaults to `10000000`

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
- `modelName`: optional, defaults to `20240126-180026.convnext_lg.kfold_000`

    - Type: string
    - Multivalued: False
    - Choices: **_`20240126-180026.convnext_lg.kfold_000`_**, `20240212-132306.convnext_lg.kfold_000`, `20240212-131937.convnext_tiny.kfold_000`


    > model name to use for classification
- `useStitcher`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the stitcher after classifying the TimePoints
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v3](http://mmif.clams.ai/vocabulary/TimeFrame/v3)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/TimePoint/v2](http://mmif.clams.ai/vocabulary/TimePoint/v2)
    - _timeUnit_ = "milliseconds"
    - _labelset_ = a list of ["B", "S", "S:H", "S:C", "S:D", "S:B", "S:G", "W", "L", "O", "M", "I", "N", "E", "P", "Y", "K", "G", "T", "F", "C", "R"]

