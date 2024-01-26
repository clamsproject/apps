---
layout: posts
classes: wide
title: "Dbpedia Spotlight Wrapper (v1.0)"
date: 2023-07-24T17:07:36+00:00
---
## About this version

* Submitter: [wricketts](https://github.com/wricketts)
* Submission Time: 2023-07-24T17:07:36+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-dbpedia-spotlight-wrapper:v1.0](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper/pkgs/container/app-dbpedia-spotlight-wrapper/v1.0)
* Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Apply named entity linking to all text documents in a MMIF file.**

* App ID: [http://apps.clams.ai/dbpedia-spotlight-wrapper/v1.0](http://apps.clams.ai/dbpedia-spotlight-wrapper/v1.0)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-dbpedia-spotlight-wrapper](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper/tree/v1.0))
* Analyzer Version: version_1.0
* Analyzer License: Apache 2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1)  (required)
(any properties)


#### Configurable Parameters
**(_Multivalued_ means the parameter can have one or more values.)**

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|confidence|disambiguation confidence score for linking|number|N|0.5||
|support|resource prominence, i.e. number of in-links in Wikipedia (lower bound)|integer|N|0||
|types|limits recognition to certain types of named entities, e.g. DBpedia:Place|string|Y|||
|policy|(whitelist) selects all entities of the same type; (blacklist) selects all entities not of the same type|string|N|whitelist|**_`whitelist`_**, `blacklist`|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
**(Note that not all output annotations are always generated.)**
* [http://vocab.lappsgrid.org/NamedEntity](http://vocab.lappsgrid.org/NamedEntity) 
(any properties)
