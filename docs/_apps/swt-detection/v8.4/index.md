---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v8.4)"
date: 2025-12-14T01:08:09+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-12-14T01:08:09+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v8.4](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v8.4)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits. This app can run in three modes, depending on `useClassifier`, `useStitcher` parameters. When `useClassifier=True`, it runs in the "TimePoint mode" and generates TimePoint annotations. When `useStitcher=True`, it runs in the "TimeFrame mode" and generates TimeFrame annotations based on existing TimePoint annotations -- if no TimePoint is found, it produces an error. By default, it runs in the 'both' mode and first generates TimePoint annotations and then TimeFrame annotations on them.**

- App ID: [http://apps.clams.ai/swt-detection/v8.4](http://apps.clams.ai/swt-detection/v8.4)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v8.4))


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


    > Use the image classifier model to generate TimePoint annotations.
- `tpModelName`: optional, defaults to `convnextv2_tiny`

    - Type: string
    - Multivalued: False
    - Choices: `convnextv2_large`, **_`convnextv2_tiny`_**


    > Model name to use for classification, only applies when `useClassifier=true`.
- `tpModelBatchSize`: optional, defaults to `200`

    - Type: integer
    - Multivalued: False


    > Number of images to process in a batch for classification. Smaller batch sizes will use less memory but may be slower. The default value of 200 is set to be the safely maximum size for "large" model running on desktop-grade GPU (12GB VRAM). Only applies when `useClassifier=true`.
- `tpUsePosModel`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the model trained with positional features, only applies when `useClassifier=true`.
- `tpStartAt`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to start processing, only applies when `useClassifier=true`.
- `tpStopAt`: optional, defaults to `9223372036854775807`

    - Type: integer
    - Multivalued: False


    > Number of milliseconds into the video to stop processing, only applies when `useClassifier=true`.
- `tpSampleRate`: optional, defaults to `1000`

    - Type: integer
    - Multivalued: False


    > Milliseconds between sampled frames, only applies when `useClassifier=true`.
- `useStitcher`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Use the stitcher after classifying the TimePoints.
- `tfMinTPScore`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > Minimum score for a TimePoint to be included in a TimeFrame. A lower value will include more TimePoints in the TimeFrame (increasing recall in exchange for precision). Only applies when `useStitcher=true`.
- `tfMinTFScore`: optional, defaults to `0.9`

    - Type: number
    - Multivalued: False


    > Minimum score for a TimeFrame. A lower value will include more TimeFrames in the output (increasing recall in exchange for precision). Only applies when `useStitcher=true`
- `tfMinTFDuration`: optional, defaults to `5000`

    - Type: integer
    - Multivalued: False


    > Minimum duration of a TimeFrame in milliseconds, only applies when `useStitcher=true`.
- `tfAllowOverlap`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > Allow overlapping time frames, only applies when `useStitcher=true`
- `tfDynamicSceneLabels`: optional, defaults to `['credit', 'credits']`

    - Type: string
    - Multivalued: True


    > Labels that are considered dynamic scenes. For dynamic scenes, TimeFrame annotations contains multiple representative points to follow any changes in the scene. Only applies when `useStitcher=true`
- `tfLabelMap`: optional, defaults to `[]`

    - Type: map
    - Multivalued: True


    > (See also `tfLabelMapPreset`, set `tfLabelMapPreset=nopreset` to make sure that a preset does not override `tfLabelMap` when using this) Mapping of a label in the input TimePoint annotations to a new label of the stitched TimeFrame annotations. Must be formatted as IN_LABEL:OUT_LABEL (with a colon). To pass multiple mappings, use this parameter multiple times. When two+ TP labels are mapped to a TF  label, it essentially works as a "binning" operation. If no mapping is used, all the input labels are passed-through, meaning no change in both TP & TF labelsets. However, when at least one label is mapped, all the other "unset" labels are mapped to the negative label (`-`) and if `-` does not exist in the TF labelset, it is added automatically. Only applies when `useStitcher=true`.
- `tfLabelMapPreset`: optional, defaults to `relaxed`

    - Type: string
    - Multivalued: False
    - Choices: `noprebin`, `nomap`, `strict`, `simpler`, `simple`, **_`relaxed`_**, `binary-bars`, `binary-slate`, `binary-chyron-strict`, `binary-chyron-relaxed`, `binary-credits`, `collapse-close`, `collapse-close-reduce-difficulty`, `collapse-close-bin-lower-thirds`, `ignore-difficulties`, `nopreset`


    > (See also `tfLabelMap`) Preset alias of a label mapping. If not `nopreset`, this parameter will override the `tfLabelMap` parameter. Available presets are:<br/>- `noprebin`: []<br/>- `nomap`: []<br/>- `strict`: ['`B`:`Bars`', '`S`:`Slate`', '`IN`:`Chyron-person`', '`CR`:`Credits`', '`M`:`Main`', '`O`:`Opening`', '`W`:`Opening`', '`Y`:`Chyron-other`', '`KU`:`Chyron-other`', '`L`:`Other-text`', '`G`:`Other-text`', '`F`:`Other-text`', '`E`:`Other-text`', '`T`:`Other-text`', '`P`:`-`', '`-`:`-`']<br/>- `simpler`: ['`B`:`Bars`', '`S`:`Slate`', '`IN`:`Chyron`', '`CR`:`Credits`', '`P`:`Neg`', '`-`:`Neg`']<br/>- `simple`: ['`B`:`Bars`', '`S`:`Slate`', '`IN`:`Chyron-person`', '`CR`:`Credits`', '`Y`:`Other-text`', '`KU`:`Other-text`', '`M`:`Other-text`', '`F`:`Other-text`', '`E`:`Other-text`', '`GLOTW`:`Other-text`', '`P`:`Neg`', '`-`:`Neg`']<br/>- `relaxed`: ['`B`:`Bars`', '`S`:`Slate`', '`Y`:`Chyron`', '`KU`:`Chyron`', '`IN`:`Chyron`', '`CR`:`Credits`', '`M`:`Other-text`', '`F`:`Other-text`', '`E`:`Other-text`', '`GLOTW`:`Other-text`', '`P`:`Neg`', '`-`:`Neg`']<br/>- `binary-bars`: ['`B`:`Bars`']<br/>- `binary-slate`: ['`S`:`Slate`']<br/>- `binary-chyron-strict`: ['`IN`:`Chyron-person`']<br/>- `binary-chyron-relaxed`: ['`Y`:`Chyron`', '`KU`:`Chyron`', '`IN`:`Chyron`']<br/>- `binary-credits`: ['`CR`:`Credits`']<br/><br/> Only applies when `useStitcher=true`.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation
- `runningTime`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v6](http://mmif.clams.ai/vocabulary/TimeFrame/v6)
    - _timeUnit_ = "milliseconds"

- [http://mmif.clams.ai/vocabulary/TimePoint/v5](http://mmif.clams.ai/vocabulary/TimePoint/v5)
    - _timeUnit_ = "milliseconds"
    - _labelset_ = a list of ["B", "CR", "E", "F", "GLOTW", "IN", "KU", "M", "P", "S", "Y"]

