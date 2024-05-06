---
layout: posts
classes: wide
title: "Pyscenedetect Wrapper (v3)"
date: 2024-03-11T17:42:55+00:00
---
## About this version

- Submitter: [kelleyl](https://github.com/kelleyl)
- Submission Time: 2024-03-11T17:42:55+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-pyscenedetect-wrapper:v3](https://github.com/clamsproject/app-pyscenedetect-wrapper/pkgs/container/app-pyscenedetect-wrapper/v3)
- Release Notes

    > sdk version updates

## About this app (See raw [metadata.json](metadata.json))

**CLAMS app wraps PySceneDetect and performs shot boundary detection on input videos**

- App ID: [http://apps.clams.ai/pyscenedetect-wrapper/v3](http://apps.clams.ai/pyscenedetect-wrapper/v3)
- App License: Apache2
- Source Repository: [https://github.com/clamsproject/app-pyscenedetect-wrapper](https://github.com/clamsproject/app-pyscenedetect-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-pyscenedetect-wrapper/tree/v3))
- Analyzer Version: 0.6.1
- Analyzer License: BSD-3


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)

 (any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `mode`: optional, defaults to `content`

    - Type: string
    - Multivalued: False
    - Choices: **_`content`_**, `threshold`, `adaptive`


    > pick a scene detector algorithm, see http://scenedetect.com/projects/Manual/en/latest/cli/detectors.html
- `threshold`: optional, defaults to `27.0`

    - Type: number
    - Multivalued: False


    > threshold value to use in the detection algorithm. Note that the meaning of this numerical value differs for different detector algorithms.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v3](http://mmif.clams.ai/vocabulary/TimeFrame/v3)
    - _label_ = "shot"
    - _timeUnit_ = "frame"

