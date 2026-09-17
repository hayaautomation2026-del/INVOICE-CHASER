# Initial license inventory — release audit still required

| Component | Version | License/source | Distribution conditions |
|---|---|---|---|
| Qwen2.5-1.5B-Instruct-GGUF Q4_K_M | exact revision recorded by provision.py | Apache-2.0, https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF | Commercial redistribution permitted subject to license/notice requirements; model license bundled |
| llama-cpp-python | 0.3.16 | MIT, https://github.com/abetlen/llama-cpp-python/blob/main/LICENSE.md | Retain copyright and license |
| llama.cpp | bundled by binding version | MIT, https://github.com/ggml-org/llama.cpp/blob/master/LICENSE | Retain copyright and license; record exact bundled revision before release |
| pypdf | 5.9.0 | BSD-3-Clause, https://github.com/py-pdf/pypdf/blob/main/LICENSE | Retain notices/disclaimer; no endorsement |
| Python / Tk | Python 3.11 build environment | PSF / Tcl-Tk licenses, https://docs.python.org/3/license.html | Preserve applicable notices with runtime |
| PyInstaller | 6.16.0 | GPL with distribution exception, https://pyinstaller.org/en/stable/license.html | Commercial application bundles permitted by exception; preserve notices |
| Inno Setup | runner-provided version, must record | https://jrsoftware.org/files/is/license.txt | Review exact installed version and retain notices before release |
| reportlab | 4.4.4 | BSD, build/test fixture generation only | Not deliberately included in customer application |
| psutil | 7.0.0 | BSD, measurement only | Not deliberately included in customer application |

Initial upstream model/runtime license checks support feasibility. This file is not a claim that the final packaged transitive-dependency inventory or notices audit is complete. Release must inspect actual bundled files, versions and licenses. Prototype artifacts are internal test builds, not approved commercial distribution.
