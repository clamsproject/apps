---
layout: posts
classes: wide
title: "Tfidf Keywordextractor (v1.0)"
date: 2024-07-19T14:07:21+00:00
---
## About this version

- Submitter: [selenasong](https://github.com/selenasong)
- Submission Time: 2024-07-19T14:07:21+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-tfidf-keywordextractor:v1.0](https://github.com/clamsproject/app-tfidf-keywordextractor/pkgs/container/app-tfidf-keywordextractor/v1.0)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**extract keywords of a text document according to TF-IDF values. IDF values and all features come from related pickle files in the current directory.App can either take a simple text document or take a MMIF file generated from the text slicer app.**

- App ID: [http://apps.clams.ai/tfidf-keywordextractor/v1.0](http://apps.clams.ai/tfidf-keywordextractor/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-tfidf-keywordextractor](https://github.com/clamsproject/app-tfidf-keywordextractor) ([source tree of the submitted version](https://github.com/clamsproject/app-tfidf-keywordextractor/tree/v1.0))


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `topN`: optional, defaults to `10`

    - Type: integer
    - Multivalued: False


    > top n keywords to extract from the current textfile.
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)
    - _text_ = "keywords"
    - _scores_ = "tfidf scores"

    > Default property 'text' stores the extracted keywords (string). Added property 'scores' stores keywords' TF-IDF values (float).
- [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1)
(of any properties)

