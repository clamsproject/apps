---
layout: posts
classes: wide
title: "Llava Captioner (v1.0)"
date: 2024-05-23T19:26:17+00:00
---
## About this version

- Submitter: [kelleyl](https://github.com/kelleyl)
- Submission Time: 2024-05-23T19:26:17+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-llava-captioner:v1.0](https://github.com/clamsproject/app-llava-captioner/pkgs/container/app-llava-captioner/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Applies llava to video frames.**

- App ID: [http://apps.clams.ai/llava-captioner/v1.0](http://apps.clams.ai/llava-captioner/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-llava-captioner](https://github.com/clamsproject/app-llava-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-llava-captioner/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) (required)
(of any properties)



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

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

