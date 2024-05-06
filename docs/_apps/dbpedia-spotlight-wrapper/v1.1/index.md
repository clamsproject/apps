---
layout: posts
classes: wide
title: "Dbpedia Spotlight Wrapper (v1.1)"
date: 2023-07-25T01:22:48+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2023-07-25T01:22:48+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-dbpedia-spotlight-wrapper:v1.1](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper/pkgs/container/app-dbpedia-spotlight-wrapper/v1.1)
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Apply named entity linking to all text documents in a MMIF file.**

- App ID: [http://apps.clams.ai/dbpedia-spotlight-wrapper/v1.1](http://apps.clams.ai/dbpedia-spotlight-wrapper/v1.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-dbpedia-spotlight-wrapper](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper/tree/v1.1))
- Analyzer Version: daf5309
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)

 (any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `confidence`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > disambiguation confidence score for linking
- `support`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > resource prominence, i.e. number of in-links in Wikipedia (lower bound)
- `types`: required

    - Type: string
    - Multivalued: False


    > types filter
- `policy`: optional, defaults to `whitelist`

    - Type: string
    - Multivalued: False
    - Choices: **_`whitelist`_**, `blacklist`


    > (whitelist) selects all entities of the same type; (blacklist) selects all entities not of the same type
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://vocab.lappsgrid.org/NamedEntity](http://vocab.lappsgrid.org/NamedEntity)

 (any properties)

