<div align="center">

# ⚡ CMOS Logic Analyzer

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="420" alt="CMOS Logic Analyzer"/>

<p>
  <a href="#-key-features"><strong>Features</strong></a> •
  <a href="#-installation"><strong>Installation</strong></a> •
  <a href="#-usage-guide"><strong>Usage</strong></a> •
  <a href="#-mathematical-foundations"><strong>Formulas</strong></a> •
  <a href="#-contributing"><strong>Contributing</strong></a>
</p>

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/CMOS-Technology-9B59B6?style=for-the-badge" alt="CMOS">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
</p>

</div>

---

<!-- TABLE OF CONTENTS -->
## 📚 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Demo Output](#-demo-output)
- [Supported CMOS Technologies](#-supported-cmos-technologies)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Mathematical Foundations](#-mathematical-foundations)
- [Design Optimization Strategy](#-design-optimization-strategy)
- [Limitations & Assumptions](#-limitations--assumptions)
- [Planned Enhancements](#-planned-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author & Contacts](#-author--contacts)
- [References](#-references)

---

## 📖 Overview

A polished, extensible Python-based analyzer for CMOS logic circuits. It performs:
- Exact propagation delay calculations using non-linear MOSFET modelling,
- Area and power analysis (per-gate and aggregate),
- Logic minimization via Quine–McCluskey and K-map visualization,
- Side-by-side NAND+NOT and NOR+NOT implementation analysis and recommendations.

This README has been carefully refactored to be well-aligned, easy to scan, and to include practical usage examples and configuration snippets.

---

## ✨ Key Features

<div align="center">

<table>
<tr>
<td width="50%" valign="top">

### 🔧 Logic & Minimization
- Quine–McCluskey exact simplifier
- K-map visualization (2–4 variables)
- Prime implicant highlighting & colorized output
- SOP/POS support and don't-care terms

### ⚡ Precise Delay Analysis
- Non-linear MOSFET equations (long-channel, square-law)
- Separate rise/fall delays
- Multi-input gate support
- Body-effect & parasitic capacitance modelling

</td>
<td width="50%" valign="top">

### 📐 Area & Power
- Exact formula based gate area estimation
- Technology aware transistor sizing
- Switching voltage & maximum power estimation
- Multi-criteria design scoring (area, speed, power, complexity)

### 📊 Comparative Analysis
- Automatic NAND vs NOR comparison
- Tabulated metrics and recommended design
- Export-friendly ASCII/Markdown tables

</td>
</tr>
</table>

</div>

---

## 🎬 Demo Output

Below is a representative analyzer output for quick reference.

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

| Technology | Gate Oxide | Vth (±V) | μn (cm²/V·s) | μp (cm²/V·s) | Use Case |
|-----------:|:----------:|:--------:|:------------:|:------------:|:--------:|
| 1.0 µm     | 20 nm      | ±0.9     | 450          | 180          | Legacy / Education |
| 0.8 µm     | 16 nm      | ±0.8     | 460          | 185          | Moderate Performance |
| 0.6 µm     | 12 nm      | ±0.75    | 470          | 190          | Standard Logic |
| 0.5 µm     | 10 nm      | ±0.7     | 460          | 190          | High-Speed |
| 0.35 µm    | 7 nm       | ±0.5     | 500          | 200          | Advanced VLSI |

---

## 🚀 Installation

Quick install (recommended for evaluation):

```bash
# Clone
git clone https://github.com/yourusername/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# Install dependencies (example)
pip install -r requirements.txt

# Run
python main.py
```

Virtualenv workflow:

```bash
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows
pip install -r requirements.txt
python main.py
```

Requirements (example):
```text
colorama>=0.4.0
tabulate>=0.8.9
numpy>=1.18.0
```

---

## 🎮 Usage Guide

Interactive CLI:

```bash
python main.py
```

Example interactive flow (abbreviated):
1. Select technology (1–5)
2. Configure transistor sizing (Wn, Ln, Wp, Lp)
3. Enter logic (SOP minterms or POS maxterms)
4. Inspect side-by-side NAND/NOR analysis & recommendation

Programmatic API (example Python usage):

```python
from cmos_analyzer import Analyzer, TechSpecs

tech = TechSpecs.from_name("0.35um")
an = Analyzer(tech=tech, Wn=2.0, Ln=0.35, Wp=4.0, Lp=0.35)
result = an.analyze_sop(num_vars=4, minterms=[1,3,5,7,9,11,13,15])
print(result.summary_table())
```

Configuration file example (YAML):

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

## 📂 Project Structure

```
cmos-logic-analyzer/
│
├── main.py                      # CLI entrypoint
├── constants.py                 # Physical constants & tech specs
├── mosfet.py                    # MOSFET parameter calculations
├── logic_minimizer.py           # Quine-McCluskey & K-map engine
├── design_implementer.py        # NAND/NOR implementation generator
├── delay_calculator.py          # Exact delay formulas
├── performance_analyzer.py      # Area, power, bit rate analysis
├── comparator.py                # Compare & recommend designs
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── LICENSE                      # MIT License
```

---

## 🧮 Mathematical Foundations (selected)

NOT gate load (VBS = 0):

```text
Cload = n(Cgd_pc + Cgd_nt) + Cdb_pc + Cdb_nc + Cgb_pc

Z_NOT⁻ = Rn × Cload    where Rn = 1/(Kn×(VDD - Vth_n))
Z_NOT⁺ = Rp × Cload    where Rp = 1/(Kp×(VDD - |Vth_p|))
```

NAND falling edge (multi-input):

```text
Z_ND⁻ = (n × Cload⁻ × 10⁶) / ((n² - 1)Kn × a) × [ ... logs ... ]
```

NOR rising edge (multi-input):

```text
Z_NR⁺ = (n × Cload⁺ × 10⁶) / ((n² - 1)Kp × a) × [ ... logs ... ]
```

Area per gate:

```text
Area = n×Wn(ln + 2LDn) + Wp(lp + 2LDp)  [μm²]
```

Max power (approx):

```text
V_inss = (√Kn × Vth_n + √Kp(VDD - Vth_p)) / (√Kn + √Kp)
Pmax = G × (Kn/2) × (V_inss - Vth_n)² × VDD  [μW]
```

(See individual module docstrings for full derivations and variable definitions.)

---

## 🎯 Design Optimization Strategy

Multi-criteria scoring balances:
- Area (25%)
- Speed (25%)
- Power (25%)
- Gate Count (25%)

Example algorithm (pseudocode):

```python
score_NAND = 0
score_NOR = 0
for metric in [area, speed, power, gates]:
    if nand_better(metric): score_NAND += 1
    elif nor_better(metric): score_NOR += 1
winner = tie_break_by_smaller_area(score_NAND, score_NOR)
```

---

## ⚠️ Limitations & Assumptions

- Long-channel (square-law) MOSFET model (not BSIM)
- Fixed ambient temperature (T = 300 K)
- Default supply VDD = 5.0 V (configurable)
- Interconnect parasitics are omitted (no RLC on wires)
- Static CMOS only (no ratioed/dynamic gates)
- Single-stage gates (no internal cascoding or complex analog effects)

---

## 🚀 Planned Enhancements (roadmap)

- Deep-submicron & BSIM support (0.18 µm and below)
- Interconnect delay modelling
- Temperature & voltage scaling analysis
- Monte Carlo PVT variation studies
- GUI (web-based) and SPICE netlist export
- PDF/HTML report generation

---

## 🤝 Contributing

We welcome contributions — please follow these steps:

1. Fork the repository.
2. Create a feature branch: git checkout -b feature/awesome
3. Write tests & follow PEP 8.
4. Open a Pull Request describing your change.

Contribution checklist:
- Add docstrings & type hints
- Add unit tests for new features
- Update README and examples
- Keep commits logical and PR description clear

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines (if present).

---

## 📜 License

This project is released under the MIT License — see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author & Contacts

Muhammad Abdulhamid — Digital Circuit Designer & VLSI Engineer  
- GitHub: [Muhammad-296](https://github.com/Muhammad-296)  
- LinkedIn: [muhammad-abdulhamid](https://www.linkedin.com/in/muhammad-abdulhamid/)  
- Email: muhammad.al.ajami.se@gmail.com

---

## 📚 References

- Weste & Harris — CMOS VLSI Design
- Rabaey et al. — Digital Integrated Circuits
- Berkeley BSIM documentation
- MIT OpenCourseWare — VLSI Design
- Quine–McCluskey algorithm — [Wikipedia](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)

---

<div align="center">
If you find this project useful, please ⭐ the repository and consider contributing!
</div>
