---
layout: posts
classes: wide
title: doctr-wrapper
---
CLAMS app wraps the [docTR, End-to-End OCR model](https://pypi.org/project/python-doctr). The model can detect text regions in the input image and recognize text in the regions (via parseq OCR model, only English is support at the moment). The text-localized regions are organized hierarchically by the model into "pages" > "blocks" > "lines" > "words", and this CLAMS app translates them into `TextDocument`, `Paragraphs`, `Sentence`, and `Token` annotations to represent recognized text contents. See descriptions for I/O types below  for details on how annotations are aligned to each other.
- [v1.2](v1.2) ([`@keighrim`](https://github.com/keighrim))
- [v1.1](v1.1) ([`@keighrim`](https://github.com/keighrim))
- [v1.0](v1.0) ([`@keighrim`](https://github.com/keighrim))
