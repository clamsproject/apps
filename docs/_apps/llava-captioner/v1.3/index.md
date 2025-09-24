---
layout: posts
classes: wide
title: "LLaVA Captioner (v1.3)"
date: 2025-09-24T03:48:59+00:00
---
## About this version

- Submitter: [kelleyl](https://github.com/kelleyl)
- Submission Time: 2025-09-24T03:48:59+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-llava-captioner:v1.3](https://github.com/clamsproject/app-llava-captioner/pkgs/container/app-llava-captioner/v1.3)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Applies LLaVA v1.6 Mistral-7B to video frames for image captioning and text transcription.**

- App ID: [http://apps.clams.ai/llava-captioner/v1.3](http://apps.clams.ai/llava-captioner/v1.3)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-llava-captioner](https://github.com/clamsproject/app-llava-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-llava-captioner/tree/v1.3))


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

- `frameInterval`: optional, defaults to `30`

    - Type: integer
    - Multivalued: False


    > The interval at which to extract frames from the video if there are no timeframe annotations. Default is every 30 frames.
- `defaultPrompt`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > default prompt to use for timeframes not specified in the promptMap. If set to `-`, timeframes not specified in the promptMap will be skipped.
- `promptMap`: optional, defaults to `[]`

    - Type: map
    - Multivalued: True


    > Mapping of labels of the input timeframe annotations to new prompts. Must be formatted as "IN_LABEL:PROMPT" (with a colon). To pass multiple mappings, use this parameter multiple times. By default, any timeframe labels not mapped to a prompt will be used with the default prompt. In order to skip timeframes with a particular label, pass `-` as the prompt value. In order to skip all timeframes not specified in the promptMap, set the defaultPrompt parameter to `-`
- `config`: optional, defaults to `config/fixed_window.yaml`

    - Type: string
    - Multivalued: False


    > Name of the configuration file to use. Configuration files can specify custom prompts, input context settings, and other processing parameters.
- `batch_size`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > Number of images to process in a single batch. Default is 1. Higher values may improve throughput but require more memory.
- `num_beams`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > Number of beams for beam search during text generation. Default is 1. Higher values may improve quality but increase generation time.
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

