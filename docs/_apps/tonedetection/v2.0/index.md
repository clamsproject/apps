---
layout: posts
classes: wide
title: "Tonedetection (v2.0)"
date: 2025-11-20T08:01:02+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-11-20T08:01:02+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-tonedetection:v2.0](https://github.com/clamsproject/app-tonedetection/pkgs/container/app-tonedetection/v2.0)
- Release Notes

    > What's new  
    > - updated to the latest SDK  
    > - replaced aubio to avoid installation quirks  
    > - removed `timeUnit` and `sampleSize` params  
    > - renamed `lengthThreshold` param to `minToneDuration`

## About this app (See raw [metadata.json](metadata.json))

**Detects spans of monotonic audio within an audio file**

- App ID: [http://apps.clams.ai/tonedetection/v2.0](http://apps.clams.ai/tonedetection/v2.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-tonedetection](https://github.com/clamsproject/app-tonedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-tonedetection/tree/v2.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
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
- `runningTime`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6)
    - _label_ = "tone"

