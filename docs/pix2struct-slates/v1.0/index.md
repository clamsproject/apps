
* Submitter: [snewman-aa](https://github.com/snewman-aa)
* Submission Time: 2023-08-22T19:40:43+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-pix2struct-slates:v1.0](https://github.com/clamsproject/app-pix2struct-slates/pkgs/container/app-pix2struct-slates/v1.0)


### Pix2struct Slates (v1.0) [metadata.json](metadata.json)
###### Run Pix2Struct slate queries on input timeframes

* App ID: [http://apps.clams.ai/pix2struct-slates/v1.0](http://apps.clams.ai/pix2struct-slates/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-pix2struct-slates](https://github.com/clamsproject/app-pix2struct-slates) ([source tree of the submitted version](https://github.com/clamsproject/app-pix2struct-slates/tree/v1.0))
* Analyzer Version: 1
* Analyzer License: Apache-2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) (required)
###### frameType=slate


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
