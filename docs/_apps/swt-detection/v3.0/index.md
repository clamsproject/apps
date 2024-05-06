---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v3.0)"
date: 2024-02-07T21:18:36+00:00
---
## About this version

- Submitter: [marcverhagen](https://github.com/marcverhagen)
- Submission Time: 2024-02-07T21:18:36+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v3.0](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v3.0)
- Release Notes

    > New model, improved MMIF output and various fixes

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits.**

- App ID: [http://apps.clams.ai/swt-detection/v3.0](http://apps.clams.ai/swt-detection/v3.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v3.0))


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
- `minTimeframeScore`: optional, defaults to `0.25`

    - Type: number
    - Multivalued: False


    > Minimum score for a TimeFrame
- `minFrameCount`: optional, defaults to `2`

    - Type: integer
    - Multivalued: False


    > Minimum number of sampled frames required for a TimeFrame
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _timeUnit_ = "milliseconds"
    - _frameType_ = "bars"

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _timeUnit_ = "milliseconds"
    - _frameType_ = "slate"

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _timeUnit_ = "milliseconds"
    - _frameType_ = "chyron"

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _timeUnit_ = "milliseconds"
    - _frameType_ = "credits"

- [http://mmif.clams.ai/vocabulary/TimePoint/v1](http://mmif.clams.ai/vocabulary/TimePoint/v1)
    - _timeUnit_ = "milliseconds"

