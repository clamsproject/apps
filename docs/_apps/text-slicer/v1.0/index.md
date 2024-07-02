---
layout: posts
classes: wide
title: "Text Slicer (v1.0)"
date: 2024-07-02T01:30:06+00:00
---
## About this version

- Submitter: [bohJiang12](https://github.com/bohJiang12)
- Submission Time: 2024-07-02T01:30:06+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-text-slicer:v1.0](https://github.com/clamsproject/app-text-slicer/pkgs/container/app-text-slicer/v1.0)
- Release Notes

    > first version of text-slicer

## About this app (See raw [metadata.json](metadata.json))

**Slice text snippets from a provided text document given time frames**

- App ID: [http://apps.clams.ai/text-slicer/v1.0](http://apps.clams.ai/text-slicer/v1.0)
- App License: Apache2
- Source Repository: [https://github.com/clamsproject/app-text-slicer](https://github.com/clamsproject/app-text-slicer) ([source tree of the submitted version](https://github.com/clamsproject/app-text-slicer/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `containLabel`: required

    - Type: string
    - Multivalued: True


    > A list of labels that user expect TimeFrames contain.<br/>Labels can be chosen from but not limited to:<br/>['bars', 'tones', 'bars-and-tones','speech','noise',<br/> 'music', 'slate', 'chyron', 'lower-third', 'credits']<br/>Users are required to select at least one label. Otherwise, errors would be thrown instead
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
(of any properties)

- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

