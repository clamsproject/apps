---
layout: posts
classes: wide
title: "CLAMS docTR Wrapper (v1.0)"
date: 2024-04-22T18:46:07+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2024-04-22T18:46:07+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-doctr-wrapper:v1.0](https://github.com/clamsproject/app-doctr-wrapper/pkgs/container/app-doctr-wrapper/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**CLAMS app wraps the docTR, End-to-End OCR model, available at https://pypi.org/project/python-doctr . The model is capable of detecting text regions in the input image and recognizing text in the regions. The text-localized regions are organized hierarchically by the model into "pages" > "blocks" > "lines" > "words", and this CLAMS app translates them into `TextDocument`, `Paragraphs`, `Sentence`, and `Token` annotations to represent recognized text contents, then aligns them to `BoundingBox` annotations that represent the detected geometries. This hierarchical structure is also represented in the `TextDocument` annotation output as two newlines (`\n\n`) between "paragraphs", one newline (`\n`) between the "lines", and one space (" ") between the "words". For the text recognition, the model is internally configured to use the "parseq" recognition model, and only works with English text at the moment.**

- App ID: [http://apps.clams.ai/doctr-wrapper/v1.0](http://apps.clams.ai/doctr-wrapper/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-doctr-wrapper](https://github.com/clamsproject/app-doctr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-doctr-wrapper/tree/v1.0))
- Analyzer Version: 0.8.1
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)

 (any properties)

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


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
    - _@lang_ = "en"

    > Fully serialized text content of the recognized text in the input images. Serialization isdone by concatenating `text` values of `Paragraph` annotations with two newline characters.
- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
    - _text_ = "*"
    - _word_ = "*"

    > Translation of the recognized docTR "words" in the input images. `text` and `word` properties store the string values of the recognized text. The duplication is for keepingbackward compatibility and consistency with `Paragraph` and `Sentence` annotations.
- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
    - _text_ = "*"

    > Translation of the recognized docTR "lines" in the input images. `text` property stores the string value of space-joined words.
- [http://vocab.lappsgrid.org/Paragraph](http://vocab.lappsgrid.org/Paragraph)
    - _text_ = "*"

    > Translation of the recognized docTR "blocks" in the input images. `text` property stores the string value of newline-joined sentences.
- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)

 (any properties)

    > Alignments between 1) `TimePoint` <-> `TextDocument`, 2) `TimePoint` <-> `Token`/`Sentence`/`Paragraph`, 3) `BoundingBox` <-> `Token`/`Sentence`/`Paragraph`
- [http://mmif.clams.ai/vocabulary/BoundingBox/v4](http://mmif.clams.ai/vocabulary/BoundingBox/v4)
    - _label_ = "text"

    > Bounding boxes of the detected text regions in the input images. No corresponding box for the entire image (`TextDocument`) region
