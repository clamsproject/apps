---
layout: posts
classes: wide
title: "CLAMS docTR Wrapper (v1.2)"
date: 2025-05-23T01:46:09+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-05-23T01:46:09+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-doctr-wrapper:v1.2](https://github.com/clamsproject/app-doctr-wrapper/pkgs/container/app-doctr-wrapper/v1.2)
- Release Notes

    > Minor update to support latest SDK  
    > - updated to the latext SDK, and hence added `cli.py` entry point  
    > - in various newly-generated annotation objects, all references to other annotation ID are now "long" form (`view_id:ann_id`) even when referring annotations within the same view  
    > - now only processes `TimeFrame` with `label` property (effectively ignores time frames from, for example, whisper-wrapper)  
    > - made model caching path inside the container consistent with other CLAMS apps (`/cache/doctr`)

## About this app (See raw [metadata.json](metadata.json))

**CLAMS app wraps the [docTR, End-to-End OCR model](https://pypi.org/project/python-doctr). The model can detect text regions in the input image and recognize text in the regions (via parseq OCR model, only English is support at the moment). The text-localized regions are organized hierarchically by the model into "pages" > "blocks" > "lines" > "words", and this CLAMS app translates them into `TextDocument`, `Paragraphs`, `Sentence`, and `Token` annotations to represent recognized text contents. See descriptions for I/O types below  for details on how annotations are aligned to each other.**

- App ID: [http://apps.clams.ai/doctr-wrapper/v1.2](http://apps.clams.ai/doctr-wrapper/v1.2)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-doctr-wrapper](https://github.com/clamsproject/app-doctr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-doctr-wrapper/tree/v1.2))
- Analyzer Version: 0.8.1
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
(of any properties)

- [http://mmif.clams.ai/vocabulary/TimeFrame/v5](http://mmif.clams.ai/vocabulary/TimeFrame/v5) (required)
    - _representatives_ = "?"
    - _label_ = "*"

    > The _labeled_ TimeFrame annotation that represents the video segment to be processed. When `representatives` property is present, the app will process videos still frames at the underlying time point annotations that are referred to by the `representatives` property. Otherwise, the app will process the middle frame of the video segment. Generic TimeFrames with no `label` property will not be processed.


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

    > Translation of the recognized docTR "words" in the input images. `text` and `word` properties store the string values of the recognized text. The duplication is for keepingbackward compatibility and consistency with `Paragraph` and `Sentence` annotations.
- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
    - _text_ = "*"

    > Translation of the recognized docTR "lines" in the input images. `text` property stores the string value of space-joined words.
- [http://vocab.lappsgrid.org/Paragraph](http://vocab.lappsgrid.org/Paragraph)
    - _text_ = "*"

    > Translation of the recognized docTR "blocks" in the input images. `text` property stores the string value of newline-joined sentences.
- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

    > Alignments between 1) `TimePoint` <-> `TextDocument`, 2) `TimePoint` <-> `Token`/`Sentence`/`Paragraph`, 3) `BoundingBox` <-> `Token`/`Sentence`/`Paragraph`
- [http://mmif.clams.ai/vocabulary/BoundingBox/v4](http://mmif.clams.ai/vocabulary/BoundingBox/v4)
    - _label_ = "text"

    > Bounding boxes of the detected text regions in the input images. No corresponding box for the entire image (`TextDocument`) region
