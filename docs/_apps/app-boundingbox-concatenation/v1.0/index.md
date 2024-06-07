---
layout: posts
classes: wide
title: "BoundingBox Concatenation (v1.0)"
date: 2024-06-07T15:41:38+00:00
---
## About this version

- Submitter: [MrSqually](https://github.com/MrSqually)
- Submission Time: 2024-06-07T15:41:38+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-boundingbox-concatenation:v1.0](https://github.com/clamsproject/app-boundingbox-concatenation/pkgs/container/app-boundingbox-concatenation/v1.0)
- Release Notes

    > initial public release of bbox-concat

## About this app (See raw [metadata.json](metadata.json))

**Converts a series of bounding-boxes at a given timepoint into a single bounding box.**

- App ID: [http://apps.clams.ai/app-boundingbox-concatenation/v1.0](http://apps.clams.ai/app-boundingbox-concatenation/v1.0)
- App License: MIT
- Source Repository: [https://github.com/clamsproject/app-boundingbox-concatenation](https://github.com/clamsproject/app-boundingbox-concatenation) ([source tree of the submitted version](https://github.com/clamsproject/app-boundingbox-concatenation/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/Document/v1](http://mmif.clams.ai/vocabulary/Document/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `timeUnit`: optional, defaults to `frames`

    - Type: string
    - Multivalued: False
    - Choices: **_`frames`_**, `seconds`, `milliseconds`


    > the division of time processing
- `boxType`: optional, defaults to `text`

    - Type: string
    - Multivalued: False


    > the type of boxes that are being concatenated


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1)
(of any properties)

