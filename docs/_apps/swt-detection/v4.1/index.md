---
layout: posts
classes: wide
title: "Scenes-with-text Detection (v4.1)"
date: 2024-03-07T03:29:41+00:00
---
## About this version

* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2024-03-07T03:29:41+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-swt-detection:v4.1](https://github.com/clamsproject/app-swt-detection/pkgs/container/app-swt-detection/v4.1)
* Release Notes

    > This version includes many bugfixes and clarification for the previous version.  
    > * more informative, consistent, and flask-friendly debug-level logging for future development  
    > * two additional pretrained models, including one based on convnext_tiny backbone for quicker annotation  
    > * `TimePoint` annotations is re-worked  
    >     * classification-related props in TP anns are now all based on the "RAW" labels from classifier  
    >     * all images classification results are now recorded as TP annotations regardless of TF annotations  
    > * added two runtime parameter  
    >     * `useStitcher` - when `"false"`, app will only generate `TimePoint` annotations, not stitching them into `TimeFrame` annotations  
    >     * `modelName` - to pick a model between pre-built classifiers (by default, app will use the best performing model from training experiments)  
    > * updated to the latest `mmif-python` and `clams-python`, and thus no longer generates MMIFs with a non-existing version

## About this app (See raw [metadata.json](metadata.json))

**Detects scenes with text, like slates, chyrons and credits.**

* App ID: [http://apps.clams.ai/swt-detection/v4.1](http://apps.clams.ai/swt-detection/v4.1)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-swt-detection](https://github.com/clamsproject/app-swt-detection) ([source tree of the submitted version](https://github.com/clamsproject/app-swt-detection/tree/v4.1))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1)  (required)
(any properties)


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|startAt|Number of milliseconds into the video to start processing|integer|N|0||
|stopAt|Number of milliseconds into the video to stop processing|integer|N|10000000||
|sampleRate|Milliseconds between sampled frames|integer|N|1000||
|minFrameScore|Minimum score for a still frame to be included in a TimeFrame|number|N|0.01||
|minTimeframeScore|Minimum score for a TimeFrame|number|N|0.5||
|minFrameCount|Minimum number of sampled frames required for a TimeFrame|integer|N|2||
|modelName|model name to use for classification|string|N|20240126-180026.convnext_lg.kfold_000|**_`20240126-180026.convnext_lg.kfold_000`_**, `20240212-132306.convnext_lg.kfold_000`, `20240212-131937.convnext_tiny.kfold_000`|
|useStitcher|Use the stitcher after classifying the TimePoints|boolean|N|true|`false`, **_`true`_**|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

* [http://mmif.clams.ai/vocabulary/TimeFrame/v3](http://mmif.clams.ai/vocabulary/TimeFrame/v3) 
    * _timeUnit_ = "milliseconds"
* [http://mmif.clams.ai/vocabulary/TimePoint/v2](http://mmif.clams.ai/vocabulary/TimePoint/v2) 
    * _timeUnit_ = "milliseconds"
    * _labelset_ = a list of ["B", "S", "S:H", "S:C", "S:D", "S:B", "S:G", "W", "L", "O", "M", "I", "N", "E", "P", "Y", "K", "G", "T", "F", "C", "R"]
