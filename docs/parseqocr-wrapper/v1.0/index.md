
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-26T00:04:08+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-parseqocr-wrapper:v1.0](https://github.com/clamsproject/app-parseqocr-wrapper/pkgs/container/app-parseqocr-wrapper/v1.0)


### Parseq OCR Wrapper (v1.0) [metadata.json](metadata.json)
###### This tool applies Parseq OCR to a video or image and generates text boxes and OCR results.

* App ID: [http://apps.clams.ai/parseqocr-wrapper/v1.0](http://apps.clams.ai/parseqocr-wrapper/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-parseqocr-wrapper](https://github.com/clamsproject/app-parseqocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-parseqocr-wrapper/tree/v1.0))
* Analyzer Version: bc8d95cd
* Analyzer License: Apache 2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) (required)
###### boxType=text


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
###### ANY
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
###### ANY
