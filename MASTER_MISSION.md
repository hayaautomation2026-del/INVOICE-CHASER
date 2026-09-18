# PrivateDocs AI — Master Mission

## Status
FINAL / FROZEN. Execute this mission; do not rewrite, review, or expand it unless a real blocker requires changing the customer promise or V1 scope.

## Roles and source of truth
- **Astra:** primary builder. Own routine technical decisions and implementation.
- **GPT-5.6 Sol:** independent reviewer/gatekeeper using GitHub evidence.
- **User:** not a technical messenger between agents.
- **Repository:** `hayaautomation2026-del/INVOICE-CHASER`
- Workflow: **Astra builds → commits/pushes → Sol reviews → Astra fixes → Sol verifies → next stage.**

Use meaningful milestone commits. Code, tests, measurements, build evidence, license notes, and known failures belong in this repository.

## Product
Build **PrivateDocs AI V1**, a downloadable Windows desktop app:

**Download → Install → Open → Add PDF → Ask → Grounded answer + source/page → Summarize**

Core promises:
- local document processing and local AI inference;
- no OpenAI/Anthropic/Gemini or other external AI API required;
- no mandatory account/login;
- no API key;
- no Python/Git/Docker/terminal/developer setup for the customer;
- document contents must not be sent to external AI/cloud services.

## V1 scope
Implement:
1. Windows desktop app.
2. Drag/drop or file-picker PDF import.
3. Local, page-aware PDF text extraction where possible.
4. Local indexing/retrieval and local inference.
5. Local document library with persistence.
6. Chat over imported PDFs.
7. Grounded answers with source PDF and page reference where available.
8. Whole-document summarization.
9. Multi-PDF questions/search.
10. Delete one document and clear all local document/index data.
11. Graceful handling of scanned/image-only, encrypted/password-protected, damaged, or unreadable PDFs.
12. Distributable Windows installer/app with required local components appropriately packaged/provisioned.

OCR is not automatically V1 scope. If a scanned PDF has no extractable text and OCR is absent, detect it and show a clear message rather than producing unreliable answers.

## Stage 0 — capability gate
Before implementation:
- verify Astra can write to this repository;
- verify the repository is usable by Sol for independent review;
- verify a real Windows environment exists for installer/runtime testing;
- choose candidate model/runtime/dependencies only after checking commercial-use and redistribution terms.

Record unavailable capabilities honestly. If no material blocker exists, continue immediately to Stage 1 without routine user approval.

## Stage 1 — feasibility
Build the smallest CPU-first proof:

**PDF → extract pages/text → index → retrieve → local AI → grounded answer → source/page**

Record:
- LLM/model/version/size;
- embedding model/approach;
- retrieval/index approach;
- RAM and approximate CPU use;
- startup/model-load time;
- answer latency;
- disk requirements;
- GPU requirement, if any;
- network behavior;
- known limitations.

Test multiple:
- supported questions;
- clearly unsupported questions;
- plausible-but-unsupported questions;
- misleading-premise questions.

**Rule: relevance is not evidence.** Unsupported information must not be fabricated.

Also create an early basic Windows package sufficient to test:

**Install → Launch → Load local components → Local inference**

This is an early packaging-risk test, not the final UI.

Test normal text PDFs plus graceful detection/failure for scanned, encrypted, damaged, and unreadable PDFs.

Commit implementation, measurements, failures, packaging evidence, and test results. Mark Stage 1 ready for Sol review.

## Stage 2 — core engine
Productionize:
- ingestion and page-aware extraction;
- chunking;
- local embeddings/index;
- retrieval;
- local inference;
- evidence grounding;
- source/page citations;
- multi-document retrieval;
- whole-document summarization;
- unsupported-answer behavior;
- deletion/index cleanup;
- persistence and clear-all-data.

Add automated tests where practical and commit meaningful milestones.

### Whole-document summary requirement
Do not label a few retrieved chunks a whole-document summary. Test a multi-page PDF with important information near the beginning, middle, and end. The strategy and result must demonstrate adequate document coverage.

## Stage 3 — customer app
Build a simple nontechnical Windows UI:
- document library: add/view/select/delete/clear PDFs;
- chat: question → grounded answer → source/page;
- summarize action;
- understandable error messages, not stack traces.

Customer must not need terminal, code, manual dependencies, configuration files, API keys, or developer knowledge.

## Stage 4 — Windows packaging
Produce a distributable Windows build. Do not assume Python, AI runtimes, databases, Git, Docker, or developer libraries are preinstalled.

Record actual tested:
- installer/download and installed size;
- model size;
- first-run behavior;
- RAM/minimum and recommended hardware;
- disk requirement;
- CPU expectations;
- Windows versions actually tested.

Do not claim untested compatibility.

## Commercial distribution gate
Maintain a license inventory for material models, embedding models, runtimes, frameworks, and packaged dependencies:
- name/version/source;
- license;
- commercial-use status;
- redistribution status;
- required attribution/notices.

Do not knowingly ship components whose terms conflict with commercial distribution.

## Privacy verification
### Connected test
While networking is enabled, inspect outbound traffic during startup, PDF import, extraction, indexing, Q&A, and summarization. Document every outbound connection.

PDF contents, extracted text, remote embeddings of private content, retrieved context, document-derived prompts, and private document questions must not be transmitted to external AI/cloud services.

### Offline test
After required local components are provisioned, disconnect networking and verify:

**Open → Import → Index → Ask → Answer → Cite → Summarize**

Core operation must continue offline. Explicitly document any non-core networking requirement.

## Stage 5 — independent verification
Sol reviews actual repository evidence: architecture, source, commits, dependencies/models/licenses, tests, grounding, failure handling, persistence/deletion, build/installer configuration, privacy/network evidence, Windows evidence, and performance measurements.

Astra's own statement that something works is not independent verification. Fix defects found and push them for re-review.

## Release acceptance
Release candidate must demonstrate:
1. clean Windows install and launch;
2. normal PDF import;
3. correct retrieval and grounded answer;
4. correct source/page citation;
5. multiple unsupported/plausible-unsupported/misleading-premise tests without fabrication;
6. multi-PDF retrieval;
7. deletion removes a document from retrieval;
8. restart persistence;
9. clear-data behavior;
10. graceful scanned/encrypted/damaged PDF handling;
11. genuine whole-document summary coverage;
12. no external AI API credentials;
13. connected-network privacy inspection;
14. offline core workflow;
15. commercial license inventory/review;
16. clean-machine Windows test.

## Technical authority
Astra may independently choose desktop framework, PDF library, local LLM/quantization, embeddings, index/vector implementation, persistence, inference runtime, installer, and test framework.

Optimize in this order:

**Reliability → Privacy → Simple installation → CPU compatibility → Reasonable RAM → Reasonable package size**

Escalate only decisions materially changing product purpose, customer experience, privacy/local promise, commercial model, or major V1 scope.

## Out of scope
Do not add browser automation, customer-support agents, coding agents, predictive maintenance, computer vision, recommendation engines, online research agents, cloud document processing/collaboration, subscriptions, or unrelated AI features.

## Definition of done
Not done merely because code exists, a dev build runs, tests pass locally, or Astra says it works.

Done means the tested Windows customer path works:

**Download → Install → Open → Add PDF → Ask → Grounded answer + source/page → Summarize**

with:
- no API key or mandatory account;
- local document processing and local inference;
- connected privacy test passed;
- offline operation passed;
- commercial distribution check completed;
- Windows build tested;
- Sol independent review completed.

## Execution rule
Start at the first unfinished stage. Do not repeat this specification in chat. Do not ask the user to relay routine technical information. Read current repository state, execute the next unfinished work, commit evidence, and continue as far as the environment permits.