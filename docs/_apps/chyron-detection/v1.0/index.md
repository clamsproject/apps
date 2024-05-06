---
layout: posts
classes: wide
title: "Chyron Detection (v1.0)"
date: 2023-07-24T21:50:08+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-07-24T21:50:08+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-chyron-detection:v1.0](https://github.com/clamsproject/app-chyron-detection/pkgs/container/app-chyron-detection/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This tool detects chyrons, generates time segments.**

- App ID: [http://apps.clams.ai/chyron-detection/v1.0](http://apps.clams.ai/chyron-detection/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-chyron-detection](https://github.com/clamsproject/app-chyron-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-chyron-detection/tree/v1.0))


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


    > unit for output timeframe
- `sampleRatio`: optional, defaults to `5`

    - Type: integer
    - Multivalued: False


    > Frequency to sample frames
- `minFrameCount`: optional, defaults to `10`

    - Type: integer
    - Multivalued: False


    > Minimum number of frames required for a timeframe to be included
- `threshold`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > Threshold from 0-1, lower accepts more potential chyrons
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
        - _frameType_ = "chyron"

