---
layout: posts
classes: wide
title: "Simple Timepoints Stitcher (v1.3)"
date: 2024-04-21T22:40:34+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-04-21T22:40:34+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-simple-timepoints-stitcher:v1.3](https://github.com/clamsproject/app-simple-timepoints-stitcher/pkgs/container/app-simple-timepoints-stitcher/v1.3)
- Release Notes

    > fixed `label` property missing from `TimeFrame`, updated to the new SDK version

## About this app (See raw [metadata.json](metadata.json))

**Stitches a sequence of `TimePoint` annotations into a sequence of `TimeFrame` annotations, performing simple smoothing of short peaks of positive labels.**

- App ID: [http://apps.clams.ai/simple-timepoints-stitcher/v1.3](http://apps.clams.ai/simple-timepoints-stitcher/v1.3)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-simple-timepoints-stitcher](https://github.com/clamsproject/app-simple-timepoints-stitcher) ([source tree of the submitted version](https://github.com/clamsproject/app-simple-timepoints-stitcher/tree/v1.3))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



]
- [http://mmif.clams.ai/vocabulary/TimePoint/v4](http://mmif.clams.ai/vocabulary/TimePoint/v4) (required)
    - _timePoint_ = "*"
    - _classification_ = "*"

    > TimePoint annotations to be stitched. Must be "exhaustive" in that it should cover an entire single time period in the input document, with a uniform sample rate.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `labelMap`: optional, defaults to `[]`

    - Type: map
    - Multivalued: True


    > mapping of labels in the input annotations to new labels. Must be formatted as "IN_LABEL:OUT_LABEL" (with a colon). To pass multiple mappings, use this parameter multiple times. By default, all the input labels are passed as is, including any "negative" labels (with default value being no remapping at all). However, when at least one label is remapped, all the other "unset" labels are discarded asa negative label("-").
- `minTFDuration`: optional, defaults to `1000`

    - Type: integer
    - Multivalued: False


    > minimum duration of a TimeFrame in milliseconds
- `minTPScore`: optional, defaults to `0.1`

    - Type: number
    - Multivalued: False


    > minimum score of a TimePoint to be considered as positive
- `minTFScore`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > minimum average score of TimePoints in a TimeFrame to be considered as positive
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
    - _label_ = "*"
    - _representatives_ = "*"

    > Stitched TimeFrame annotations. Each TimeFrame annotation represents a continuous segment of timepoints and its `label` property is determined by the `labelMap` parameter (see `parameters` section). The `representatives` is a singleton list of the TimePoint annotation that has the highest score in the TimeFrame.
