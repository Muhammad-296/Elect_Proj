# ⚡ CMOS Logic Analyzer

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="420" alt="CMOS Logic Analyzer"/>
</p>

<p align="center">
  <a href="#-key-features"><strong>Features</strong></a> •
  <a href="#-installation"><strong>Installation</strong></a> •
  <a href="#-usage"><strong>Usage</strong></a> •
  <a href="#-mathematical-foundations"><strong>Formulas</strong></a> •
  <a href="#-contributing"><strong>Contributing</strong></a> •
  <a href="#-license-(mit---full-text-included)"><strong>License</strong></a>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
</p>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Why use this project?](#-why-use-this-project)
- [Demo Output (Representative)](#-demo-output-representative)
- [Supported CMOS Technologies](#-supported-cmos-technologies)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
  - [Interactive CLI](#interactive-cli)
  - [Command-line Arguments](#command-line-arguments)
  - [Programmatic API](#programmatic-api)
  - [Configuration File (YAML)](#configuration-file-yaml)
- [Project Structure](#-project-structure)
- [Mathematical Foundations](#-mathematical-foundations)
- [Design & Implementation Notes](#-design--implementation-notes)
- [Examples & Typical Workflows](#-examples--typical-workflows)
- [Testing & CI](#-testing--ci)
- [Troubleshooting & FAQ](#-troubleshooting--faq)
- [Contributing](#-contributing)
- [Security & Responsible Disclosure](#-security--responsible-disclosure)
- [Roadmap](#-roadmap)
- [Changelog (high level)](#-changelog-high-level)
- [Author & Contacts](#-author--contacts)
- [License (MIT — full text included)](#-license-mit---full-text-included)
- [References & Acknowledgements](#-references--acknowledgements)

---

## 📖 Overview

CMOS Logic Analyzer is an extensible Python toolkit for analyzing, comparing, and optimizing CMOS logic implementations (principally NAND+NOT vs NOR+NOT). The tool provides:

- Exact propagation delay calculations (rise/fall) using long-channel MOSFET models.
- Area and switching power estimations with per-gate aggregation.
- Logic minimization (Quine–McCluskey) and K-map visualization (2–4 variables).
- Multi-input NAND/NOR support, body-effect modeling, and a recommendation engine based on multiple metrics.
- CLI, config-driven runs (YAML), and programmatic API for batch and research workflows.

This project is designed for education, early-stage VLSI architecture exploration, and research prototyping.

---

## ✨ Key Features

- Quine–McCluskey logic minimization + K-map visualizer (2–4 variables).
- Exact MOSFET-based delay calculations (rise/fall) and output bit-rate estimation.
- Area estimation using geometry-aware transistor sizing calculations.
- Switching & peak power estimation per gate and aggregated.
- Multi-input NAND/NOR modeling (n inputs), body effect and parasitic capacitance included.
- Side-by-side NAND+NOT vs NOR+NOT comparison and deterministic multi-criteria recommendation engine.
- YAML configuration, JSON export, programmatic API, and interactive CLI.

---

## ❓ Why use this project?

- Accurate: Uses transistor-level parameterized models (long-channel square-law) for delay.
- Comparative: Directly compares NAND-centric vs NOR-centric implementations to drive design choices.
- Reproducible: Config-driven runs and JSON exports allow reproducible experiments and automated sweeps.
- Educational: Useful for courses and labs to demonstrate transistor sizing, delay vs. area vs. power trade-offs.

---

## 🎬 Demo Output (Representative)

```text
════════════════════════════════════════════════════════════════════════
   🔬 CMOS LOGIC ANALYZER - EXACT DELAY & AREA CALCULATIONS
════════════════════════════════════════════════════════════════════════

✓ Technology: 0.35µm CMOS
✓ Function: F = A + B + C + D
✓ Analysis: NAND+NOT vs NOR+NOT

╔════════════════════════╦═══════════════╦═══════════════╗
║ Performance Metric     ║ NAND+NOT      ║ NOR+NOT       ║
╠════════════════════════╬═══════════════╬═══════════════╣
║ Total Delay (ns)       ║ 2.456         ║ 2.189  ✓      ║
║ Bit Rate (MHz)         ║ 407.18        ║ 456.82 ✓      ║
║ Total Area (μm²)       ║ 45.23         ║ 42.15  ✓      ║
║ Max Power (μW)         ║ 12.34         ║ 11.02  ✓      ║
║ Gate Count             ║ 6             ║ 5      ✓      ║
╚════════════════════════╩═══════════════╩═══════════════╝

🏆 RECOMMENDED DESIGN: NOR+NOT
   └─ Superior in all 5 optimization criteria
```

---

## 🔬 Supported CMOS Technologies (examples)

| Technology | Gate Oxide | Vth (±V) | µn (cm²/V·s) | µp (cm²/V·s) | Typical Use |
|:----------:|:----------:|:--------:|:------------:|:------------:|:-----------:|
| 1.0 µm     | 20 nm      | ±0.9     | 450          | 180          | Legacy / Teaching |
| 0.8 µm     | 16 nm      | ±0.8     | 460          | 185          | Moderate Performance |
| 0.6 µm     | 12 nm      | ±0.75    | 470          | 190          | Standard Logic |
| 0.5 µm     | 10 nm      | ±0.7     | 460          | 190          | High-Speed Logic |
| 0.35 µm    | 7 nm       | ±0.5     | 500          | 200          | Advanced VLSI/Research |

You can add or override technology parameters using the `constants.py` (or via `TechSpecs.from_dict(...)` API when available).

---

## 🚀 Installation

Requirements:
- Python 3.7+
- pip

Quick install (from GitHub):

```bash
git clone https://github.com/yourusername/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# (Recommended) create and activate virtual environment
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

Minimal runtime dependencies:
- colorama
- tabulate
- numpy
- pyyaml

Install minimal dependencies via pip:

```bash
pip install colorama tabulate numpy pyyaml
```

---

## 🧭 Quick Start

Run the interactive CLI:

```bash
python main.py
```

Run using a YAML configuration:

```bash
python main.py --config examples/config.yml
```

Run programmatically (example script):

```python
from cmos_logic_analyzer import Analyzer, TechSpecs

tech = TechSpecs.from_name("0.35um")
an = Analyzer(tech=tech, Wn=2.0, Ln=0.35, Wp=4.0, Lp=0.35)

res = an.analyze_sop(num_vars=4, minterms=[1,3,5,7,9,11,13,15])
print(res.summary_table())
```

---

## 🎮 Usage

### Interactive CLI

When you run `python main.py` the CLI will guide you through:

1. Selecting CMOS technology (preset or custom).
2. Entering transistor sizing (Wn, Ln, Wp, Lp) or using defaults.
3. Selecting logic mode (SOP/POS) and entering minterms/maxterms.
4. Displaying K-map (2–4 variables), minimized expression, NAND/NOR implementations, and metrics.

### Command-line Arguments

(Example; actual flags may vary — consult `main.py --help`)

```bash
python main.py --tech 0.35um --mode SOP --vars 4 --minterms 1,3,5,7,9,11,13,15 --output markdown
python main.py --config path/to/config.yaml
python main.py --json-out results.json
```

### Programmatic API

Primary classes:
- TechSpecs: load or create technology parameter sets.
- Analyzer: top-level orchestration (minimization, mapping, delay/area/power).
- Result (or AnalysisReport): structured output, exports (markdown/json), and helper visualizations.

Example:

```python
from cmos_logic_analyzer import Analyzer, TechSpecs

tech = TechSpecs.from_name("0.5um")
analyzer = Analyzer(tech=tech)

report = analyzer.analyze_pos(num_vars=3, maxterms=[0,2,5])
print(report.minimized_expression)
print(report.metrics)         # dict with delay, area, power
```

### Configuration File (YAML)

A sample `config.yml`:

```yaml
technology: "0.35um"
transistors:
  Wn: 2.0
  Ln: 0.35
  Wp: 4.0
  Lp: 0.35
logic:
  mode: "SOP"
  variables: 4
  minterms: [1,3,5,7,9,11,13,15]
output:
  format: "markdown"   # options: markdown, ascii, json
  save: "results.md"
```

Run:

```bash
python main.py --config config.yml
```

---

## 📂 Project Structure

```
cmos-logic-analyzer/
│
├── main.py                      # CLI entrypoint & runner
├── constants.py                 # Physical constants & tech specs
├── mosfet.py                    # MOSFET parameter calculations
├── logic_minimizer.py           # Quine–McCluskey & K-map engine
├── design_implementer.py        # NAND/NOR implementation generator
├── delay_calculator.py          # Exact delay formulas
├── performance_analyzer.py      # Area, power, bit rate analysis
├── comparator.py                # Compare & recommend designs
├── visualizer.py                # K-map, ASCII/Markdown tables & plots
├── examples/                     # Example configs and example runs
├── tests/                        # Unit tests
├── requirements.txt             # Python dependencies
├── README.md                    # This file (enhanced)
└── LICENSE                      # MIT license
```

---

## 🧮 Mathematical Foundations (selected / summary)

This section summarizes the principal formulas used in the analyzer. For full derivations, see the module docstrings in `delay_calculator.py`, `mosfet.py`.

NOT gate (simplified) — load & time constants:

```text
C_load = n(Cgd_p + Cgd_n) + Cdb_p + Cdb_n + Cgb_p

Z_NOT^- = Rn × C_load    where Rn = 1/(K_n × (VDD - Vth_n))
Z_NOT^+ = Rp × C_load    where Rp = 1/(K_p × (VDD - |Vth_p|))
```

NAND / NOR multi-input delay (abridged):

```text
Z_NAND^- = f(n, C_load^-, K_n, a)   # See delay_calculator.py
Z_NOR^+  = f(n, C_load^+, K_p, a)   # See delay_calculator.py
```

Area (per gate):

```text
Area_gate = n * Wn * (ln + 2*LDn) + Wp*(lp + 2*LDp)   # [μm^2]
```

Switching power (approx.):

```text
V_inss = (√K_n * Vth_n + √K_p * (VDD - Vth_p)) / (√K_n + √K_p)
P_max ≈ G * (K_n / 2) × (V_inss - Vth_n)^2 × VDD   # [μW]
```

The library computes rise/fall delays separately and aggregates them into a total propagation delay metric and derived bit-rate.

---

## 🔧 Design & Implementation Notes

- MOSFET modeling: Current implementation relies on long-channel square-law approximations. This makes the models reasonable for technologies >= ~0.35µm. For short-channel nodes (sub-0.18µm), accuracy degrades; BSIM or measured models are recommended.
- Capacitances: Intrinsic gate/drain/body capacitances are modeled and included in C_load. Interconnect capacitance is not modeled by default but can be provided by the user as an external C_load.
- Sizing: Default transistor sizing aims for logical effort balance, but the API allows full manual control over W/L to support design-space sweeps.
- Multi-criteria decision: Uses equal weights for area/speed/power/complexity by default; weights can be customized in configuration or API.

---

## 🛠 Examples & Typical Workflows

1. Quick evaluation (interactive):
   - Run `python main.py` -> choose tech 0.35um, SOP, 4 vars, enter minterms -> get summary & recommendation.

2. Single-run (config):
   - Create `config.yml` and run `python main.py --config config.yml` -> exports markdown report and JSON.

3. Batch sweep (programmatic):
   - Use the API to iterate over Wn/Wp pairs or tech choices and write CSV/JSON results for plotting trade-offs.

4. Research mode:
   - Call Analyzer directly in a Jupyter notebook; collect results for statistical analysis.

Example script for sweeping Wn:

```python
from cmos_logic_analyzer import Analyzer, TechSpecs
import json

tech = TechSpecs.from_name("0.35um")
results = []
for Wn in [1.0, 1.5, 2.0, 3.0]:
    an = Analyzer(tech=tech, Wn=Wn, Wp=2*Wn)
    r = an.analyze_sop(4, [1,3,5,7,9,11,13,15])
    results.append(r.metrics)

with open('sweep_results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

---

## ✅ Testing & CI

- Unit tests are stored under `tests/` and cover logic minimization, K-map generation, core delay equations, and API stability.
- Recommended test runner: `pytest`
- Example:

```bash
pip install -r requirements-dev.txt
pytest -q
```

- CI: Add GitHub Actions to run tests on push & PR. A sample workflow (`.github/workflows/ci.yml`) should:
  - Setup Python
  - Install deps
  - Run `pytest`
  - Run `flake8` or `pylint` (optional linting)

---

## ❓ Troubleshooting & FAQ

Q: Results seem unrealistic for modern nodes (e.g., 7nm)
- A: The models are long-channel. For sub-0.18µm, use BSIM or measured parameters. We plan to add BSIM support.

Q: Can I include wire/interconnect capacitance?
- A: Not by default. Add the expected downstream C_load value to the analyzer via the API or modify node capacitances directly.

Q: My K-map doesn't display for >4 variables
- A: K-map visualization intentionally limited to 2–4 variables. For larger variable counts, rely on the Quine–McCluskey minimizer (text/JSON outputs).

If you find any issue, please open an issue on the repository and include:
- Repro steps
- Config or CLI inputs
- Python version & `requirements.txt` output

---

## 🤝 Contributing

We welcome contributions!

Suggested workflow:
1. Fork the repo.
2. Create a branch (feature/xxx).
3. Add tests and documentation.
4. Open a focused pull request describing intent and impact.

Guidelines:
- Follow PEP 8 and type-hint where helpful.
- Include docstrings for new modules/functions.
- Add unit tests for new algorithms or bug fixes.
- Keep PRs focused and atomic.

Please sign the Contributor License Agreement (CLA) if required by the repository owner.

---

## 🔒 Security & Responsible Disclosure

If you discover a security issue:
- Do NOT post exploit details in public issues.
- Email the repository owner securely: muhammad.al.ajami.se@gmail.com
- Provide: affected versions, reproduction steps, and suggested mitigation if possible.

---

## 🚀 Roadmap

Planned features and improvements (priority order):

- [ ] BSIM-level short-channel modeling (improved delay accuracy for sub-0.18µm nodes)
- [ ] Interconnect-aware delay & parasitic RC modeling
- [ ] GUI for visualization and interactive K-map editing
- [ ] Graph export (Graphviz) for gate-netlist visualization
- [ ] Integration with SPICE netlists and simple SPICE-based verification
- [ ] Improved power models (statistical switching, leakage)

Contributions to accelerate any of these items are highly welcome.

---

## 📝 Changelog (high level)

- 2024-01-10 — Initial public release: core analysis, Quine–McCluskey minimizer, K-map (2–4 vars).
- 2024-06-15 — Added multi-input NAND/NOR delay formulas & area model refinements.
- 2024-11-05 — CLI improvements, YAML config support, JSON export.
- 2025-12-24 — README enhanced: full docs, more examples, and expanded troubleshooting.

(For detailed history, consult Git tags and commit messages.)

---

## 👨‍💻 Author & Contacts

Muhammad Abdulhamid — Digital Circuit Designer & VLSI Engineer  
- GitHub: [Muhammad-296](https://github.com/Muhammad-296)  
- LinkedIn: [muhammad-abdulhamid](https://www.linkedin.com/in/muhammad-abdulhamid/)  
- Email: muhammad.al.ajami.se@gmail.com

If you use this tool in research, please cite the repository and the modules you used.

---

## 📜 License (MIT — full text included)

Copyright (c) 2025 Muhammad Abdulhamid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 📚 References & Acknowledgements

- Weste & Harris — CMOS VLSI Design (4th ed.)
- Rabaey et al. — Digital Integrated Circuits
- Berkeley BSIM documentation
- MIT OpenCourseWare — VLSI Design
- Quine–McCluskey algorithm — [Wikipedia](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)

Thanks to early contributors and reviewers for feedback on delay formulas and test cases.

---

If this project helped you, please give it a ⭐ on GitHub and consider contributing!
