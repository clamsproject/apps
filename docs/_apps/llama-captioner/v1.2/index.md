---
layout: posts
classes: wide
title: "Llama Captioner (v1.2)"
date: 2025-01-23T15:43:59+00:00
---
## About this version

- Submitter: [kelleyl](https://github.com/kelleyl)
- Submission Time: 2025-01-23T15:43:59+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-llava-captioner:v1.2](https://github.com/clamsproject/app-llama-captioner/pkgs/container/app-llama-captioner/v1.2)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Applies LLaMA 3.2 to video frames.**

- App ID: [http://apps.clams.ai/llama-captioner/v1.2](http://apps.clams.ai/llama-captioner/v1.2)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-llama-captioner](https://github.com/clamsproject/app-llama-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-llama-captioner/tree/v1.2))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/ImageDocument/v1](http://mmif.clams.ai/vocabulary/ImageDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `frameInterval`: optional, defaults to `300`

    - Type: integer
    - Multivalued: False


    > The interval at which to extract frames from the video if there are no timeframe annotations. Default is every 30 frames.
- `defaultPrompt`: optional, defaults to `Describe what is shown in this video frame. Analyze the purpose of this frame in the context of a news video. Transcribe any text present.`

    - Type: string
    - Multivalued: False


    > default prompt to use for timeframes not specified in the promptMap. If set to `-`, timeframes not specified in the promptMap will be skipped.
- `promptMap`: optional, defaults to `[]`

    - Type: map
    - Multivalued: True


    > mapping of labels of the input timeframe annotations to new prompts. Must be formatted as "IN_LABEL:PROMPT" (with a colon). To pass multiple mappings, use this parameter multiple times. By default, any timeframe labels not mapped to a prompt will be used with the defaultprompt. In order to skip timeframes with a particular label, pass `-` as the prompt value.in order to skip all timeframes not specified in the promptMap, set the defaultPromptparameter to `-`
- `modelVersion`: optional, defaults to `3.2`

    - Type: string
    - Multivalued: False


    > Version of the LLaMA model to use.
- `config`: optional, defaults to `config/default.yaml`

    - Type: string
    - Multivalued: False


    > Name of the config file to use.
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

