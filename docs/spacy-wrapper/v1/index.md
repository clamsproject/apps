
### CLAMS wrapper for spaCy NLP (v1) [metadata.json](metadata.json)
###### Apply spaCy NLP to all text documents in a MMIF file.

* App ID: [https://apps.clams.ai/spacy-wrapper/v1](https://apps.clams.ai/spacy-wrapper/v1)
* App License: Apache 2.0
* Source Repository: [https://github.com/clamsproject/app-spacy-nlp](https://github.com/clamsproject/app-spacy-nlp)
* Prebuilt Container Image: [ghcr.io/clamsproject/app-spacy-wrapper:v1](ghcr.io/clamsproject/app-spacy-wrapper:v1)
* Analyzer Version: 3.1.2
* Analyzer License: MIT


#### Inputs
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
###### ANY
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|pretokenized|Boolean parameter to set the app to use existing tokenization, if available, for text documents for NLP processing. Useful to process ASR documents, for example.|boolean|False|**`false`** (*), `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
###### ANY
* [http://vocab.lappsgrid.org/Token#pos](http://vocab.lappsgrid.org/Token#pos) 
###### ANY
* [http://vocab.lappsgrid.org/Token#lemma](http://vocab.lappsgrid.org/Token#lemma) 
###### ANY
* [http://vocab.lappsgrid.org/NounChunk](http://vocab.lappsgrid.org/NounChunk) 
###### ANY
* [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence) 
###### ANY
* [http://vocab.lappsgrid.org/NamedEntity](http://vocab.lappsgrid.org/NamedEntity) 
###### ANY

