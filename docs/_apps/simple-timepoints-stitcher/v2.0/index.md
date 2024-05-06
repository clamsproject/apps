---
layout: posts
classes: wide
title: "Simple Timepoints Stitcher (v2.0)"
date: 2024-05-06T16:13:55+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2024-05-06T16:13:55+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-simple-timepoints-stitcher:v2.0](https://github.com/clamsproject/app-simple-timepoints-stitcher/pkgs/container/app-simple-timepoints-stitcher/v2.0)
* Release Notes

    > Major update to add  
    > - experimental CLI. CLI shares the same parameters specified in the app metadata. Try `python cli.py --help`!  
    > - added presets for complex labelMap parameter. Find out about labelMapPreset parameter in the metadata.

## About this app (See raw [metadata.json](metadata.json))

**Stitches a sequence of `TimePoint` annotations into a sequence of `TimeFrame` annotations, performing simple smoothing of short peaks of positive labels.**

* App ID: [http://apps.clams.ai/simple-timepoints-stitcher/v2.0](http://apps.clams.ai/simple-timepoints-stitcher/v2.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-simple-timepoints-stitcher](https://github.com/clamsproject/app-simple-timepoints-stitcher) ([source tree of the submitted version](https://github.com/clamsproject/app-simple-timepoints-stitcher/tree/v2.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1)  (required)
(any properties)
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


]
* [http://mmif.clams.ai/vocabulary/TimePoint/v4](http://mmif.clams.ai/vocabulary/TimePoint/v4)  (required)
    > TimePoint annotations to be stitched. Must be "exhaustive" in that it should cover an entire single time period in the input document, with a uniform sample rate.
    * _timePoint_ = "*"
    * _classification_ = "*"


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|labelMap|mapping of labels in the input annotations to new labels. Must be formatted as "IN_LABEL:OUT_LABEL" (with a colon). To pass multiple mappings, use this parameter multiple times. By default, all the input labels are passed as is, including any "negative" labels (with default value being no remapping at all). However, when at least one label is remapped, all the other "unset" labels are discarded as the negative label("-").|map|Y|[]||
|minTFDuration|minimum duration of a TimeFrame in milliseconds|integer|N|1000||
|minTPScore|minimum score of a TimePoint to be considered as positive|number|N|0.1||
|minTFScore|minimum average score of TimePoints in a TimeFrame to be considered as positive|number|N|0.5||
|labelMapPreset|preset of label mappings. If not `null`, this parameter will override the `labelMap` parameter. Available presets are:<br/>- `null`: `None`<br/>- `swt-v4-4way`: `['B:bars', 'S:slate', 'S-H:slate', 'S-C:slate', 'S-D:slate', 'S-G:slate', 'I:chyron', 'N:chyron', 'Y:chyron', 'C:credit', 'R:credit']`<br/>- `swt-v4-6way`: `['B:bars', 'S:slate', 'S-H:slate', 'S-C:slate', 'S-D:slate', 'S-G:slate', 'I:chyron', 'N:chyron', 'Y:chyron', 'C:credit', 'R:credit', 'E:other_text', 'K:other_text', 'G:other_text', 'T:other_text', 'F:other_text', 'W:other_opening', 'L:other_opening', 'O:other_opening', 'M:other_opening']`|string|N|null|**_`null`_**, `swt-v4-4way`, `swt-v4-6way`|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

* [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) 
    > Stitched TimeFrame annotations. Each TimeFrame annotation represents a continuous segment of timepoints and its `label` property is determined by the `labelMap` parameter (see `parameters` section). The `representatives` is a singleton list of the TimePoint annotation that has the highest score in the TimeFrame.
    * _timeUnit_ = "milliseconds"
    * _label_ = "*"
    * _representatives_ = "*"
