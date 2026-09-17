# Stage 0 evidence

- User authorized INVOICE-CHASER as the source of truth, overriding the initial repository name.
- GitHub metadata reported pull/push/admin capability; actual workflow commit d6078ad93ca3da11fabeb8004f66da0cf2884659 verified write access.
- Independent gpt-5.6-sol reviewer read the repository and workflow without builder mediation and independently confirmed successful run 35288228480.
- https://github.com/hayaautomation2026-del/INVOICE-CHASER/actions/runs/35288228480 ran successfully on windows-2022. This establishes real Windows automated execution, not clean consumer Windows acceptance or ordinary-PC benchmarks.
- Local authoring environment is Linux with Python 3.12. Native Windows tools are absent locally. Windows packaging and local inference execute through GitHub Actions.
- Initial selected model/runtime licensing: official Qwen2.5-1.5B-Instruct GGUF Apache-2.0; llama.cpp and llama-cpp-python MIT; pypdf BSD-3-Clause. Sparse TF-IDF embeddings are implemented in project code, with no external embedding model. Inventory below records remaining bundled-notice obligations.

Stage 0 is sufficient to attempt Stage 1. No release qualification is implied.
