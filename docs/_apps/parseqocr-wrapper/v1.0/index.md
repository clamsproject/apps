---
layout: posts
classes: wide
title: "Parseq OCR Wrapper (v1.0)"
date: 2023-07-26T00:04:08+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-07-26T00:04:08+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-parseqocr-wrapper:v1.0](https://github.com/clamsproject/app-parseqocr-wrapper/pkgs/container/app-parseqocr-wrapper/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This tool applies Parseq OCR to a video or image and generates text boxes and OCR results.**

- App ID: [http://apps.clams.ai/parseqocr-wrapper/v1.0](http://apps.clams.ai/parseqocr-wrapper/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-parseqocr-wrapper](https://github.com/clamsproject/app-parseqocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-parseqocr-wrapper/tree/v1.0))
- Analyzer Version: bc8d95cd
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) (required)
    - _boxType_ = "text"



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

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

