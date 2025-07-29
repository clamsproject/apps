---
layout: posts
classes: wide
title: "Parakeet Wrapper (v1.0)"
date: 2025-07-29T14:54:18+00:00
---
## About this version

- Submitter: [shel-ho](https://github.com/shel-ho)
- Submission Time: 2025-07-29T14:54:18+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-parakeet-wrapper:v1.0](https://github.com/clamsproject/app-parakeet-wrapper/pkgs/container/app-parakeet-wrapper/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for NVIDIA NeMo Parakeet ASR models available on huggingface-hub with support for punctuation, capitalization, and word-level timestamping.**

- App ID: [http://apps.clams.ai/parakeet-wrapper/v1.0](http://apps.clams.ai/parakeet-wrapper/v1.0)
- App License: Apache-2.0
- Source Repository: [https://github.com/clamsproject/app-parakeet-wrapper](https://github.com/clamsproject/app-parakeet-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-parakeet-wrapper/tree/v1.0))
- Analyzer Version: 20250714
- Analyzer License: cc-by-4.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



]


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `contextSize`: optional, defaults to `96`

    - Type: integer
    - Multivalued: False


    > Local attention context size for the model. Can be any positive integer, or 0 to set global (full-context) attention. Larger context sizes may improve performance but require a lot more memory. For desktop CUDA device with 12GB VRAM, a context size of around 100 is recommended for full utilization of VRAM. Default is 96
- `modelSize`: optional, defaults to `0.6b`

    - Type: string
    - Multivalued: False
    - Choices: `110m`, **_`0.6b`_**, `1.1b`


    > Parakeet model size to use. Choices: 110m, 0.6b, 1.1b
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

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6)
(of any properties)

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)

- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

