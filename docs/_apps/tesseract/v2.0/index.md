---
layout: posts
classes: wide
title: "TesseractOCR Wrapper (v2.0)"
date: 2025-07-02T02:52:55+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-07-02T02:52:55+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-tesseractocr-wrapper:v2.0](https://github.com/clamsproject/app-tesseractocr-wrapper/pkgs/container/app-tesseractocr-wrapper/v2.0)
- Release Notes

    > Updated to Tesseract5, and output MMIF format matches other TR apps

## About this app (See raw [metadata.json](metadata.json))

**This tool applies Tesseract OCR to a video or image and generates text boxes and OCR results. Currenly only support English language.**

- App ID: [http://apps.clams.ai/tesseract/v2.0](http://apps.clams.ai/tesseract/v2.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-tesseractocr-wrapper](https://github.com/clamsproject/app-tesseractocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-tesseractocr-wrapper/tree/v2.0))
- Analyzer Version: tesseract5.3
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) (required)
    - _representatives_ = "?"

    > The Time frame annotation that represents the video segment to be processed. When `representatives` property is present, the app will process videos still frames at the underlying time point annotations that are referred to by the `representatives` property. Otherwise, the app will process the middle frame of the video segment.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `tfLabel`: optional, defaults to `[]`

    - Type: string
    - Multivalued: True


    > The label of the TimeFrame annotation to be processed. By default (`[]`), all TimeFrame annotations will be processed, regardless of their `label` property values.
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
    - _@lang_ = "en"

    > Fully serialized text content of the recognized text in the input images. Serialization isdone by concatenating `text` values of `Paragraph` annotations with two newline characters.
- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
    - _text_ = "*"
    - _word_ = "*"

    > Translation of the recognized tesseract "words" in the input images. `token` properties store the string values of the recognized text. The duplication is for keepingbackward compatibility and consistency with `Paragraph` and `Sentence` annotations.
- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
    - _text_ = "*"

    > Translation of the recognized tesseract "lines" in the input images. `sentence` property from LAPPS vocab stores the string value of space-joined words.
- [http://vocab.lappsgrid.org/Paragraph](http://vocab.lappsgrid.org/Paragraph)
    - _text_ = "*"

    > Translation of the recognized tesseract "blocks" in the input images. `paragraph` property from LAPPS vocab stores the string value of newline-joined sentences.
- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

    > Alignments between 1) `TimePoint` <-> `TextDocument`, 2) `TimePoint` <-> `Token`/`Sentence`/`Paragraph`, 3) `BoundingBox` <-> `Token`/`Sentence`/`Paragraph`
- [http://mmif.clams.ai/vocabulary/BoundingBox/v4](http://mmif.clams.ai/vocabulary/BoundingBox/v4)
    - _label_ = "text"

    > Bounding boxes of the detected text regions in the input images. No corresponding box for the entire image (`TextDocument`) region
