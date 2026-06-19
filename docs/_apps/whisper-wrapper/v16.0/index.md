---
layout: posts
classes: wide
title: "Whisper Wrapper (v16.0)"
date: 2026-06-19T20:37:50+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-06-19T20:37:50+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-whisper-wrapper:v16.0](https://github.com/clamsproject/app-whisper-wrapper/pkgs/container/app-whisper-wrapper/v16.0)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-whisper-wrapper:v16.0" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**A CLAMS wrapper for Whisper-based ASR software originally developed by OpenAI.**

- App ID: [http://apps.clams.ai/whisper-wrapper/v16.0](http://apps.clams.ai/whisper-wrapper/v16.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-whisper-wrapper](https://github.com/clamsproject/app-whisper-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-whisper-wrapper/tree/v16.0)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-whisper-wrapper/tree/v16.0" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer License: MIT


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://clams.ai/vocabulary/type/AudioDocument/v2](http://clams.ai/vocabulary/type/AudioDocument/v2) (required)
(of any properties)

- [http://clams.ai/vocabulary/type/VideoDocument/v2](http://clams.ai/vocabulary/type/VideoDocument/v2) (required)
(of any properties)



]


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `model`: optional, defaults to `turbo`

    - Type: string
    - Multivalued: False
    - Choices: `tiny.en`, `tiny`, `base.en`, `base`, `small.en`, `small`, `medium.en`, `medium`, `large-v1`, `large-v2`, `large-v3`, `large-v3-turbo`, `t`, `b`, `s`, `m`, `l`, `l2`, `l3`, `tu`, `large`, **_`turbo`_**


    > (from openai-whisper CLI) name of the Whisper model to use. Canonical names are the keys of this app's `analyzer_versions`; short aliases (e.g. `tu`/`turbo` for `large-v3-turbo`) are also accepted.
- `language`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) language spoken in the audio, specify None to perform language detection. For the list of supported language codes, see https://github.com/openai/whisper/blob/04f449b8a437f1bbd3dba5c9f826aca972e7709a/whisper/tokenizer.py
- `task`: optional, defaults to `transcribe`

    - Type: string
    - Multivalued: False
    - Choices: **_`transcribe`_**, `translate`


    > (from openai-whisper CLI) whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')
- `initialPrompt`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) optional text to provide as a prompt for the first window.
- `conditionOnPreviousText`: optional, defaults to `True`

    - Type: string
    - Multivalued: False


    > (from openai-whisper CLI) if True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to getting stuck in a failure loop
- `noSpeechThreshold`: optional, defaults to `0.6`

    - Type: number
    - Multivalued: False


    > (from openai-whisper CLI) if the probability of the <|nospeech|> token is higher than this value AND the decoding has failed due to `logprob_threshold`, consider the segment as silence
- `pretty`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The JSON body of the HTTP response will be re-formatted with 2-space indentation
- `runningTime`: optional, defaults to `true`

    - Type: boolean
    - Multivalued: False
    - Choices: `false`, **_`true`_**


    > The running time of the app will be recorded in the view metadata
- `hwFetch`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > The hardware information (architecture, GPU and vRAM) will be recorded in the view metadata
- `tfSamplingMode`: optional, defaults to `representatives`

    - Type: string
    - Multivalued: False
    - Choices: **_`representatives`_**, `single`, `all`


    > Sampling mode for TimeFrame annotations. Has no effect when the app does not process TimeFrames. "representatives" uses all representative timepoints if present, otherwise skips the TimeFrame. "single" uses the middle representative if present, otherwise extracts an image from the midpoint of the start/end interval (midpoint is calculated by floor division of the sum of start and end). "all" uses all target timepoints if present, otherwise extracts all images from the time interval.


#### Outputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

(**Note**: Not all output annotations are always generated.)

- [http://clams.ai/vocabulary/type/TextDocument/v2](http://clams.ai/vocabulary/type/TextDocument/v2)
(of any properties)

- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6)
    - _timeUnit_ = "milliseconds"

- [http://clams.ai/vocabulary/type/Alignment/v1](http://clams.ai/vocabulary/type/Alignment/v1)
(of any properties)

- [http://vocab.lappsgrid.org/Token](http://vocab.lappsgrid.org/Token)
(of any properties)

- [http://vocab.lappsgrid.org/Sentence](http://vocab.lappsgrid.org/Sentence)
(of any properties)

