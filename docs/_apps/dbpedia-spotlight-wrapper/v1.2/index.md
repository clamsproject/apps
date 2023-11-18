---
layout: single
classes: wide
title: "Dbpedia Spotlight Wrapper (v1.2)"
---
* Submitter: [wricketts](https://github.com/wricketts)
* Submission Time: 2023-08-24T15:51:13+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-dbpedia-spotlight-wrapper:v1.2](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper/pkgs/container/app-dbpedia-spotlight-wrapper/v1.2)


### Dbpedia Spotlight Wrapper (v1.2) [metadata.json](metadata.json)
###### Apply named entity linking to all text documents in a MMIF file.

* App ID: [http://apps.clams.ai/dbpedia-spotlight-wrapper/v1.2](http://apps.clams.ai/dbpedia-spotlight-wrapper/v1.2)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-dbpedia-spotlight-wrapper](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-dbpedia-spotlight-wrapper/tree/v1.2))
* Analyzer Version: daf5309
* Analyzer License: Apache 2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|confidence|disambiguation confidence score for linking|number|N|0.5||
|support|resource prominence, i.e. number of in-links in Wikipedia (lower bound)|integer|N|0||
|types|limits recognition to certain types of named entities, e.g. DBpedia:Place|string|Y|||
|policy|(whitelist) selects all entities of the same type; (blacklist) selects all entities not of the same type|string|N|whitelist|**_`whitelist`_**, `blacklist`|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://vocab.lappsgrid.org/NamedEntity](http://vocab.lappsgrid.org/NamedEntity) 
###### ANY
