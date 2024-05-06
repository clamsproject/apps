---
layout: posts
classes: wide
title: "Bars Detection (v1.0)"
date: 2023-07-26T00:07:49+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-07-26T00:07:49+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-barsdetection:v1.0](https://github.com/clamsproject/app-barsdetection/pkgs/container/app-barsdetection/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This tool detects SMPTE color bars.**

- App ID: [http://apps.clams.ai/barsdetection/v1.0](http://apps.clams.ai/barsdetection/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-barsdetection](https://github.com/clamsproject/app-barsdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-barsdetection/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)

 (any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `timeUnit`: optional, defaults to `frames`

    - Type: string
    - Multivalued: False
    - Choices: **_`frames`_**, `seconds`, `milliseconds`


    > Unit for output typeframe.
- `sampleRatio`: optional, defaults to `30`

    - Type: integer
    - Multivalued: False


    > Frequency to sample frames.
- `stopAt`: optional, defaults to `9000`

    - Type: integer
    - Multivalued: False


    > Frame number to stop processing.
- `stopAfterOne`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > When True, processing stops after first timeframe is found.
- `minFrameCount`: optional, defaults to `10`

    - Type: integer
    - Multivalued: False


    > minimum number of frames required for a timeframe to be included in the output.
- `threshold`: optional, defaults to `0.7`

    - Type: number
    - Multivalued: False


    > Threshold from 0-1, lower accepts more potential slates.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _typeSpecificProperty_ = a complex object with the following keys:
        - _frameType_ = "bars"

