---
layout: posts
classes: wide
title: "EAST Text Detection (v1.2)"
date: 2024-06-24T13:52:29+00:00
---
## About this version

- Submitter: [MrSqually](https://github.com/MrSqually)
- Submission Time: 2024-06-24T13:52:29+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-east-textdetection:v1.2](https://github.com/clamsproject/app-east-textdetection/pkgs/container/app-east-textdetection/v1.2)
- Release Notes

    > SDK v1.2.4 update

## About this app (See raw [metadata.json](metadata.json))

**OpenCV-based text localization app that used EAST text detection model. Please visit the source code repository for full documentation.**

- App ID: [http://apps.clams.ai/east-textdetection/v1.2](http://apps.clams.ai/east-textdetection/v1.2)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-east-textdetection](https://github.com/clamsproject/app-east-textdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-east-textdetection/tree/v1.2))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/ImageDocument/v1](http://mmif.clams.ai/vocabulary/ImageDocument/v1) (required)
(of any properties)



]
- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `timeUnit`: optional, defaults to `frames`

    - Type: string
    - Multivalued: False
    - Choices: **_`frames`_**, `seconds`, `milliseconds`


    > Unit for time points in the output. Only works with VideoDocument input.
- `frameType`: optional, defaults to `['']`

    - Type: string
    - Multivalued: True
    - Choices: ``, `slate`, `chyron`, `rolling-credit`


    > Segments of video to run on. Only works with VideoDocument input and TimeFrame input. Empty value means run on the every frame types.
- `sampleRate`: optional, defaults to `30`

    - Type: integer
    - Multivalued: False


    > Frequency to sample frames. Only works with VideoDocument input, and without TimeFrame input. (when `TimeFrame` annotation is found, this parameter is ignored.)
- `stopAt`: optional, defaults to `216000`

    - Type: integer
    - Multivalued: False


    > Frame number to stop running. Only works with VideoDocument input. The default is roughly 2 hours of video at 30fps.
- `mergeBoxes`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > if True, creates a single merged bounding box from all detected boxes.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/BoundingBox/v4](http://mmif.clams.ai/vocabulary/BoundingBox/v4)
    - _bboxtype_ = "text"

