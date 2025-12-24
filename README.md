<div align="center">

# ⚡ CMOS Logic Analyzer

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="420" alt="CMOS Logic Analyzer"/>

<p>
  <a href="#-key-features"><strong>Features</strong></a> •
  <a href="#-installation"><strong>Installation</strong></a> •
  <a href="#-usage-guide"><strong>Usage</strong></a> •
  <a href="#-mathematical-foundations"><strong>Formulas</strong></a> •
  <a href="#-contributing"><strong>Contributing</strong></a> •
  <a href="#-license"><strong>License</strong></a>
</p>

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
</p>

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Demo Output](#-demo-output)
- [Supported CMOS Technologies](#-supported-cmos-technologies)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
  - [Interactive CLI](#interactive-cli)
  - [Programmatic API](#programmatic-api)
  - [Configuration File (YAML)](#configuration-file-yaml)
- [Project Structure](#-project-structure)
- [Mathematical Foundations](#-mathematical-foundations)
- [Design Optimization Strategy](#-design-optimization-strategy)
- [Examples & Typical Workflows](#-examples--typical-workflows)
- [Troubleshooting & FAQ](#-troubleshooting--faq)
- [Contributing](#-contributing)
- [Security & Responsible Disclosure](#-security--responsible-disclosure)
- [Changelog](#-changelog)
- [Author & Contacts](#-author--contacts)
- [License (MIT — full text inline)](#-license)
- [References](#-references)

---

## 📖 Overview

CMOS Logic Analyzer is an extensible Python-based toolkit to analyze, compare, and optimize CMOS logic circuit implementations (NAND+NOT vs NOR+NOT). It supports exact delay calculations using long-channel MOSFET models, area estimation, power analysis, Quine–McCluskey logic minimization, and K-map visualization (2–4 variables). Designed for education, research, and early-stage VLSI architecture exploration.

Key goals:
- Accuracy: Non-linear MOSFET-based delay formulas and parasitic capacitances.
- Comparability: Side-by-side metrics for rival implementations.
- Usability: Interactive CLI + programmatic API + configuration-driven runs.

---

## ✨ Key Features

- Logic minimization with Quine–McCluskey algorithm and K-map visualization (2–4 variables).
- Exact propagation delay computations (rise/fall) using square-law MOS model.
- Area estimation per-gate and total circuit area using geometry-aware formulas.
- Switching & maximum power estimation with per-gate aggregation.
- Multi-input NAND/NOR support (2..n inputs) and body-effect modeling.
- Side-by-side NAND+NOT vs NOR+NOT comparison and multi-criteria recommendation engine.
- Config file driven runs (YAML), programmatic API, and interactive CLI.

---

## 🎬 Demo Output (Representative)

```text
═══════════════════════════════════════════════════════════════════════
   🔬 CMOS LOGIC ANALYZER - EXACT DELAY & AREA CALCULATIONS
═══════════════════════════════════════════════════════════════════════

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

## 🔬 Supported CMOS Technologies

| Technology | Gate Oxide | Vth (±V) | µn (cm²/V·s) | µp (cm²/V·s) | Typical Use |
|:----------:|:----------:|:--------:|:------------:|:------------:|:-----------:|
| 1.0 µm     | 20 nm      | ±0.9     | 450          | 180          | Legacy / Teaching |
| 0.8 µm     | 16 nm      | ±0.8     | 460          | 185          | Moderate Performance |
| 0.6 µm     | 12 nm      | ±0.75    | 470          | 190          | Standard Logic |
| 0.5 µm     | 10 nm      | ±0.7     | 460          | 190          | High-Speed Logic |
| 0.35 µm    | 7 nm       | ±0.5     | 500          | 200          | Advanced VLSI/Research |

---

## 🚀 Installation

Requirements:
- Python 3.7+
- pip

Quick install:

```bash
# Clone repository
git clone https://github.com/yourusername/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# (Recommended) Virtual environment
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run example
python main.py
```

Minimal dependencies (example):
- colorama
- tabulate
- numpy
- pyyaml

Install example:
```bash
pip install colorama tabulate numpy pyyaml
```

---

## 🎮 Usage Guide

### Interactive CLI
Run:
```bash
python main.py
```

Typical interactive flow:
1. Select CMOS technology.
2. Enter transistor sizing (Wn, Ln, Wp, Lp).
3. Select logic input format (SOP/POS).
4. Enter variables and minterms/maxterms.
5. View K-map, minimized expression, NAND/NOR implementations, and side-by-side metrics.

### Programmatic API (example)
Example usage with the library API (pseudo / example):

```python
from cmos_logic_analyzer import Analyzer, TechSpecs

# Load technology
tech = TechSpecs.from_name("0.35um")

# Create analyzer instance
an = Analyzer(tech=tech, Wn=2.0, Ln=0.35, Wp=4.0, Lp=0.35)

# Analyze SOP function (4 variables)
result = an.analyze_sop(num_vars=4, minterms=[1,3,5,7,9,11,13,15])
print(result.summary_table())

# Access structured results
print(result.minimized_expression)   # e.g. "A + B + C + D"
print(result.kmap_ascii())
```

### Configuration File (YAML)
Example config.yml:

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
```

Run with config:
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
├── requirements.txt             # Python dependencies
├── README.md                    # This file (enhanced)
└── LICENSE                      # (kept for compatibility; full text included below)
```

---

## 🧮 Mathematical Foundations (selected)

NOT gate (simplified):

Cload (VBS = 0):
```text
Cload = n(Cgd_pc + Cgd_nt) + Cdb_pc + Cdb_nc + Cgb_pc
Z_NOT^- = Rn × Cload    where Rn = 1/(Kn × (VDD - Vth_n))
Z_NOT^+ = Rp × Cload    where Rp = 1/(Kp × (VDD - |Vth_p|))
```

NAND / NOR multi-input delay (abridged):
```text
Z_ND^- = (n × Cload^- × 10^6) / ((n^2 - 1)Kn × a) × [log terms...]
Z_NR^+ = (n × Cload^+ × 10^6) / ((n^2 - 1)Kp × a) × [log terms...]
```

Area (per gate):
```text
Area = n × Wn (ln + 2 × LDn) + Wp (lp + 2 × LDp)  [μm^2]
```

Power (approx. switching):
```text
V_inss = (√Kn × Vth_n + √Kp (VDD - Vth_p)) / (√Kn + √Kp)
P_max ≈ G × (Kn/2) × (V_inss - Vth_n)^2 × VDD  [μW]
```

For full derivations and variable definitions, consult module docstrings and the `delay_calculator.py` and `mosfet.py` sources.

---

## 🎯 Design Optimization Strategy

We use a weighted multi-criteria decision process:

- Area — 25%
- Speed — 25%
- Power — 25%
- Gate Count (complexity) — 25%

Scoring is simple, transparent, and deterministic; tie-breaking uses smaller total area.

Pseudocode:
```python
score_NAND = 0
score_NOR = 0
for metric in [area, speed, power, gates]:
    if nand_better(metric): score_NAND += 1
    elif nor_better(metric): score_NOR += 1
winner = nand if score_NAND > score_NOR else nor
if score_NAND == score_NOR:
    winner = design_with_smaller_area
```

---

## 🛠 Examples & Typical Workflows

1. Quick evaluation of SOP with default transistor sizes:
   - Run interactive CLI, input minterms, get immediate comparison.

2. Batch testing multiple functions:
   - Prepare multiple YAML config files and script runs in parallel or sequentially.

3. Research mode:
   - Use API to sweep Wn/Wp sizes or technology parameters and collect delay/area/power trade-offs.

Output export:
- Markdown tables (for README/notes).
- ASCII for terminal.
- JSON export (for automated post-processing).

---

## ❓ Troubleshooting & FAQ

Q: "Results look off for sub-0.18 µm technologies."
A: The current models use long-channel square-law assumptions; accuracy falls off for short-channel processes. Planned BSIM support will address this.

Q: "Can I include interconnect capacitance?"
A: Not yet by default. You can add a downstream C_load to the analyzer to approximate wiring effects. Interconnect-aware models are on the roadmap.

Q: "What if my function has >4 variables?"
A: K-map visualization is limited to 2–4 variables. The logic minimizer supports higher-variable minimization via Quine–McCluskey algorithm—expect no K-map.

If you find bugs, please open an issue on the repository with:
- Repro steps
- Config file or CLI inputs
- Version info (python --version, requirements list)

---

## 🤝 Contributing

We welcome contributions. Suggested workflow:
1. Fork the repo.
2. Create a feature branch (feature/xxx).
3. Add tests and documentation.
4. Open a pull request describing intent and impact.

Guidelines:
- Follow PEP 8.
- Include docstrings & type hints.
- Unit tests for new algorithms/features.
- Keep PRs focused and atomic.

Please review [CONTRIBUTING.md] if present, or use the checklist above.

---

## 🔒 Security & Responsible Disclosure

If you discover a security issue:
- Do not open a public issue with exploit details.
- Contact the repository owner via secure means (email: muhammad.al.ajami.se@gmail.com) with a clear disclosure and steps to reproduce.
- Provide affected versions and recommended mitigation steps.

---

## 📝 Changelog (high level)

- 2024-01-10 — Initial public release: core analysis, Quine–McCluskey minimizer, K-map (2–4 vars).
- 2024-06-15 — Added multi-input NAND/NOR delay formulas & area model refinements.
- 2024-11-05 — CLI improvements, YAML config support, JSON export.
- 2025-12-24 — README enhanced, inline license added, examples & troubleshooting.

(For detailed change history see Git tags and commit messages.)

---

## 👨‍💻 Author & Contacts

Muhammad Abdulhamid — Digital Circuit Designer & VLSI Engineer  
- GitHub: [Muhammad-296](https://github.com/Muhammad-296)  
- LinkedIn: [muhammad-abdulhamid](https://www.linkedin.com/in/muhammad-abdulhamid/)  
- Email: muhammad.al.ajami.se@gmail.com

If you use this project in research or a publication, please cite the repo and the relevant modules you used.

---

## 📜 License (MIT — full text included)

Copyright (c) 2024 Muhammad Abdulhamid

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

(Above license text is included inline in this README for convenience; a separate LICENSE file may also be present in the repository.)

---

## 📚 References

- Weste & Harris — CMOS VLSI Design (4th ed.)
- Rabaey et al. — Digital Integrated Circuits
- Berkeley BSIM documentation
- MIT OpenCourseWare — VLSI Design
- Quine–McCluskey algorithm — [Wikipedia](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)

---

<div align="center">
If this project helped you, please give it a ⭐ on GitHub and consider contributing!
</div>
