---
layout: posts
classes: wide
title: qwen35-timeframe-captioner
date: 1970-01-01T00:00:00+00:00
---
Applies a Qwen3.5 vision-language model to video frames selected by input TimeFrame annotations for prompt-driven captioning / scene description. Per-TimeFrame captioning is composite: every frame sampled from a TF is fed to the model in a single prompt and yields one caption per TF. A `model` runtime parameter selects the Qwen3.5 variant (default `Qwen/Qwen3.5-2B`); larger variants need substantially more VRAM (see metadata.py for the GPU/VRAM sketch). Qwen3.5 is a reasoning model -- this app runs it for captions and strips any `<think>` reasoning block from the output.
- [v0.1](v0.1) ([`@keighrim`](https://github.com/keighrim), 2026-07-10, [source](https://github.com/clamsproject/app-qwen35-timeframe-captioner/tree/v0.1)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-qwen35-timeframe-captioner/tree/v0.1" title="Copy source URL" aria-label="Copy source URL">📋</button>, [image](https://github.com/clamsproject/app-qwen35-timeframe-captioner/pkgs/container/app-qwen35-timeframe-captioner/v0.1)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-qwen35-timeframe-captioner:v0.1" title="Copy image tag" aria-label="Copy image tag">📋</button>)
