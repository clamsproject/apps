---
layout: posts
classes: wide
title: "Slate Detection (v2.1)"
date: 2023-08-03T17:56:59+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-08-03T17:56:59+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-slatedetection:v2.1](https://github.com/clamsproject/app-slatedetection/pkgs/container/app-slatedetection/v2.1)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This tool detects slates.**

- App ID: [http://apps.clams.ai/slatedetection/v2.1](http://apps.clams.ai/slatedetection/v2.1)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-slatedetection](https://github.com/clamsproject/app-slatedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-slatedetection/tree/v2.1))


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


    > Unit of time to use in output.
- `sampleRatio`: optional, defaults to `30`

    - Type: integer
    - Multivalued: False


    > Frequency to sample frames.
- `stopAt`: optional, defaults to `9000`

    - Type: integer
    - Multivalued: False


    > Frame number to stop processing
- `stopAfterOne`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > When True, processing stops after first timeframe is found
- `minFrameCount`: optional, defaults to `10`

    - Type: integer
    - Multivalued: False


    > Minimum number of frames required for a timeframe to be included in the output
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
    - _properties_ = a complex object with the following keys:
        - _frameType_ = "slate"

