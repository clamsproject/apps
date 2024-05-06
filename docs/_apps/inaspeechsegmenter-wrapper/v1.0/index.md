---
layout: posts
classes: wide
title: "inaSpeechSegmenter Wrapper (v1.0)"
date: 2023-06-20T02:49:35+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-06-20T02:49:35+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-inaspeechsegmenter-wrapper:v1.0](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/pkgs/container/app-inaspeechsegmenter-wrapper/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**inaSpeechSegmenter is a CNN-based audio segmentation toolkit. The original software can be found at https://github.com/ina-foss/inaSpeechSegmenter .**

- App ID: [http://apps.clams.ai/inaspeechsegmenter-wrapper/v1.0](http://apps.clams.ai/inaspeechsegmenter-wrapper/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-inaspeechsegmenter-wrapper](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v1.0))
- Analyzer Version: 0.7.6
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)

 (any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)

 (any properties)



]


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _timeunit_ = "milliseconds"

