
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-24T20:01:10+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-gentle-forced-aligner-wrapper:v1.0](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/pkgs/container/app-gentle-forced-aligner-wrapper/v1.0)


### Gentle Forced Aligner Wrapper (v1.0) [metadata.json](metadata.json)
###### This CLAMS app aligns transcript and audio track using Gentle. Gentle is a robust yet lenient forced aligner built on Kaldi.This app only works when Gentle is already installed locally.Unfortunately, Gentle is not distributed as a Python package distribution.To get Gentle installation instruction, see https://lowerquality.com/gentle/ Make sure install Gentle from the git commit specified in ``analyzer_version`` in this metadata.

* App ID: [http://apps.clams.ai/gentle-forced-aligner-wrapper/v1.0](http://apps.clams.ai/gentle-forced-aligner-wrapper/v1.0)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-gentle-forced-aligner-wrapper](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/tree/v1.0))
* Analyzer Version: f29245a
* Analyzer License: MIT


#### Inputs
* [http://mmif.clams.ai/vocabulary/TextDocument/v1](http://mmif.clams.ai/vocabulary/TextDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
###### ANY
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### frameType=speech
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|use_speech_segmentation|When set true, use exising "speech"-typed ``TimeFrame`` annotations and run aligner only on those frames, instead of entire audio files.|boolean|False|`false`, **_`true`_**|
|use_tokenization|When set true, ``Alignment`` annotation output will honor existing latest tokenization (``Token`` annotations). Due to a limitation of the way Kaldi reads in English tokens, existing tokens must not contain whitespaces. |boolean|False|`false`, **_`true`_**|
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|False|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token) 
###### ANY
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### frameType=speech, timeUnit=milliseconds
* [http://mmif.clams.ai/vocabulary/Alignment/v1](http://mmif.clams.ai/vocabulary/Alignment/v1) 
###### ANY
