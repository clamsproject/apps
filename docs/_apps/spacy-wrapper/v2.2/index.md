---
layout: posts
classes: wide
title: "CLAMS wrapper for spaCy NLP (v2.2)"
date: 2026-06-18T19:06:20+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-06-18T19:06:20+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-spacy-wrapper:v2.2](https://github.com/clamsproject/app-spacy-wrapper/pkgs/container/app-spacy-wrapper/v2.2)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-spacy-wrapper:v2.2" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > bumped SDK to 1.7.0, spacy to 3.8

## About this app (See raw [metadata.json](metadata.json))

**Apply spaCy NLP to all text documents in a MMIF file.**

- App ID: [http://apps.clams.ai/spacy-wrapper/v2.2](http://apps.clams.ai/spacy-wrapper/v2.2)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-spacy-wrapper](https://github.com/clamsproject/app-spacy-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-spacy-wrapper/tree/v2.2)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-spacy-wrapper/tree/v2.2" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer Version: 3.8.*
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://clams.ai/vocabulary/type/TextDocument/v2](http://clams.ai/vocabulary/type/TextDocument/v2) (required)
(of any properties)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `pretokenized`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > Boolean parameter to set the app to use existing tokenization, if available, for text documents for NLP processing. Useful to process ASR documents, for example.
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

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)

- [http://vocab.lappsgrid.org/Token#pos](http://vocab.lappsgrid.org/Token#pos)
(of any properties)

- [http://vocab.lappsgrid.org/Token#lemma](http://vocab.lappsgrid.org/Token#lemma)
(of any properties)

- [http://vocab.lappsgrid.org/NounChunk](http://vocab.lappsgrid.org/NounChunk)
(of any properties)

- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

- [http://vocab.lappsgrid.org/NamedEntity](http://vocab.lappsgrid.org/NamedEntity)
(of any properties)

