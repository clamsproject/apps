---
layout: posts
classes: wide
title: "Llava Captioner (v1.1)"
date: 2024-05-23T19:38:32+00:00
---
## About this version

- Submitter: [kelleyl](https://github.com/kelleyl)
- Submission Time: 2024-05-23T19:38:32+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-llava-captioner:v1.1](https://github.com/clamsproject/app-llava-captioner/pkgs/container/app-llava-captioner/v1.1)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Applies llava to video frames.**

- App ID: [http://apps.clams.ai/llava-captioner/v1.1](http://apps.clams.ai/llava-captioner/v1.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-llava-captioner](https://github.com/clamsproject/app-llava-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-llava-captioner/tree/v1.1))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `defaultPrompt`: optional, defaults to `What is shown in this video frame?`

    - Type: string
    - Multivalued: False


    > default prompt to use for timeframes not specified in the promptMap. If set to `-`, timeframes not specified in the promptMap will be skipped.
- `promptMap`: optional, defaults to `[]`

    - Type: map
    - Multivalued: True


    > mapping of labels of the input timeframe annotations to new prompts. Must be formatted as "IN_LABEL:PROMPT" (with a colon). To pass multiple mappings, use this parameter multiple times. By default, any timeframe labels not mapped to a prompt will be used with the defaultprompt. In order to skip timeframes with a particular label, pass `-` as the prompt value.in order to skip all timeframes not specified in the promptMap, set the defaultPromptparameter to `-`
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

