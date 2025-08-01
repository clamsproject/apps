---
layout: posts
classes: wide
title: "CLAMS wrapper for spaCy NLP (v2.1)"
date: 2025-07-26T21:02:46+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2025-07-26T21:02:46+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-spacy-wrapper:v2.1](https://github.com/clamsproject/app-spacy-wrapper/pkgs/container/app-spacy-wrapper/v2.1)
- Release Notes

    > CLAMS SDK and spacy version bump

## About this app (See raw [metadata.json](metadata.json))

**Apply spaCy NLP to all text documents in a MMIF file.**

- App ID: [http://apps.clams.ai/spacy-wrapper/v2.1](http://apps.clams.ai/spacy-wrapper/v2.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-spacy-wrapper](https://github.com/clamsproject/app-spacy-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-spacy-wrapper/tree/v2.1))
- Analyzer Version: 3.7
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
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

