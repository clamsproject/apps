
* Submitter: [snewman-aa](https://github.com/snewman-aa)
* Submission Time: 2023-08-22T19:40:18+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-pix2struct-chyrons:v1.0](https://github.com/clamsproject/app-pix2struct-docvqa-wrapper/pkgs/container/app-pix2struct-docvqa-wrapper/v1.0)


### Pix2struct Chyrons (v1.0) [metadata.json](metadata.json)
###### extracts text from input timeframes based on chyron queries using the pix2struct Doc-VQA model

* App ID: [http://apps.clams.ai/pix2struct-chyrons/v1.0](http://apps.clams.ai/pix2struct-chyrons/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-pix2struct-docvqa-wrapper](https://github.com/clamsproject/app-pix2struct-docvqa-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-pix2struct-docvqa-wrapper/tree/v1.0))
* Analyzer Version: 1
* Analyzer License: apache-2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) (required)
###### frameType=chyron


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

##### N/A


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
###### description=extracted text from input timeframes based on chyron queries using the pix2struct Doc-VQA model
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
###### description=alignment between text document and timeframes
