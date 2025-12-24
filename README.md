<div align="center">

<!-- HERO / TITLE -->
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="460" alt="CMOS Logic Analyzer Animated"/>

<h1 align="center">⚡ CMOS Logic Analyzer</h1>

<p align="center">
  <strong>Advanced Circuit Design & Analysis — Exact Delay, Area & Power</strong>
</p>

<!-- SOCIAL BADGES -->
<p align="center">
  <a href="https://github.com/Muhammad-296" title="GitHub — Muhammad-296">
    <img src="https://img.shields.io/badge/GitHub-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/muhammad-abdulhamid/" title="LinkedIn — Muhammad Abdulhamid">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:muhammad.al.ajami.se@gmail.com" title="Email — muhammad.al.ajami.se@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836.svg?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="#-key-features" title="See Features">
    <img src="https://img.shields.io/badge/Explore-Features-00BFFF.svg?style=for-the-badge" alt="Explore Features">
  </a>
</p>

<!-- ANIMATED TAGLINE -->
<p align="center">
  <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" width="640" alt="animated-tagline"/>
</p>

</div>

---

<!-- TABLE OF CONTENTS -->
## 📚 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Demo Output](#-demo-output)
- [Technologies](#-supported-cmos-technologies)
- [Install & Quick Start](#-installation)
- [Usage Examples](#-usage-guide)
- [Project Structure](#-project-structure)
- [Formulas & Foundations](#-mathematical-foundations)
- [Optimization Strategy](#-design-optimization-strategy)
- [Limitations & Roadmap](#-limitations--assumptions)
- [Contributing](#-contributing)
- [License & Author](#-license--author)
- [References](#-references)

---

## 📖 Overview

A sleek, colored and interactive README for the CMOS Logic Analyzer — a Python toolkit for:
- Exact MOSFET-based delay analysis (rise/fall),
- Gate-area & power estimation,
- Logic minimization (Quine–McCluskey & K-maps),
- NAND+NOT vs NOR+NOT comparative optimization.

This README adds vivid badges, icons, and animated accents to present information clearly and attractively while remaining GitHub-friendly.

---

## ✨ Key Features

<div align="center">

<table>
<tr>
<td width="50%" valign="top">

<h3>🔧 Logic & Minimization</h3>
<ul>
  <li>Quine–McCluskey exact simplifier</li>
  <li>2–4 variable K-map visualizer (color-coded)</li>
  <li>SOP/POS input with don't-care support</li>
</ul>

<h3>⚡ Precise Delay Analysis</h3>
<ul>
  <li>Non-linear MOSFET long-channel equations</li>
  <li>Separate rise & fall delay computation</li>
  <li>Body-effect & parasitic capacitances considered</li>
</ul>

</td>
<td width="50%" valign="top">

<h3>📐 Area & Power</h3>
<ul>
  <li>Exact per-gate area formula</li>
  <li>Switching voltage & Pmax estimation</li>
  <li>Technology-aware transistor sizing</li>
</ul>

<h3>📊 Comparative Analysis</h3>
<ul>
  <li>Automatic NAND vs NOR side-by-side scores</li>
  <li>Multi-criteria optimization (area/speed/power/gates)</li>
  <li>Export-friendly ASCII / Markdown tables</li>
</ul>

</td>
</tr>
</table>

</div>

---

## 🎬 Demo Output (stylized)
<div align="center">
<img src="https://img.shields.io/badge/Demo-Output-FF7F50?style=for-the-badge" alt="Demo">
</div>

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

<p align="center">
  <img src="https://img.shields.io/badge/1.0µm-Legacy-8B8B8B?style=for-the-badge" alt="1.0um">
  <img src="https://img.shields.io/badge/0.8µm-Moderate-6A5ACD?style=for-the-badge" alt="0.8um">
  <img src="https://img.shields.io/badge/0.6µm-Standard-20B2AA?style=for-the-badge" alt="0.6um">
  <img src="https://img.shields.io/badge/0.5µm-HighSpeed-FFB400?style=for-the-badge" alt="0.5um">
  <img src="https://img.shields.io/badge/0.35µm-Advanced-00C853?style=for-the-badge" alt="0.35um">
</p>

---

## 🚀 Installation (Quick & Colorful)

```bash
# Clone the repo
git clone https://github.com/yourusername/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# Install deps
python -m pip install -r requirements.txt

# Run the analyzer
python main.py
```

Requirements example:
- colorama
- tabulate
- numpy

---

## 🎮 Usage Guide

Interactive CLI:
```bash
python main.py
```

Programmatic example (Python API):
```python
from cmos_analyzer import Analyzer, TechSpecs
tech = TechSpecs.from_name("0.35um")
an = Analyzer(tech=tech, Wn=2.0, Ln=0.35, Wp=4.0, Lp=0.35)
result = an.analyze_sop(num_vars=4, minterms=[1,3,5,7,9,11,13,15])
print(result.summary_table())
```

YAML config example:
```yaml
technology: 0.35um
transistors:
  Wn: 2.0
  Ln: 0.35
  Wp: 4.0
  Lp: 0.35
logic:
  mode: SOP
  variables: 4
  minterms: [1,3,5,7,9,11,13,15]
```

---

## 📂 Project Structure (visually aligned)

```
cmos-logic-analyzer/
│
├── main.py
├── constants.py
├── mosfet.py
├── logic_minimizer.py
├── design_implementer.py
├── delay_calculator.py
├── performance_analyzer.py
├── comparator.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧮 Mathematical Foundations (compact & color-coded)

- NOT gate load & delays:
  - Cload formulas & Z_NOT rise/fall expressions.
- NAND / NOR multi-input delay integrals (see delay_calculator.py).
- Area per gate:
  - Area = n*Wn(ln + 2LDn) + Wp(lp + 2LDp)
- Maximum power:
  - Pmax = G × (Kn/2) × (V_inss - Vth_n)^2 × VDD

For derivations, examine module docstrings and comments.

---

## 🎯 Optimization Strategy

We apply a 4-criterion equal-weight scoring:
- Area (25%), Speed (25%), Power (25%), Gate Count (25%).
Tie-breaker: smaller area wins.

---

## ⚠️ Limitations & Assumptions

- Square-law (long-channel) MOSFET model.
- Fixed default VDD = 5.0 V (configurable).
- Temperature fixed at 300K unless user changes constants.
- Interconnect parasitics omitted.
- Static CMOS gates only; single-stage gates.

---

## 🛣️ Roadmap (Planned Enhancements)

- BSIM4/BSIM6 support for deep-submicron.
- Interconnect & temperature-aware analysis.
- Monte Carlo PVT variation studies.
- Web GUI + SPICE netlist export.
- PDF/HTML report generator.

---

## 🤝 Contributing

We welcome improvements! Please:
1. Fork the repo
2. Create a feature branch
3. Add tests & documentation
4. Raise a PR with a clear description

Conventions:
- PEP8, type hints, docstrings, unit tests for new features.

---

## 📜 License & Author

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

**Author:** Muhammad Abdulhamid — Digital Circuit Designer & VLSI Engineer  
- GitHub: [Muhammad-296](https://github.com/Muhammad-296)  
- LinkedIn: [muhammad-abdulhamid](https://www.linkedin.com/in/muhammad-abdulhamid/)  
- Email: <a href="mailto:muhammad.al.ajami.se@gmail.com">muhammad.al.ajami.se@gmail.com</a>

---

## 📚 References

- Weste & Harris — CMOS VLSI Design  
- Rabaey et al. — Digital Integrated Circuits  
- Berkeley BSIM documentation  
- MIT OpenCourseWare — VLSI Design  
- Quine–McCluskey — https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm

---

<div align="center">
  <p>
    If this project helped you, please <strong>⭐ Star</strong> the repo and consider contributing!
  </p>
  <p>
    <a href="https://github.com/Muhammad-296"><img src="https://img.shields.io/badge/Star-This%20Repo-FF69B4?style=for-the-badge" alt="Star"></a>
    <a href="https://github.com/yourusername/cmos-logic-analyzer/releases"><img src="https://img.shields.io/badge/Release-v1.0.0-00C853?style=for-the-badge" alt="Release"></a>
  </p>
</div>
