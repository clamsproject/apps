---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v7.0)"
date: 2024-11-03T03:41:54+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-11-03T03:41:54+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v7.0](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v7.0)
- Release Notes

    > This version re-implements stitcher based on `simple-timepoints-stitcher`  
    > - app now can run stitch-only mode (`useClassifier` and `useStitcher`)  
    >     - simple-timepoints-stitcher app will retire  
    > - prefixed all parameters with their corresponding modes (e.g., `sampleRat  
    > e` > `tpSampleRate`, `minTPScore` > `tfMinTPScore`  
    > - changes to parameters  
    >     - `minTFCount` (frame count-based) became `tfMinTFDuration` (time-based)  
    >     - `map` became `tfLabelMap` to clarify what "map" the param sets  
    >     - `tfDynamicSceneLabels` is added to configure dynamic scene types that need multiple representative images/timepoints (defaults to [`credit`, ` credits`])  
    >     - default values for stitcher parameters are changed based on recent experiments. Most significantly now `minTPScore` defaults to 0.5 and `minTFScore` defaults to 0.9. See https://github.com/clamsproject/aapb-evaluations/issues/60 to read the full experimental reports.  
    > - changes to app behavior  
    >     - new stitcher implementation is not exactly the same as the old, and users should expect more "break-ups" in the middle of long time frames  
    >     - for dynamic scene types, the gap between representative time points is now twice the `tfMinTFDuration` value  
    >     - image classification is now done in batches (currently fixed to size 2000) to reduce memory usage. This will add some time overhead to image extraction process

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits. This app can run in three modes, depending on `useClassifier`, `useStitcher` parameters. When `useClassifier=True`, it runs in the "TimePoint mode" and generates TimePoint annotations. When `useStitcher=True`, it runs in the "TimeFrame mode" and generates TimeFrame annotations based on existing TimePoint annotations -- if no TimePoint is found, it produces an error. By default, it runs in the 'both' mode and first generates TimePoint annotations and then TimeFrame annotations on them.**

- App ID: [http://apps.clams.ai/swt-detection/v7.0](http://apps.clams.ai/swt-detection/v7.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v7.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `useClassifier`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the image classifier model to generate TimePoint annotations
- `tpModelName`: optional, defaults to `convnext_lg`

    - Type: string
    - Multivalued: False
    - Choices: **_`convnext_lg`_**, `convnext_tiny`


    > model name to use for classification, only applies when `useClassifier=true`
- `tpUsePosModel`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the model trained with positional features, only applies when `useClassifier=true`
- `tpStartAt`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to start processing, only applies when `useClassifier=true`
- `tpStopAt`: optional, defaults to `9223372036854775807`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to stop processing, only applies when `useClassifier=true`
- `tpSampleRate`: optional, defaults to `1000`

    - Type: integer
    - Multivalued: False


    > Milliseconds between sampled frames, only applies when `useClassifier=true`
- `useStitcher`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the stitcher after classifying the TimePoints
- `tfMinTPScore`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > Minimum score for a TimePoint to be included in a TimeFrame, only applies when `useStitcher=true`
- `tfMinTFScore`: optional, defaults to `0.9`

    - Type: number
    - Multivalued: False


    > Minimum score for a TimeFrame, only applies when `useStitcher=true`
- `tfMinTFDuration`: optional, defaults to `5000`

    - Type: integer
    - Multivalued: False


    > Minimum duration of a TimeFrame in milliseconds, only applies when `useStitcher=true`
- `tfAllowOverlap`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > Allow overlapping time frames, only applies when `useStitcher=true`
- `tfDynamicSceneLabels`: optional, defaults to `['credit', 'credits']`

    - Type: string
    - Multivalued: True


    > Labels that are considered dynamic scenes. For dynamic scenes, TimeFrame annotations contains multiple representative points to follow any changes in the scene. Only applies when `useStitcher=true`
- `tfLabelMap`: optional, defaults to `['B:bars', 'S:slate', 'I:chyron', 'N:chyron', 'Y:chyron', 'C:credits', 'R:credits', 'W:other_opening', 'L:other_opening', 'O:other_opening', 'M:other_opening', 'E:other_text', 'K:other_text', 'G:other_text', 'T:other_text', 'F:other_text']`

    - Type: map
    - Multivalued: True


    > Mapping of a label in the input annotations to a new label. Must be formatted as IN_LABEL:OUT_LABEL (with a colon). To pass multiple mappings, use this parameter multiple times. By default, all the input labels are passed as is, including any negative labels (with default value being no remapping at all). However, when at least one label is remapped, all the other "unset" labels are discarded as a negative label. Only applies when `useStitcher=true`
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

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/TimePoint/v4](http://mmif.clams.ai/vocabulary/TimePoint/v4)
    - _timeUnit_ = "milliseconds"
    - _labelset_ = a list of ["B", "S", "W", "L", "O", "M", "I", "N", "E", "P", "Y", "K", "G", "T", "F", "C", "R"]

