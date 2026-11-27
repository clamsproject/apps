---
layout: posts
classes: wide
title: "Heuristic Chyron Understanding (v0.3)"
date: 2026-11-27T22:03:43+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-11-27T22:03:43+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-heuristic-chyron-understanding:v0.3](https://github.com/clamsproject/app-heuristic-chyron-understanding/pkgs/container/app-heuristic-chyron-understanding/v0.3)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-heuristic-chyron-understanding:v0.3" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > Compatible with latest TextDocument shape with `origins`

## About this app (See raw [metadata.json](metadata.json))

**Prototype to convert chyron text from OCR output (e.g., docTR, Tesseract or a VLM captioner) into a name and list of attributes, with line-based heuristics.**

- App ID: [http://apps.clams.ai/heuristic-chyron-understanding/v0.3](http://apps.clams.ai/heuristic-chyron-understanding/v0.3)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-heuristic-chyron-understanding](https://github.com/clamsproject/app-heuristic-chyron-understanding) ([source tree of the submitted version](https://github.com/clamsproject/app-heuristic-chyron-understanding/tree/v0.3)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-heuristic-chyron-understanding/tree/v0.3" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://clams.ai/vocabulary/type/TextDocument/v2](http://clams.ai/vocabulary/type/TextDocument/v2) (required)
(of any properties)

    > Chyron text transcribed by an OCR app. The app reads the TextDocuments of the last view that has any; without such a view, the top-level TextDocuments of the MMIF. Empty texts and "no text" markers (e.g., `NONE`, `N/A`) are skipped, and markdown code fence lines (e.g., "```") around the text are ignored.


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
- `runningTime`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata
- `tfSamplingMode`: optional, defaults to `representatives`

    - Type: string
    - Multivalued: False
    - Choices: **_`representatives`_**, `single`, `all`


    > Sampling mode for TimeFrame annotations. Has no effect when the app does not process TimeFrames. "representatives" uses all representative timepoints if present, otherwise skips the TimeFrame. "single" uses the middle representative if present, otherwise extracts an image from the midpoint of the start/end interval (midpoint is calculated by floor division of the sum of start and end). "all" uses all target timepoints if present, otherwise extracts all images from the time interval.


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://clams.ai/vocabulary/type/TextDocument/v2](http://clams.ai/vocabulary/type/TextDocument/v2)
    - _document_ = "*"
    - _origins_ = "*"
    - _origination_ = "derived"
    - _mime_ = "application/json"

    > Reformatted chyron text, one per input TextDocument: a JSON string with three fields, `name-as-written`, `name-normalized` and `attributes`. The `origins` property points to the input OCR TextDocument; `document` is copied from it, or else is the ID of the source `VideoDocument`.
