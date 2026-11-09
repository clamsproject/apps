---
layout: posts
classes: wide
title: "Gemma 4 Captioner (v0.1)"
date: 2026-11-09T01:34:04+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-11-09T01:34:04+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-gemma4-timeframe-captioner:v0.1](https://github.com/clamsproject/app-gemma4-timeframe-captioner/pkgs/container/app-gemma4-timeframe-captioner/v0.1)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-gemma4-timeframe-captioner:v0.1" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    > first experimental release

## About this app (See raw [metadata.json](metadata.json))

**Applies a Gemma 4 vision-language model, run with llama.cpp from a GGUF file, to video frames selected by input TimeFrame annotations for prompt-driven captioning / scene description (experimental llama.cpp backend). Captioning is composite: the frames sampled from a TF are fed to the model in a single prompt and yield one caption. When `maxImagesPerPrompt` is set, a TF with more frames than the cap is split into several prompts and yields one caption per prompt, all aligned to that TF. A `model` runtime parameter selects the Gemma 4 size and quantization (default `ggml-org/gemma-4-E4B-it-GGUF:Q8_0`); see metadata.py for the GPU memory each needs. The app runs its own llama-server process and needs the `llama-server` executable (included in the container image).**

- App ID: [http://apps.clams.ai/gemma4-timeframe-captioner/v0.1](http://apps.clams.ai/gemma4-timeframe-captioner/v0.1)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-gemma4-timeframe-captioner](https://github.com/clamsproject/app-gemma4-timeframe-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-gemma4-timeframe-captioner/tree/v0.1)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-gemma4-timeframe-captioner/tree/v0.1" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://clams.ai/vocabulary/type/VideoDocument/v2](http://clams.ai/vocabulary/type/VideoDocument/v2) (required)
(of any properties)

- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6) (required)
    - _representatives_ = "?"
    - _label_ = "*"

    > Labeled TimeFrame annotations selecting which video segments to caption. Frame selection within each segment is controlled by the universal `tfSamplingMode` parameter (see SDK docs). Filter by label with the `tfLabels` and `tfLabelIgnore` parameters.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `tfLabels`: optional, defaults to `[]`

    - Type: string
    - Multivalued: True


    > Label(s) of input TimeFrame annotations to caption. By default (`[]`), all TimeFrames are processed regardless of label. When set, TimeFrames without a label are not processed.
- `tfLabelIgnore`: optional, defaults to `[]`

    - Type: string
    - Multivalued: True


    > Label(s) of input TimeFrame annotations to leave out, applied after `tfLabels`. TimeFrames without a label are never dropped by this list.
- `prompt`: optional, defaults to `These frames are sampled in order from one segment of a video. Describe what is shown and quote any visible text exactly. Describe only what the frames show; do not guess the date or era.`

    - Type: string
    - Multivalued: True


    > User prompt(s) sent to the model. A single value runs as a one-shot generation. A multi-value list is interpreted as a multi-turn static prompt; see ``promptMode`` for how turns are assembled.
- `systemPrompt`: optional, defaults to `Answer in one plain-text paragraph. Do not use Markdown, headings, lists, or a separate summary.`

    - Type: string
    - Multivalued: False


    > Optional system-role text prepended to the conversation. Empty by default.
- `promptMode`: optional, defaults to `turn-taking`

    - Type: string
    - Multivalued: False
    - Choices: `user-only`, **_`turn-taking`_**


    > How to interpret a multi-value ``prompt`` list. Has no effect when ``prompt`` has a single value. For semantics of each choice and worked examples, see https://clams.ai/clams-python/app-baseclasses.html#promptable-multiturn
- `maxNewTokens`: optional, defaults to `512`

    - Type: integer
    - Multivalued: False


    > Maximum number of new tokens generated per inference call. Forwarded to the backend's ``generate``-equivalent. Larger values grow the KV cache linearly and increase GPU memory usage; reduce if VRAM is constrained.
- `useReasoning`: optional, defaults to `false`

    - Type: boolean
    - Multivalued: False
    - Choices: **_`false`_**, `true`


    > Request the model's reasoning ("thinking") mode. Off by default. Honored only by apps whose backing model has a distinct reasoning mode; apps without one ignore it. When honored and enabled, the reasoning trace is split from the answer and stored in the ``modelReasoningTrace`` property of the output ``TextDocument`` (kept out of the document text). Reasoning is markedly slower and far more token-hungry: the whole trace is generated before the answer and drawn from the same budget capped by ``maxNewTokens``, so raise ``maxNewTokens`` substantially (thousands of tokens, not hundreds) when enabling this, or the trace may consume the entire budget and the answer be truncated or empty. Small reasoning models (as a rule of thumb, roughly 4B parameters and under) are especially prone to non-terminating "thinking loops" that exhaust the budget without producing an answer; validate termination per model before relying on it.
- `temperature`: optional, defaults to `0`

    - Type: number
    - Multivalued: False


    > Sampling temperature. The default ``0.0`` selects deterministic / greedy decoding for maximum reproducibility; override for sampled generation.
- `topP`: optional, defaults to `1`

    - Type: number
    - Multivalued: False


    > Nucleus-sampling cumulative probability cutoff. Only meaningful when ``temperature`` is greater than 0.
- `topK`: optional, defaults to `50`

    - Type: integer
    - Multivalued: False


    > Top-K sampling cutoff. Only meaningful when ``temperature`` is greater than 0.
- `maxImagesPerPrompt`: optional, defaults to `0`

    - Type: integer
    - Multivalued: False


    > Maximum number of images the app bundles into a single prompt (one generation, one output TextDocument). ``0`` means no limit, so all images for a TimeFrame go into one prompt and yield one TextDocument. With a positive N, the app splits a TimeFrame whose frames exceed N into consecutive groups of at most N; each group produces its own TextDocument aligned to the same TimeFrame and grounded to its own source TimePoints via ``origins``. This bounds GPU memory for long dynamic scenes. The value is operator-set, so the number of output TextDocuments is deterministic and does not vary by GPU. Composes with the number of prompts the backend runs together (``parallelPrompts`` in apps that offer it).
- `imagesPerPromptMode`: optional, defaults to `max`

    - Type: string
    - Multivalued: False
    - Choices: **_`max`_**, `balanced`


    > How the images of a TimeFrame that exceeds ``maxImagesPerPrompt`` are spread over its prompts. Has no effect when ``maxImagesPerPrompt`` is ``0``. Both choices produce the same number of prompts. "max" fills each prompt to the cap and puts the remainder in the last one (33 images at a cap of 32 give 32 and 1). "balanced" spreads the images evenly, so prompt sizes differ by at most one (33 images at a cap of 32 give 17 and 16).
- `model`: optional, defaults to `ggml-org/gemma-4-E4B-it-GGUF:Q8_0`

    - Type: string
    - Multivalued: False
    - Choices: `ggml-org/gemma-4-E2B-it-GGUF:Q8_0`, `ggml-org/gemma-4-E2B-it-GGUF:Q4_0`, `ggml-org/gemma-4-E2B-it-GGUF:BF16`, **_`ggml-org/gemma-4-E4B-it-GGUF:Q8_0`_**, `ggml-org/gemma-4-E4B-it-GGUF:Q4_0`, `ggml-org/gemma-4-E4B-it-GGUF:BF16`, `ggml-org/gemma-4-12B-it-GGUF:Q8_0`, `ggml-org/gemma-4-12B-it-GGUF:Q4_0`, `ggml-org/gemma-4-12B-it-GGUF:BF16`, `ggml-org/gemma-4-26B-A4B-it-GGUF:Q8_0`, `ggml-org/gemma-4-26B-A4B-it-GGUF:Q4_0`, `ggml-org/gemma-4-26B-A4B-it-GGUF:BF16`, `ggml-org/gemma-4-31B-it-GGUF:Q8_0`, `ggml-org/gemma-4-31B-it-GGUF:Q4_0`, `ggml-org/gemma-4-31B-it-GGUF:BF16`


    > Model to use for this request. Must be one of the model ids declared in this app's ``analyzer_versions``; the SDK pins the corresponding commit hash at load time. A model id is a Hugging Face repository, optionally followed by ``:<quantization>`` (e.g. ``org/repo-GGUF:Q8_0``). When the app ships a single model, this parameter defaults to it and can be omitted.
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
    - _origins_ = "*"
    - _origination_ = "derived"

    > Caption text generated by the Gemma 4 model for each prompt: one per processed TimeFrame, or several when `maxImagesPerPrompt` splits a TimeFrame. The `origins` property points to the `TimePoint`(s) anchoring the image(s) that caption was generated from.
- [http://clams.ai/vocabulary/type/Alignment/v1](http://clams.ai/vocabulary/type/Alignment/v1)
(of any properties)

    > Alignment between each parent TimeFrame and the TextDocument(s) derived from it.
- [http://clams.ai/vocabulary/type/TimePoint/v5](http://clams.ai/vocabulary/type/TimePoint/v5)
    - _timeUnit_ = "milliseconds"
    - _timePoint_ = "*"

    > Optional output. Newly-created TimePoint annotations for images sampled from a TimeFrame interval without an existing backing TimePoint (see `tfSamplingMode`).
