---
layout: posts
classes: wide
title: "Gentle Forced Aligner Wrapper (v1.0)"
date: 2023-07-24T20:01:10+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-07-24T20:01:10+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-gentle-forced-aligner-wrapper:v1.0](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/pkgs/container/app-gentle-forced-aligner-wrapper/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**This CLAMS app aligns transcript and audio track using Gentle. Gentle is a robust yet lenient forced aligner built on Kaldi.This app only works when Gentle is already installed locally.Unfortunately, Gentle is not distributed as a Python package distribution.To get Gentle installation instruction, see https://lowerquality.com/gentle/ Make sure install Gentle from the git commit specified in ``analyzer_version`` in this metadata.**

- App ID: [http://apps.clams.ai/gentle-forced-aligner-wrapper/v1.0](http://apps.clams.ai/gentle-forced-aligner-wrapper/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-gentle-forced-aligner-wrapper](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/tree/v1.0))
- Analyzer Version: f29245a
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)

 (any properties)

- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)

 (any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _frameType_ = "speech"

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)

 (any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `use_speech_segmentation`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > When set true, use exising "speech"-typed ``TimeFrame`` annotations and run aligner only on those frames, instead of entire audio files.
- `use_tokenization`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > When set true, ``Alignment`` annotation output will honor existing latest tokenization (``Token`` annotations). Due to a limitation of the way Kaldi reads in English tokens, existing tokens must not contain whitespaces. 
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)

 (any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1)
    - _frameType_ = "speech"
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)

 (any properties)

