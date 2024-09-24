---
layout: posts
classes: wide
title: "EAST Text Detection (v1.1)"
date: 2023-07-26T19:06:10+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-07-26T19:06:10+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-east-textdetection:v1.1](https://github.com/clamsproject/app-east-textdetection/pkgs/container/app-east-textdetection/v1.1)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**OpenCV-based text localization app that used EAST text detection model. Please visit the source code repository for full documentation.**

- App ID: [http://apps.clams.ai/east-textdetection/v1.1](http://apps.clams.ai/east-textdetection/v1.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-east-textdetection](https://github.com/clamsproject/app-east-textdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-east-textdetection/tree/v1.1))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/ImageDocument/v1](http://mmif.clams.ai/vocabulary/ImageDocument/v1) (required)
(of any properties)



]
- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `timeUnit`: optional, defaults to `frames`

    - Type: string
    - Multivalued: False
    - Choices: **_`frames`_**, `seconds`, `milliseconds`


    > Unit for time points in the output. Only works with VideoDocument input.
- `frameType`: optional, defaults to `""`

    - Type: string
    - Multivalued: True
    - Choices: ``, `slate`, `chyron`, `rolling-credit`


    > Segments of video to run on. Only works with VideoDocument input and TimeFrame input. Empty value means run on the every frame types.
- `sampleRatio`: optional, defaults to `30`

    - Type: integer
    - Multivalued: False


    > Frequency to sample frames. Only works with VideoDocument input, and without TimeFrame input. (when `TimeFrame` annotation is found, this parameter is ignored.)
- `stopAt`: optional, defaults to `2 * 60 * 60 * 30`

    - Type: integer
    - Multivalued: False


    > Frame number to stop running. Only works with VideoDocument input. The default is roughly 2 hours of video at 30fps.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1)
    - _bboxtype_ = "text"

