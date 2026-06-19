---
layout: posts
classes: wide
title: "SmolVLM2 Captioner (v1.0)"
date: 2026-06-01T20:28:09+00:00
---
## About this version

- Submitter: [keighrim](https://github.com/keighrim)
- Submission Time: 2026-06-01T20:28:09+00:00
- Prebuilt Container Image: [ghcr.io/clamsproject/app-smolvlm2-captioner:v1.0](https://github.com/clamsproject/app-smolvlm2-captioner/pkgs/container/app-smolvlm2-captioner/v1.0)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-smolvlm2-captioner:v1.0" title="Copy image tag" aria-label="Copy image tag">&#128203;</button>
- Release Notes

    (no notes provided by the developer)

## About this app (See raw [metadata.json](metadata.json))

**Applies the SmolVLM2-2.2B-Instruct multimodal model to video frames selected by input TimeFrame annotations for prompt-driven captioning / scene description. Each invocation runs a single `prompt` against the TimeFrames selected by `tfLabels`; to apply different prompts to different label subsets (e.g. one prompt for slates, another for chyrons), run the app once per (`prompt`, `tfLabels`) combination. Per-TimeFrame captioning is composite: every frame sampled from a TF is fed to the model in a single prompt and yields one caption per TF. This app ships only the 2.2B-Instruct variant -- the largest and most general-purpose model in the SmolVLM2 family. The smaller (256M and 500M) SmolVLM2 releases are post-trained specifically for video-QA tasks and we do not expect them to generalize well, given their size.**

- App ID: [http://apps.clams.ai/smolvlm2-captioner/v1.0](http://apps.clams.ai/smolvlm2-captioner/v1.0)
- App License: Apache 2.0
- Source Repository: [https://github.com/clamsproject/app-smolvlm2-captioner](https://github.com/clamsproject/app-smolvlm2-captioner) ([source tree of the submitted version](https://github.com/clamsproject/app-smolvlm2-captioner/tree/v1.0)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-smolvlm2-captioner/tree/v1.0" title="Copy source URL" aria-label="Copy source URL">&#128203;</button>)
- Analyzer License: Apache 2.0


#### Inputs
(**Note**: "*" as a property value means that the property is required but can be any value.)

- [http://clams.ai/vocabulary/type/VideoDocument/v2](http://clams.ai/vocabulary/type/VideoDocument/v2) (required)
(of any properties)

- [http://clams.ai/vocabulary/type/TimeFrame/v6](http://clams.ai/vocabulary/type/TimeFrame/v6) (required)
    - _representatives_ = "?"
    - _label_ = "*"

    > Labeled TimeFrame annotations selecting which video segments to caption. Frame selection within each segment is controlled by the universal `tfSamplingMode` parameter (see SDK docs). When present, the `representatives` property is consumed for representative-based sampling modes. Filter by label with the `tfLabels` parameter.


#### Configurable Parameters
(**Note**: _Multivalued_ means the parameter can have one or more values.)

- `tfLabels`: optional, defaults to `[]`

    - Type: string
    - Multivalued: True


    > Label(s) of input TimeFrame annotations to caption. By default (`[]`), all TimeFrames are processed regardless of label. To restrict to specific labels, pass this parameter one or more times.
- `prompt`: optional, defaults to `You are looking at one or more frames sampled from a single segment of a news video. Describe what is shown, the purpose of this segment in the broader news video, and transcribe any visible text. Produce one consolidated caption across all provided frames.`

    - Type: string
    - Multivalued: True


    > User prompt(s) sent to the model. A single value runs as a one-shot generation. A multi-value list is interpreted as a multi-turn static prompt; see ``promptMode`` for how turns are assembled.
- `systemPrompt`: optional, defaults to `""`

    - Type: string
    - Multivalued: False


    > Optional system-role text prepended to the conversation. Empty by default.
- `promptMode`: optional, defaults to `turn-taking`

    - Type: string
    - Multivalued: False
    - Choices: `user-only`, **_`turn-taking`_**


    > How to interpret a multi-value ``prompt`` list. Has no effect when ``prompt`` has a single value. For semantics of each choice and worked examples, see https://clams.ai/clams-python/app-baseclasses.html#promptable-multiturn
- `maxNewTokens`: optional, defaults to `200`

    - Type: integer
    - Multivalued: False


    > Maximum number of new tokens generated per inference call. Forwarded to the backend's ``generate``-equivalent. Larger values grow the KV cache linearly and increase GPU memory usage; reduce if VRAM is constrained.
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
- `parallelPrompts`: optional, defaults to `1`

    - Type: integer
    - Multivalued: False


    > Number of independent prompts the app runs in parallel (stacks into a single forward pass). The *size* of each prompt (how many images, how long the system/user text is, etc.) is NOT regulated by this parameter; that is each app's responsibility. Prompt count and per-prompt content size combine multiplicatively for GPU memory, so the two can blow up together. Catastrophic example: ``tfSamplingMode=all`` on a TimeFrame without ``targets`` expands that TF into one image per native-FPS frame (300 images for a 10-second TF at 30fps); ``parallelPrompts=4`` then runs 4 such prompts in one forward pass (~1200 images), guaranteed OOM. Keep at ``1`` on memory-tight setups; raise only when per-prompt content is small and bounded.
- `model`: optional, defaults to `HuggingFaceTB/SmolVLM2-2.2B-Instruct`

    - Type: string
    - Multivalued: False
    - Choices: **_`HuggingFaceTB/SmolVLM2-2.2B-Instruct`_**


    > HuggingFace model identifier to use for this request. Must be one of the model ids declared in this app's ``analyzer_versions``; the SDK pins the corresponding commit hash at load time. When the app ships a single model (the typical case), this parameter defaults to that one model and can be omitted. Pass the full HF model id (e.g. ``org/repo-name``); URL-encoding the ``/`` is optional.
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

    > Caption text generated by the SmolVLM2 model for each processed image. The `origins` property points to the `TimePoint` anchoring the image (an existing TimePoint reused when one already backs the image, or a TimePoint newly created in this view when the image was sampled from a TimeFrame interval without a backing TimePoint).
- [http://clams.ai/vocabulary/type/Alignment/v1](http://clams.ai/vocabulary/type/Alignment/v1)
(of any properties)

    > Alignment between each parent TimeFrame and the TextDocument(s) derived from it.
- [http://clams.ai/vocabulary/type/TimePoint/v5](http://clams.ai/vocabulary/type/TimePoint/v5)
    - _timeUnit_ = "milliseconds"
    - _timePoint_ = "*"

    > Optional output. Newly-created TimePoint annotations for images that were sampled from a TimeFrame interval without an existing backing TimePoint (see `tfSamplingMode`). When every sampled image came from an existing TimePoint, no TimePoints are created
