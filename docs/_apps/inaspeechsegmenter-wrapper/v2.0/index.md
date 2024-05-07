---
layout: posts
classes: wide
title: "inaSpeechSegmenter Wrapper (v2.0)"
date: 2024-05-07T03:45:14+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-05-07T03:45:14+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-inaspeechsegmenter-wrapper:v2.0](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/pkgs/container/app-inaspeechsegmenter-wrapper/v2.0)
- Release Notes

    > Major update  
    > - `TimeFrame` properties are updated to match new CLAMS vocab specification  
    > - `noEnergy` label from INA segmenter is stored as `silence` in MMIF for clarity  
    > - added parameter `silenceRatio` to configure silence detection threshold  
    > - renamed `minDuration` parameter to `minTFDuration` for clarity  
    > - bugfixes in cli.py

## About this app (See raw [metadata.json](metadata.json))

**inaSpeechSegmenter is a CNN-based audio segmentation toolkit. The original software can be found at https://github.com/ina-foss/inaSpeechSegmenter .**

- App ID: [http://apps.clams.ai/inaspeechsegmenter-wrapper/v2.0](http://apps.clams.ai/inaspeechsegmenter-wrapper/v2.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-inaspeechsegmenter-wrapper](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v2.0))
- Analyzer Version: 0.7.6
- Analyzer License: MIT


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

- `minTFDuration`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > minimum duration of a TimeFrame in milliseconds
- `silenceRatio`: optional, defaults to `3`

    - Type: integer
    - Multivalued: False


    > percentage ratio (0-100) of audio energy to to determine silence, ratio to mean every of the input audio.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)
    - _timeunit_ = "milliseconds"
    - _labelset_ = a list of ["silence", "speech", "noise", "music"]

    > The INA semgmenter uses 5-way classification (['noEnergy', 'female', 'male', 'noise', 'music']) and this wrapper remaps the labels to ['silence', 'speech', 'noise', 'music'], by 1) renaming `noEnergy` to `silence` 2) collapsing `female` and `male` into `speech` (leaving additional `gender` property). Note that the time frame annotations do not exhaustively cover the input audio, but only the segments.
