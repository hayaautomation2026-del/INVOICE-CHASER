# PrivateDocs AI

Local Windows PDF question answering. This repository name is INVOICE-CHASER at the owner's explicit direction; the product is PrivateDocs AI.

**Status: Stage 1 feasibility implementation, not a completed product or release candidate.**

The prototype uses local Qwen2.5-1.5B-Instruct Q4_K_M, CPU-only llama.cpp through llama-cpp-python, pypdf, and local sparse TF-IDF retrieval. Answers are exact model-selected evidence quotes. Document/page references are assigned by code. Quote verification prevents invented quote text but does not prove semantic relevance; the independent grounding evaluation remains a release gate. Sparse retrieval may miss paraphrases and is subject to Stage 1 review.

## Build (developer only)

On Windows with Python 3.11 and C++ build tools: `pip install -r requirements-build.txt`, `python scripts/provision.py`, `python scripts/feasibility.py`. The workflow then packages the runtime/model into an installer using PyInstaller and Inno Setup. Customers will not install Python or use a terminal.

The build script obtains the official Qwen model, records the exact repository revision and verifies its SHA-256 against upstream LFS metadata. The application itself contains no download code or cloud AI fallback. Build-time networking is separate from customer inference. No API key is used.

## Stage gates

0. GitHub writes confirmed by d6078ad; independent Sol read access confirmed; Windows hosted CI run 35288228480 passed. Consumer Windows testing is still required before release.
1. PDF-to-local-answer prototype, evidence tests and early packaged inference. See Actions for actual results; no performance claim until measured.
2–5. Persistent library, deletion, full summaries, final UX, privacy inspection, clean consumer Windows acceptance and independent final review are pending.

Run `python -m unittest discover -s tests -v` for deterministic tests. These use a fake inference adapter and are NOT proof of real model answer quality. `scripts/feasibility.py` performs the real CPU-model evaluation separately.

No minimum consumer RAM, supported Windows editions, latency, or hallucination-free guarantee is claimed yet. Scanned PDFs require OCR outside V1. Page numbers mean physical PDF pages, starting at 1.
