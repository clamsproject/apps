---
layout: posts
classes: wide
title: "Simple Timepoints Stitcher (v3.0)"
date: 2024-08-06T12:25:05+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-08-06T12:25:05+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-simple-timepoints-stitcher:v3.0](https://github.com/clamsproject/app-simple-timepoints-stitcher/pkgs/container/app-simple-timepoints-stitcher/v3.0)
- Release Notes

    > Now can filter overlapping time frames  
    > - via `allowOverlap` parameter (default is true to keep the backward compatibility)  
    > - the filtering algorithm (based on https://github.com/clamsproject/app-swt-detection/blob/5092274d1ead64f21e0e3c2bbb7aa3ad4db75cd4/modeling/stitch.py#L88-L104)  
    >     - sort collected positive TP sequences based on their mean scores, regardless of the labels  
    >     - loop through the sorted seqs, if a seq in the loop does not include any "seen" TP, mark the seq as "final" and mark all the underlying TPs as "seen", otherwise skip that one.  
    >     - return the "final" frames, re-sorted by the start TPs

## About this app (See raw [metadata.json](metadata.json))

**Stitches a sequence of `TimePoint` annotations into a sequence of `TimeFrame` annotations, performing simple smoothing of short peaks of positive labels.**

- App ID: [http://apps.clams.ai/simple-timepoints-stitcher/v3.0](http://apps.clams.ai/simple-timepoints-stitcher/v3.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-simple-timepoints-stitcher](https://github.com/clamsproject/app-simple-timepoints-stitcher) ([source tree of the submitted version](https://github.com/clamsproject/app-simple-timepoints-stitcher/tree/v3.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)



]
- [http://mmif.clams.ai/vocabulary/TimePoint/v4](http://mmif.clams.ai/vocabulary/TimePoint/v4) (required)
    - _timePoint_ = "*"
    - _classification_ = "*"

    > TimePoint annotations to be stitched. Must be "exhaustive" in that it should cover an entire single time period in the input document, with a uniform sample rate.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `labelMap`: optional, defaults to `[]`

    - Type: map
    - Multivalued: True


    > mapping of labels in the input annotations to new labels. Must be formatted as "IN_LABEL:OUT_LABEL" (with a colon). To pass multiple mappings, use this parameter multiple times. By default, all the input labels are passed as is, including any "negative" labels (with default value being no remapping at all). However, when at least one label is remapped, all the other "unset" labels are discarded as the negative label("-").
- `minTFDuration`: optional, defaults to `1000`

    - Type: integer
    - Multivalued: False


    > minimum duration of a TimeFrame in milliseconds
- `minTPScore`: optional, defaults to `0.1`

    - Type: number
    - Multivalued: False


    > minimum score of a TimePoint to be considered as positive
- `minTFScore`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > minimum average score of TimePoints in a TimeFrame to be considered as positive
- `labelMapPreset`: optional, defaults to `null`

    - Type: string
    - Multivalued: False
    - Choices: **_`null`_**, `swt-v4-4way`, `swt-v4-6way`


    > preset of label mappings. If not `null`, this parameter will override the `labelMap` parameter. Available presets are:<br/>- `null`: `None`<br/>- `swt-v4-4way`: `['B:bars', 'S:slate', 'I:chyron', 'N:chyron', 'Y:chyron', 'C:credits', 'R:credits']`<br/>- `swt-v4-6way`: `['B:bars', 'S:slate', 'I:chyron', 'N:chyron', 'Y:chyron', 'C:credits', 'R:credits', 'E:other_text', 'K:other_text', 'G:other_text', 'T:other_text', 'F:other_text', 'W:other_opening', 'L:other_opening', 'O:other_opening', 'M:other_opening']`
- `allowOverlap`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > Allow overlapping time frames
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
    - _label_ = "*"
    - _representatives_ = "*"

    > Stitched TimeFrame annotations. Each TimeFrame annotation represents a continuous segment of timepoints and its `label` property is determined by the `labelMap` parameter (see `parameters` section). The `representatives` is a singleton list of the TimePoint annotation that has the highest score in the TimeFrame.
