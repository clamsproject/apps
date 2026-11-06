---
layout: posts
classes: wide
title: "TimeFrame Heuristic Winnower (v0.1)"
date: 2026-11-03T18:16:34+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-11-03T18:16:34+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-timeframe-heuristic-winnower:v0.1](https://github.com/clamsproject/app-timeframe-heuristic-winnower/pkgs/container/app-timeframe-heuristic-winnower/v0.1)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-timeframe-heuristic-winnower:v0.1" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > first pre-release version

## About this app (See raw [metadata.json](metadata.json))

**Selects segment boundaries by agreement across upstream views. Every view in the input MMIF that carries time-anchored annotations is a source of candidate boundary events (a view whose TimeFrames declare different `labelsetUri` values is one source per value): the endpoints of its Sentence annotations when it has any, otherwise the endpoints of its TimeFrame annotations (word-level frames aligned to Tokens are skipped). Events are widened into a window of `windowMs`, and a boundary is a point where at least the share `minAgreementRatio` of the sources agree. Among boundaries closer than `minSeparationMs`, the best-corroborated set is selected exactly by dynamic programming. Output is one `segment` TimeFrame per interval between consecutive boundaries. The method needs no model and no GPU. The JCDL 2026 paper (https://doi.org/10.1145/3805696.3846037) used these defaults with `minAgreementRatio=0.8` over five sources (whisper-wrapper, pyannotesd-wrapper, pyscenedetect-wrapper, inaspeechsegmenter-wrapper, swt-detection).**

- App ID: [http://apps.clams.ai/timeframe-heuristic-winnower/v0.1](http://apps.clams.ai/timeframe-heuristic-winnower/v0.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-timeframe-heuristic-winnower](https://github.com/clamsproject/app-timeframe-heuristic-winnower) ([source tree of the submitted version](https://github.com/clamsproject/app-timeframe-heuristic-winnower/tree/v0.1)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-timeframe-heuristic-winnower/tree/v0.1" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

One of the following is required: [
- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6) (required)
(of any properties)

    > Time-anchored annotations from any upstream app. Each view that contains them is one voting source. Each TimeFrame must have a `document`, on the annotation or at view level. Filter by label with `tfLabels` and `tfLabelIgnore`.
- [http://clams.ai/vocabulary/type/Sentence/v1](http://clams.ai/vocabulary/type/Sentence/v1) (required)
(of any properties)

    > Sentence annotations whose `targets` are Tokens aligned to TimeFrames (as produced by ASR apps such as whisper-wrapper). When a view has Sentences, their endpoints are used as that view's events instead of its TimeFrames.


]
- [http://clams.ai/vocabulary/type/Token/v1](http://clams.ai/vocabulary/type/Token/v1)
(of any properties)

- [http://clams.ai/vocabulary/type/Alignment/v1](http://clams.ai/vocabulary/type/Alignment/v1)
(of any properties)



#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `windowMs`: optional, defaults to `5000`

    - Type: integer
    - Multivalued: False


    > W: width in milliseconds of the window each candidate event is widened into before sources are compared.
- `minAgreementRatio`: optional, defaults to `0.5`

    - Type: number
    - Multivalued: False


    > Share of the voting sources of a document that must agree for a point to become a candidate boundary, in (0, 1]. The minimum number of sources K is this share of the number of sources, rounded up and at least 1: with the default, one of two sources, two of three, or three of five. When K is 1, the app warns that the boundaries are not corroborated.
- `minSeparationMs`: optional, defaults to `20000`

    - Type: integer
    - Multivalued: False


    > M: minimum distance in milliseconds between two selected boundaries, and from the start and the end of the recording. Encodes the shortest admissible segment. 0 disables the constraint.
- `tfLabels`: optional, defaults to `[]`

    - Type: string
    - Multivalued: True


    > Label(s) of input TimeFrame annotations to use as candidate events. By default (`[]`) every TimeFrame is used regardless of label. When set, TimeFrames without a label are not used. Sentence-derived events are not affected.
- `tfLabelIgnore`: optional, defaults to `['segment']`

    - Type: string
    - Multivalued: True


    > Label(s) of input TimeFrame annotations to leave out, applied after `tfLabels`. The default leaves out this app's own `segment` output, and setting this parameter replaces the default. TimeFrames without a label are never dropped by this list. Sentence-derived events are not affected.
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

- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6)
    - _timeUnit_ = "milliseconds"
    - _label_ = "segment"

    > One TimeFrame per segment between consecutive selected boundaries, tiling each document that the input TimeFrames refer to. Each carries the `document` of those TimeFrames. Start and end are integer milliseconds.
