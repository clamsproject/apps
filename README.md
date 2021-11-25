# CLAMS Apps

## Repository naming convention

* Applications in the `clamsproject` organization should prefixed with `app-`. 
* An application that wraps an extant tool or application must be suffixed with `-wrapper`. 
* `LICENSE` file should always contains licensing information of the terminal tool. If the terminal tool is a wrapper, an additional file containing licensing information of the original tool must be placed next to the `LICENSE` file when the original license requires so. 

## Requirements for CLAMS applications

1. An app should implement [`ClamsApp`](https://github.com/clamsproject/clams-python-sdk/blob/master/clams/serve/__init__.py) in the python SDK
1. An app is recommended to be served as a REST-ful web service. See [`Restifier`](https://github.com/clamsproject/clams-python-sdk/blob/master/clams/restify/__init__.py) in the SDK. 
1. To be compatible with [the CLAMS galaxy appliance](https://github.com/clamsproject/appliance), an app repository should provide a `dockerfile` to make a single-purposed docker container for the app. 


## Apps in action 

| App name (link) | AnnotationType | Latest (link) | Based-on ([`clams-python`](https://sdk.clams.ai/target-versions.html)) | Documentation (link) | Evaluation |
| --- | --- | :---: | :---: | --- | --- |
| [fastpunct](https://github.com/clamsproject/app-fastpunct) | text > text | [main](https://github.com/clamsproject/app-fastpunct/tree/02b2e01e7239162dceda86ad577507f0fc6b6ecf) | [0.5.0](https://github.com/clamsproject/app-fastpunct/blob/02b2e01e7239162dceda86ad577507f0fc6b6ecf/requirements.txt#L1) | [README](https://github.com/clamsproject/app-fastpunct/blob/02b2e01e7239162dceda86ad577507f0fc6b6ecf/README.md)| [Plan](https://github.com/clamsproject/app-fastpunct/blob/main/evaluation/README.md) |
| [spacy-nlp](https://github.com/clamsproject/app-spacy-nlp) | text > text | [0.0.6](https://github.com/clamsproject/app-spacy-nlp/tree/v0.0.6) | [0.2.4](https://github.com/clamsproject/app-spacy-nlp/blob/v0.0.6/requirements.txt#L1) | [README](https://github.com/clamsproject/app-spacy-nlp/blob/v0.0.6/README.md)| [Plan](https://github.com/clamsproject/app-spacy-nlp/blob/master/evaluation.md) |
| [slate-textdetection](https://github.com/clamsproject/app-slate-textdetection) | video > boundingbox | [main](https://github.com/clamsproject/app-slate-textdetection/tree/d937b38f99f9584a6b83f8c08c91bf07fc9997df) | [*](https://github.com/clamsproject/app-slate-textdetection/blob/d937b38f99f9584a6b83f8c08c91bf07fc9997df/requirements.txt#L7) | [README](https://github.com/clamsproject/app-slate-textdetection/blob/d937b38f99f9584a6b83f8c08c91bf07fc9997df/README.md) (docker, example input MMIF)| [Plan](https://github.com/clamsproject/app-slatedetection/blob/master/evaluation.md) |
| [tesseractocr-wrapper](https://github.com/clamsproject/app-tesseractocr-wrapper) | video > text | [main](https://github.com/clamsproject/app-tesseractocr-wrapper) | [0.4.3](https://github.com/clamsproject/app-tesseractocr-wrapper/blob/771c975cf28dcd8abab265c94aebdabb9cd8a3b6/requirements.txt#L6) | [README](https://github.com/clamsproject/app-tesseractocr-wrapper/blob/771c975cf28dcd8abab265c94aebdabb9cd8a3b6/README.md) (docker, params)|  |
| [inaspeechsegmenter-wrapper](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper) | audio > timeframe | [0.2.3](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/tree/v0.2.3) | [0.4.4](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/blob/v0.2.3/requirements.txt#L1) | [README](https://github.com/clamsproject/app-inaspeechsegmenter-wrapper/blob/v0.2.3/README.md)|  |
| [brandeis-acs](https://github.com/clamsproject/app-brandeis-acs) | audio > timeframe | [0.3.4](https://github.com/clamsproject/app-brandeis-acs/tree/v0.3.4) | [0.4.*](https://github.com/clamsproject/app-brandeis-acs/blob/v0.3.4/requirements.txt#L1) | [README](https://github.com/clamsproject/app-brandeis-acs/blob/v0.3.4/README.md) (quite emtpy)|  |
| [aapb-pua-kaldi-wrapper](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper) | audio > text | [0.2.3](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper/tree/v0.2.3) | [0.4.4](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper/blob/v0.2.3/requirements.txt#L1) | [README](https://github.com/clamsproject/app-aapb-pua-kaldi-wrapper/blob/v0.2.3/README.md) (quite empty)|  |
| [gentle-forced-aligner-wrapper](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper) | audio + text > timeframe | [0.1.0](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/tree/v0.1.0) | [0.4.4](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/blob/v0.1.0/requirements.txt#L2) | [README](https://github.com/clamsproject/app-gentle-forced-aligner-wrapper/blob/v0.1.0/README.md)|  |
| [bardetection](https://github.com/clamsproject/app-barsdetection) | video > timeframe | [main](https://github.com/clamsproject/app-barsdetection) | [0.2.2](https://github.com/clamsproject/app-barsdetection/blob/master/requirements.txt#L5) | [README](https://github.com/clamsproject/app-barsdetection/blob/master/README.md) (docker, example input MMIF)| [Plan](https://github.com/clamsproject/app-barsdetection/blob/master/evaluation.md) |
