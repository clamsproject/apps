---
layout: posts
classes: wide
title: gemma4-timeframe-captioner
date: 1970-01-01T00:00:00+00:00
---
Applies a Gemma 4 vision-language model, run with llama.cpp from a GGUF file, to video frames selected by input TimeFrame annotations for prompt-driven captioning / scene description (experimental llama.cpp backend). Captioning is composite: the frames sampled from a TF are fed to the model in a single prompt and yield one caption. When `maxImagesPerPrompt` is set, a TF with more frames than the cap is split into several prompts and yields one caption per prompt, all aligned to that TF. A `model` runtime parameter selects the Gemma 4 size and quantization (default `ggml-org/gemma-4-E4B-it-GGUF:Q8_0`); see metadata.py for the GPU memory each needs. The app runs its own llama-server process and needs the `llama-server` executable (included in the container image).
- [v0.1](v0.1) ([`@keighrim`](https://github.com/keighrim), 2026-11-09, [source](https://github.com/clamsproject/app-gemma4-timeframe-captioner/tree/v0.1)<button class="copy-btn" data-clip="https://github.com/clamsproject/app-gemma4-timeframe-captioner/tree/v0.1" title="Copy source URL" aria-label="Copy source URL">📋</button>, [image](https://github.com/clamsproject/app-gemma4-timeframe-captioner/pkgs/container/app-gemma4-timeframe-captioner/v0.1)<button class="copy-btn" data-clip="ghcr.io/clamsproject/app-gemma4-timeframe-captioner:v0.1" title="Copy image tag" aria-label="Copy image tag">📋</button>)
