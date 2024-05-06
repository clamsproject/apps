---
layout: posts
classes: wide
title: "Tone_Detector (v1.0)"
date: 2023-07-24T17:50:36+00:00
---
## About this version

- Submitter: [MrSqually](https://github.com/MrSqually)
- Submission Time: 2023-07-24T17:50:36+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-tonedetection:v1.0](https://github.com/clamsproject/app-tonedetection/pkgs/container/app-tonedetection/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Detects spans of monotonic audio within an audio file**

- App ID: [http://apps.clams.ai/tonedetection/v1.0](http://apps.clams.ai/tonedetection/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-tonedetection](https://github.com/clamsproject/app-tonedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-tonedetection/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)

 (any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `timeUnit`: optional, defaults to `seconds`

    - Type: string
    - Multivalued: False
    - Choices: **_`seconds`_**, **_`seconds`_**, `milliseconds`


    > the unit for annotation output
- `lengthThreshold`: optional, defaults to `2000`

    - Type: integer
    - Multivalued: False


    > minimum length threshold (in ms)
- `sampleSize`: optional, defaults to `512`

    - Type: integer
    - Multivalued: False


    > length for each segment of samples to be compared
- `stopAt`: optional, defaults to `None`

    - Type: integer
    - Multivalued: False


    > stop point for audio processing (in ms). Defaults to the length of the file
- `tolerance`: optional, defaults to `1.0`

    - Type: number
    - Multivalued: False


    > threshold value for a "match" within audio processing
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _frameType_ = "tone"

