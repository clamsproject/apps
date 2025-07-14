---
layout: posts
classes: wide
title: "Heuristic Chyron Understanding (v0.2)"
date: 2025-07-14T23:10:14+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-07-14T23:10:14+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-heuristic-chyron-understanding:v0.2](https://github.com/clamsproject/app-heuristic-chyron-understanding/pkgs/container/app-heuristic-chyron-understanding/v0.2)
- Release Notes

    > Initial release with naive line parsing and name normalization

## About this app (See raw [metadata.json](metadata.json))

**Prototype to convert chyron text from docTR/Tesseract/LLaVA MMIF outputinto a name and list of attributes.**

- App ID: [http://apps.clams.ai/heuristic-chyron-understanding/v0.2](http://apps.clams.ai/heuristic-chyron-understanding/v0.2)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-heuristic-chyron-understanding](https://github.com/clamsproject/app-heuristic-chyron-understanding) ([source tree of the submitted version](https://github.com/clamsproject/app-heuristic-chyron-understanding/tree/v0.2))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
(of any properties)

    > Text content transcribed from video input by docTR/Tesseract/LLAVA.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `note4mode`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > Boolean to set the app to run in "note-4" mode and to take the second line (if available) from the input text to be the `name-normalized` value. The default is false, which means the app will try to generate normalization from`name-as-written` (from the first line) value. 
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

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
    - _document_ = "*"
    - _origin_ = "*"
    - _provenance_ = "derived"
    - _mime_ = "application/json"

    > Reformatted chyron text. `document` property stores the ID of the original source `VideoDocument`. `origin` property stores the ID of the original OCR `TextDocument` annotation. Reformatted text is escaped JSON string with three fields: `name-as-written`, `name-normalized`, and `attributes`. 
