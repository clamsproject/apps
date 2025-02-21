---
layout: posts
classes: wide
title: "Easyocr Wrapper (v1.0)"
date: 2024-01-25T18:44:59+00:00
---
## About this version

- Submitter: [snewman-aa](https://github.com/snewman-aa)
- Submission Time: 2024-01-25T18:44:59+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-easyocr-wrapper:v1.0](https://github.com/clamsproject/app-easyocr-wrapper/pkgs/container/app-easyocr-wrapper/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Using EasyOCR to extract text from timeframes**

- App ID: [http://apps.clams.ai/easyocr-wrapper/v1.0](http://apps.clams.ai/easyocr-wrapper/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-easyocr-wrapper](https://github.com/clamsproject/app-easyocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-easyocr-wrapper/tree/v1.0))
- Analyzer Version: 1.7.0
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `sampleFrames`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > Number of frames to sample from timeframe
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimePoint/v1](http://mmif.clams.ai/vocabulary/TimePoint/v1)
(of any properties)

