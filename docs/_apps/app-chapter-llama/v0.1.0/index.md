---
layout: posts
classes: wide
title: "Chapter-Llama (v0.1.0)"
date: 2026-06-09T01:47:25+00:00
---
## About this version

- Submitter: [bohJiang12](https://github.com/bohJiang12)
- Submission Time: 2026-06-09T01:47:25+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-chapter-llama:v0.1.0](https://github.com/clamsproject/app-chapter-llama/pkgs/container/app-chapter-llama/v0.1.0)
- Release Notes

    > release v0.1.0

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Chapter-Llama, a video chaptering system that uses LLMs (Llama-3.1-8B-Instruct with LoRA adapters) to partition long videos into chapters with timestamps and titles. It processes speech transcripts (ASR) as text input to the LLM.**

- App ID: [http://apps.clams.ai/app-chapter-llama/v0.1.0](http://apps.clams.ai/app-chapter-llama/v0.1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-chapter-llama](https://github.com/clamsproject/app-chapter-llama) ([source tree of the submitted version](https://github.com/clamsproject/app-chapter-llama/tree/v0.1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)



]


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `model`: optional, defaults to `asr-10k`

    - Type: string
    - Multivalued: False
    - Choices: **_`asr-10k`_**, `asr-1k`, `captions_asr-10k`, `captions_asr-1k`


    > Chapter-Llama LoRA model variant to use.
- `windowTokenSize`: optional, defaults to `15000`

    - Type: integer
    - Multivalued: False


    > Token size for each processing window. Longer videos are split into windows of this size.
- `firstWindowOnly`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > Process only the first window (for debugging).
- `quantization`: optional, defaults to `4bit`

    - Type: string
    - Multivalued: False
    - Choices: **_`4bit`_**, `8bit`, `none`


    > Quantization method to reduce GPU memory usage. '4bit' reduces ~75%, '8bit' reduces ~50%, 'none' uses full precision.
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

- [http://mmif.clams.ai/vocabulary/Chapter/v6](http://mmif.clams.ai/vocabulary/Chapter/v6)
    - _timeUnit_ = "milliseconds"

