<div align="center">

# ⚡ CMOS Logic Analyzer

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="400">

### 🔬 Advanced Circuit Design & Analysis Tool

<p>
  <strong>Exact Delay Calculation</strong> • 
  <strong>Area Optimization</strong> • 
  <strong>Power Analysis</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/CMOS-Technology-9B59B6?style=for-the-badge" alt="CMOS">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
</p>

<p>
  <a href="#-key-features"><strong>Features</strong></a> •
  <a href="#-installation"><strong>Installation</strong></a> •
  <a href="#-usage-guide"><strong>Usage</strong></a> •
  <a href="#-mathematical-foundations"><strong>Formulas</strong></a> •
  <a href="#-contributing"><strong>Contributing</strong></a>
</p>

---

</div>

## 📖 Overview

A **comprehensive Python-based tool** for analyzing and optimizing CMOS logic circuits. This analyzer implements **exact delay calculations**, area optimization, and power analysis for digital logic designs using both **NAND+NOT** and **NOR+NOT** implementations.

<div align="center">


---

## ✨ Key Features

<div align="center">

<table>
<tr>
<td width="50%" valign="top">

<h3 align="center">🔧 Logic Minimization</h3>

<ul align="left">
<li>🚀 <strong>Quine-McCluskey Algorithm</strong> for exact simplification</li>
<li>🧩 Boolean function reduction</li>
<li>🎨 <strong>K-map Visualization</strong> (2-4 variables)</li>
<li>🔹 Prime implicant grouping</li>
<li>🌈 Color-coded analysis outputs</li>
</ul>

<h3 align="center">⚡ Precise Delay Analysis</h3>

<ul align="left">
<li>⚡ <strong>Non-linear MOSFET equations</strong></li>
<li>⏱️ Exact propagation delay measurement</li>
<li>🔺 Separate <strong>rise/fall</strong> delays</li>
<li>🧪 Advanced capacitance modeling</li>
<li>🔗 Multi-input gate support</li>
</ul>

<h3 align="center">📐 Area Optimization</h3>

<ul align="left">
<li>📏 <strong>Exact area formula</strong> implementation</li>
<li>🏭 Technology-dependent parameters</li>
<li>🔍 Gate-level footprint breakdown</li>
<li>💾 Silicon area minimization</li>
</ul>

</td>
<td width="50%" valign="top">

<h3 align="center">🔋 Power Analysis</h3>

<ul align="left">
<li>⚡ <strong>Maximum power dissipation</strong> estimation</li>
<li>🔌 Switching voltage calculation</li>
<li>🧮 Dynamic power breakdown</li>
<li>🌱 Energy-efficient recommendations</li>
</ul>

<h3 align="center">🎨 Interactive K-Maps</h3>

<ul align="left">
<li>🌈 <strong>Color-coded groupings</strong></li>
<li>🔹 Prime implicant highlighting</li>
<li>📊 ASCII & visual display</li>
<li>🖱️ Intuitive exploration</li>
</ul>

<h3 align="center">📊 Comparative Analysis</h3>

<ul align="left">
<li>⚔️ <strong>NAND vs NOR</strong> comparison</li>
<li>📈 Multi-criteria optimization</li>
<li>🖥️ Side-by-side metrics</li>
<li>🤖 Smart recommendations</li>
<li>📑 Detailed comparison tables</li>
</ul>

</td>
</tr>
</table>

</div>

---

## 🎬 Demo Output

<div align="center">

```
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

Key Advantages:
  • 12.2% faster operation
  • 6.8% smaller silicon area
  • 10.7% lower power consumption
  • 1 fewer gate required
```

</div>

---

## 🔬 Supported CMOS Technologies

<div align="center">

<table>
<thead>
<tr>
<th align="center">Technology</th>
<th align="center">Gate Oxide</th>
<th align="center">V<sub>th</sub> (V)</th>
<th align="center">μ<sub>n</sub> (cm²/V·s)</th>
<th align="center">μ<sub>p</sub> (cm²/V·s)</th>
<th align="center">Applications</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><strong>1.0µm</strong></td>
<td align="center">20 nm</td>
<td align="center">±0.9</td>
<td align="center">450</td>
<td align="center">180</td>
<td align="center">🎓 Legacy & Education</td>
</tr>
<tr>
<td align="center"><strong>0.8µm</strong></td>
<td align="center">16 nm</td>
<td align="center">±0.8</td>
<td align="center">460</td>
<td align="center">185</td>
<td align="center">🔧 Moderate Performance</td>
</tr>
<tr>
<td align="center"><strong>0.6µm</strong></td>
<td align="center">12 nm</td>
<td align="center">±0.75</td>
<td align="center">470</td>
<td align="center">190</td>
<td align="center">⚙️ Standard Logic</td>
</tr>
<tr>
<td align="center"><strong>0.5µm</strong></td>
<td align="center">10 nm</td>
<td align="center">±0.7</td>
<td align="center">460</td>
<td align="center">190</td>
<td align="center">🚀 High-Speed Circuits</td>
</tr>
<tr>
<td align="center"><strong>0.35µm</strong></td>
<td align="center">7 nm</td>
<td align="center">±0.5</td>
<td align="center">500</td>
<td align="center">200</td>
<td align="center">💎 Advanced VLSI</td>
</tr>
</tbody>
</table>

</div>

---

## 🚀 Installation

<div align="center">

### 📋 Prerequisites

</div>

```bash
✓ Python 3.7 or higher
✓ pip package manager
```

<div align="center">

### ⚡ Quick Start

</div>

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# 2️⃣ Install dependencies
pip install colorama tabulate

# 3️⃣ Run the analyzer
python main.py
```

<div align="center">

### 🔧 Advanced Installation (Virtual Environment)

</div>

```bash
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Unix/MacOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch application
python main.py
```

---

## 📂 Project Structure

```
cmos-logic-analyzer/
│
├── 📄 main.py                      # Application entry point & CLI
├── 📄 constants.py                 # Physical constants & CMOS datasheets
├── 📄 mosfet.py                    # MOSFET parameter calculations
├── 📄 logic_minimizer.py           # Quine-McCluskey & K-map engine
├── 📄 design_implementer.py        # NAND/NOR gate implementations
├── 📄 delay_calculator.py          # Exact delay formulas
├── 📄 performance_analyzer.py      # Area, power, bit rate analysis
├── 📄 comparator.py                # Design comparison & optimization
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # Documentation
└── 📄 LICENSE                      # MIT License
```

<details>
<summary><strong>📦 Detailed Module Descriptions</strong> (Click to expand)</summary>

<br>

<div align="center">

| Module | Description |
|--------|-------------|
| `main.py` | Interactive CLI with colorful output using colorama |
| `constants.py` | Physical constants (q, ε₀, εsi) and 5 CMOS technology datasheets |
| `mosfet.py` | Calculates Cox, Kn, Kp, Vth, and all parasitic capacitances |
| `logic_minimizer.py` | Implements Quine-McCluskey algorithm with K-map visualization |
| `design_implementer.py` | Converts SOP to NAND+NOT and NOR+NOT gate implementations |
| `delay_calculator.py` | Exact delay formulas for NOT, NAND, and NOR gates |
| `performance_analyzer.py` | Calculates area, power dissipation, and maximum bit rate |
| `comparator.py` | Compares both designs and recommends optimal implementation |

</div>

</details>

---

## 💡 Usage Guide

<div align="center">

### 🎮 Interactive Mode

</div>

```bash
python main.py
```

<details>
<summary><strong>📸 Complete Step-by-Step Tutorial</strong> (Click to expand)</summary>

<br>

#### **Step 1: Select CMOS Technology**

```
╔════════════════════════════════════════════════════════════╗
║           Available CMOS Technologies                      ║
╚════════════════════════════════════════════════════════════╝

1. 1.0µm CMOS  - Legacy systems & education
2. 0.8µm CMOS  - Moderate performance
3. 0.6µm CMOS  - Standard digital logic
4. 0.5µm CMOS  - High-speed circuits
5. 0.35µm CMOS - Advanced VLSI

Select technology number: 5
```

#### **Step 2: Configure MOSFET Dimensions**

```
╔════════════════════════════════════════════════════════════╗
║           Transistor Dimension Configuration               ║
╚════════════════════════════════════════════════════════════╝

Enter NMOS width Wn (µm): 2.0
Enter NMOS length Ln (µm): 0.35
Enter PMOS width Wp (µm): 4.0
Enter PMOS length Lp (µm): 0.35
Enter body-source voltage VBS (V): 0
```

#### **Step 3: Define Logic Function**

```
╔════════════════════════════════════════════════════════════╗
║           Logic Function Input                             ║
╚════════════════════════════════════════════════════════════╝

Use SOP (minterms) or POS (maxterms)? [S/P]: S
Enter number of variables (2-4): 4
Enter minterms separated by commas: 1,3,5,7,9,11,13,15
Enter don't care terms (optional): 
```

#### **Step 4: View Comprehensive Results**

The analyzer provides:
- ✅ Minimized logic expression
- ✅ Color-coded K-map visualization
- ✅ NAND+NOT implementation details
- ✅ NOR+NOT implementation details
- ✅ Side-by-side performance comparison
- ✅ Optimization analysis
- ✅ **Intelligent design recommendation**

</details>

---

## 🧮 Mathematical Foundations

<div align="center">

### Core Formulas Used in Analysis

</div>

<details>
<summary><strong>📊 NOT Gate Delay Equations</strong> (Click to expand)</summary>

<br>

**Load Capacitance (V<sub>BS</sub> ≠ 0):**

```
Cload = n(Cgd_pc + Cgd_nt + Cdb_pt) + Cdb_nc + Cgb_pc
```

**Load Capacitance (V<sub>BS</sub> = 0):**

```
Cload = n(Cgd_pc + Cgd_nt) + Cdb_pc + Cdb_nc + Cgb_pc
```

**Propagation Delays:**

```
Z_NOT⁻ = Rn × Cload    where Rn = 1/(Kn×(VDD - Vth_n))
Z_NOT⁺ = Rp × Cload    where Rp = 1/(Kp×(VDD - |Vth_p|))
```

</details>

<details>
<summary><strong>⚡ NAND Gate Delay Equations</strong> (Click to expand)</summary>

<br>

**Key Parameters:**

```
a = VDD - Vth_n
X₁ = a(1 - √(1/n))
X₂ = a(1 - √(1/n [1 + (1 - Vth_n/a)²(n-1)]))
```

**Falling Edge Delay:**

```
Z_ND⁻ = (n × Cload⁻ × 10⁶) / ((n² - 1)Kn × a) × 
        [(n-1)ln((a - X₂/2)/(a - X₁/2)) + 
         2ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) + 
         (n+1)ln(X₁/X₂)]
```

**Rising Edge Delay:**

```
Z_ND⁺ = NOT gate rise delay
```

</details>

<details>
<summary><strong>🔄 NOR Gate Delay Equations</strong> (Click to expand)</summary>

<br>

**Key Parameters:**

```
a = VDD - |Vth_p|
X₁ = a(1 - √(1/n))
X₂ = a(1 - √(1/n [1 + (1 - Vth_p/a)²(n-1)]))
```

**Rising Edge Delay:**

```
Z_NR⁺ = (n × Cload⁺ × 10⁶) / ((n² - 1)Kp × a) × 
        [(n-1)ln((a - X₂/2)/(a - X₁/2)) + 
         2ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) + 
         (n+1)ln(X₁/X₂)]
```

**Falling Edge Delay:**

```
Z_NR⁻ = NOT gate fall delay
```

</details>

<details>
<summary><strong>📐 Area Calculation Formula</strong> (Click to expand)</summary>

<br>

**Per-Gate Area:**

```
Area = n×Wn(ln + 2LDn) + wp(lp + 2LDp) [μm²]

where:
  n   = number of inputs
  Wn  = NMOS width per transistor
  ln  = NMOS channel length
  LDn = NMOS lateral diffusion length
  wp  = PMOS width per transistor
  lp  = PMOS channel length
  LDp = PMOS lateral diffusion length
```

</details>

<details>
<summary><strong>🔋 Power Dissipation Formula</strong> (Click to expand)</summary>

<br>

**Input Switching Voltage:**

```
V_inss = (√Kn × Vth_n + √Kp(VDD - Vth_p)) / (√Kn + √Kp)
```

**Maximum Power Dissipation:**

```
Pmax = G × (Kn/2) × (V_inss - Vth_n)² × VDD [μW]

where:
  G = total number of gates
```

</details>

---

## 🎯 Design Optimization Strategy

<div align="center">

<table>
<thead>
<tr>
<th align="center">Criterion</th>
<th align="center">Description</th>
<th align="center">Unit</th>
<th align="center">Weight</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">🏆 <strong>Area</strong></td>
<td align="center">Silicon real estate minimization</td>
<td align="center">μm²</td>
<td align="center">25%</td>
</tr>
<tr>
<td align="center">⚡ <strong>Speed</strong></td>
<td align="center">Operating frequency maximization</td>
<td align="center">MHz</td>
<td align="center">25%</td>
</tr>
<tr>
<td align="center">🔋 <strong>Power</strong></td>
<td align="center">Energy consumption minimization</td>
<td align="center">μW</td>
<td align="center">25%</td>
</tr>
<tr>
<td align="center">🎚️ <strong>Gates</strong></td>
<td align="center">Circuit complexity reduction</td>
<td align="center">Count</td>
<td align="center">25%</td>
</tr>
</tbody>
</table>

### 📈 Optimization Algorithm

```python
# Multi-criteria scoring system
score_NAND = 0
score_NOR = 0

for criterion in [area, speed, power, gates]:
    if NAND_design is_better_than NOR_design:
        score_NAND += 1
    elif NOR_design is_better_than NAND_design:
        score_NOR += 1

# Winner determination with tie-breaker
if score_NAND == score_NOR:
    winner = design_with_smaller_area
else:
    winner = design_with_higher_score
```

</div>

---

## 🔍 Technical Highlights

<div align="center">

### 💎 Advanced Engineering Features

<table>
<tr>
<td align="center" width="50%">

**Accuracy Features**
- ✅ Non-linear delay models
- ✅ Body effect consideration
- ✅ Separate cutoff/triode capacitances
- ✅ Complete load calculation

</td>
<td align="center" width="50%">

**Scalability Features**
- ✅ Multi-input gate support (2-n inputs)
- ✅ Technology scaling (1.0µm - 0.35µm)
- ✅ Exact mathematical formulas
- ✅ Industry-standard parameters

</td>
</tr>
</table>

</div>

---

## ⚠️ Limitations & Assumptions

<div align="center">

<table>
<thead>
<tr>
<th align="center">Category</th>
<th align="left">Assumption</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">⚙️</td>
<td><strong>Switching:</strong> Ideal transitions, no noise or signal integrity issues</td>
</tr>
<tr>
<td align="center">🌡️</td>
<td><strong>Temperature:</strong> Room temperature operation (T = 300K)</td>
</tr>
<tr>
<td align="center">⚡</td>
<td><strong>Supply:</strong> Fixed V<sub>DD</sub> = 5.0V</td>
</tr>
<tr>
<td align="center">🔌</td>
<td><strong>Interconnects:</strong> Wiring parasitics neglected</td>
</tr>
<tr>
<td align="center">📐</td>
<td><strong>Model:</strong> Square-law (long-channel approximation)</td>
</tr>
<tr>
<td align="center">🎚️</td>
<td><strong>Stages:</strong> Single-stage gates only</td>
</tr>
<tr>
<td align="center">📊</td>
<td><strong>Logic:</strong> Static CMOS only (no dynamic/ratioed)</td>
</tr>
</tbody>
</table>

### 🚀 Planned Enhancements

</div>

<table>
<tr>
<td width="33%" valign="top" align="center">

**🔬 Advanced Models**
- Deep submicron (<0.18µm)
- BSIM4/BSIM6 models
- Short-channel effects
- Process variations

</td>
<td width="33%" valign="top" align="center">

**📊 Analysis**
- Interconnect delays
- Temperature effects
- Voltage variations
- Monte Carlo analysis

</td>
<td width="33%" valign="top" align="center">

**💻 Features**
- Web GUI interface
- SPICE netlist export
- PDF report generation
- Multi-level optimization

</td>
</tr>
</table>

---

## 🤝 Contributing

<div align="center">

### 🌟 We Welcome Contributors!

<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="200">

</div>

Contributions are highly appreciated! Here's how you can help:

<table>
<tr>
<td width="33%" valign="top">

<h3 align="center">🔬 Research</h3>

- Add new CMOS technologies
- Implement BSIM models
- Advanced delay models
- Process variation analysis
- Temperature effects

</td>
<td width="33%" valign="top">

<h3 align="center">💻 Development</h3>

- Web interface (React/Vue)
- Mobile applications
- GUI (PyQt/Tkinter)
- API development
- Export features

</td>
<td width="33%" valign="top">

<h3 align="center">📚 Documentation</h3>

- Tutorial creation
- Video demonstrations
- API documentation
- Translations
- Example library

</td>
</tr>
</table>

<div align="center">

### 📝 Contribution Process

</div>

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/AmazingFeature

# 3. Commit your changes
git commit -m 'Add some AmazingFeature'

# 4. Push to the branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
```

<div align="center">

### 📋 Guidelines

- Follow **PEP 8** style guidelines
- Add **docstrings** to all functions
- Include **type hints** where appropriate
- Write **unit tests** for new features
- Update **documentation**
- Add **examples** for new functionality

</div>

---

## 📜 License

<div align="center">

**MIT License**

Copyright (c) 2024 CMOS Logic Analyzer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND**

---

</div>

## 👨‍💻 Author

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/213844263-a8897a51-32f4-4b3b-b5c2-e1528b89f6f3.png" width="100">

### Muhammad Abdulhamid

**Digital Circuit Designer & VLSI Engineer**

<p>
  <a href="https://github.com/Muhammad-296">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/muhammad-abdulhamid/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:muhammad.al.ajami.se@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
</p>

**Created with ❤️ for the Digital Design Community**

</div>

---

## 🙏 Acknowledgments

<div align="center">

Special thanks to the **VLSI Design Community**, all **Contributors & Testers**, and **Academic Resources** that made this project possible.

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="400">

</div>

---

## 📚 References

<div align="center">

### Academic & Technical Resources

</div>

<table>
<tr>
<td width="50%" valign="top">

**📖 Textbooks**
1. Weste & Harris - *CMOS VLSI Design* (4th ed.)
2. Rabaey et al. - *Digital Integrated Circuits* (2nd ed.)
3. Sedra & Smith - *Microelectronic Circuits* (7th ed.)

**🔬 Technical Documentation**
4. BSIM Model Documentation (Berkeley)
5. MOSIS IC Fabrication Specifications
6. IEEE Xplore - CMOS Delay Modeling

</td>
<td width="50%" valign="top">

**🌐 Online Resources**
7. [MIT OpenCourseWare - VLSI Design](https://ocw.mit.edu/)
8. [Electronics Tutorials - CMOS Logic](https://www.electronics-tutorials.ws/)
9. [Quine-McCluskey Algorithm](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)

**📊 Research Papers**
- Various IEEE publications on CMOS technology
- Semiconductor physics journals
- VLSI design conference proceedings

</td>
</tr>
</table>

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

**Made with 🔬 precision and ⚡ passion**

</div>
