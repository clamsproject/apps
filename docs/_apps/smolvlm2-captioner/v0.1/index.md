---
layout: posts
classes: wide
title: "SmolVLM2 Captioner (v0.1)"
date: 2025-11-20T14:50:10+00:00
---
## About this version

- Submitter: [kelleyl](https://github.com/kelleyl)
- Submission Time: 2025-11-20T14:50:10+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-smolvlm2-captioner:v0.1](https://github.com/clamsproject/app-smolvlm2-captioner/pkgs/container/app-smolvlm2-captioner/v0.1)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Applies SmolVLM2-2.2B-Instruct multimodal model to video frames for image captioning.**

- App ID: [http://apps.clams.ai/smolvlm2-captioner/v0.1](http://apps.clams.ai/smolvlm2-captioner/v0.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-smolvlm2-captioner](https://github.com/clamsproject/app-smolvlm2-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-smolvlm2-captioner/tree/v0.1))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/ImageDocument/v1](http://mmif.clams.ai/vocabulary/ImageDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `frameInterval`: optional, defaults to `30`

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
- `config`: optional, defaults to `config/default.yaml`

    - Type: string
    - Multivalued: False


    > Name of the config file to use.
- `num_beams`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > Number of beams for beam search during text generation. Default is 1. Higher values may improve quality but increase generation time.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation
- `runningTime`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

