
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-26T00:03:43+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-tesseractocr-wrapper:v1.0](https://github.com/clamsproject/app-tesseractocr-wrapper/pkgs/container/app-tesseractocr-wrapper/v1.0)


### Tesseract OCR Wrapper (v1.0) [metadata.json](metadata.json)
###### This tool applies Tesseract OCR to a video or image and generates text boxes and OCR results.

* App ID: [http://apps.clams.ai/tesseractocr-wrapper/v1.0](http://apps.clams.ai/tesseractocr-wrapper/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-tesseractocr-wrapper](https://github.com/clamsproject/app-tesseractocr-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-tesseractocr-wrapper/tree/v1.0))
* Analyzer Version: tesseract4
* Analyzer License: apache


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/BoundingBox/v1](http://mmif.clams.ai/vocabulary/BoundingBox/v1) (required)
###### boxType=text
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|frameType|Use this to specify TimeFrame to use for filtering "text"-typed BoundingBox annotations. Can be "slate", "chyron", "speech", etc.. If not set, the app won't use TimeFrames for filtering.|string|Y|||
|threshold|Use this value between 0 and 1 to filter out low-confidence text boxes.|number|N|0.9||
|psm|Tesseract Page Segmentation Modes. See https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html#page-segmentation-method|integer|N|0|**_`0`_**, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) 
###### ANY
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
###### ANY
