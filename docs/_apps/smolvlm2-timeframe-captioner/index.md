---
layout: posts
classes: wide
title: smolvlm2-timeframe-captioner
date: 1970-01-01T00:00:00+00:00
---
Applies the SmolVLM2-2.2B-Instruct multimodal model to video frames selected by input TimeFrame annotations for prompt-driven captioning / scene description. Each invocation runs a single `prompt` against the TimeFrames selected by `tfLabels`; to apply different prompts to different label subsets (e.g. one prompt for slates, another for chyrons), run the app once per (`prompt`, `tfLabels`) combination. Per-TimeFrame captioning is composite: every frame sampled from a TF is fed to the model in a single prompt and yields one caption per TF. This app ships only the 2.2B-Instruct variant -- the largest and most general-purpose model in the SmolVLM2 family. The smaller (256M and 500M) SmolVLM2 releases are post-trained specifically for video-QA tasks and we do not expect them to generalize well, given their size.
- [v1.0](v1.0) ([`@keighrim`](https://github.com/keighrim))
