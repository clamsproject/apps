---
layout: posts
classes: wide
title: "Few Shot Classifier (v1.0)"
date: 2023-08-01T22:57:12+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-08-01T22:57:12+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-fewshotclassifier:v1.0](https://github.com/clamsproject/app-fewshotclassifier/pkgs/container/app-fewshotclassifier/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This tool uses a vision model to classify video segments. Currenly supports "chyron" frame type.**

- App ID: [http://apps.clams.ai/fewshotclassifier/v1.0](http://apps.clams.ai/fewshotclassifier/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-fewshotclassifier](https://github.com/clamsproject/app-fewshotclassifier) ([source tree of the submitted version](https://github.com/clamsproject/app-fewshotclassifier/tree/v1.0))
- Analyzer Version: 1.0
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `timeUnit`: optional, defaults to `frames`

    - Type: string
    - Multivalued: False
    - Choices: **_`frames`_**, `milliseconds`


    > Unit for output timeframe
- `sampleRatio`: optional, defaults to `30`

    - Type: integer
    - Multivalued: False


    > Frequency to sample frames.
- `minFrameCount`: optional, defaults to `60`

    - Type: integer
    - Multivalued: False


    > Minimum number of frames required for a timeframe to be included in the output with a minimum value of 1
- `threshold`: optional, defaults to `0.8`

    - Type: number
    - Multivalued: False


    > Threshold from 0-1, lower accepts more potential labels.
- `finetunedFrameType`: optional, defaults to `chyron`

    - Type: string
    - Multivalued: False


    > Name of fine-tuned model to use. All pre-installed models are named after the frame type they were fine-tuned for.<br/><br/>If an empty value is passed, the app will look for fewshots.csv file in the same directory as the app.py and create a new fine-tuned model based on the examples in that file.<br/><br/>At the moment, a model fine-tuned on "chyron" frame type is shipped as pre-installed.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _frameType_ = "string"

