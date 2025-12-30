<div align="center">

# ⚡ CMOS Logic Analyzer

### Professional Circuit Design & Optimization Tool

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![CMOS](https://img.shields.io/badge/CMOS-Technology-purple?style=flat)](https://github.com)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat)](https://github.com)

**[Features](#-features)** • **[Installation](#-installation)** • **[Usage](#-usage)** • **[Formulas](#-formulas)** • **[Contributing](#-contributing)**

</div>

---

## 📊 Project Statistics

<div align="center">

| Metric | Value |
|:------:|:-----:|
| 🎯 **Supported CMOS Technologies** | 5 (1.0µm → 0.35µm) |
| 🧮 **Analysis Methods** | 3 (Delay, Area, Power) |
| 📐 **K-Map Variables** | 2-4 Variables |
| ⚡ **Calculation Accuracy** | Exact (Non-linear) |
| 🔄 **Implementation Types** | NAND+NOT & NOR+NOT |
| 📦 **Total Modules** | 8 Python Files |
| 🎨 **K-Map Visualizations** | Color-coded ASCII |
| 🏆 **Optimization Criteria** | 4 (Area/Speed/Power/Gates) |

</div>

---

## 📖 Overview

A **comprehensive Python-based tool** for analyzing and optimizing CMOS logic circuits with **exact mathematical formulas** derived from fundamental semiconductor physics. This analyzer implements precise delay calculations, area optimization, and power analysis for digital logic designs.

### 🎯 Why This Tool?

- ✅ **Exact Calculations** - No approximations, uses real MOSFET equations
- ✅ **Visual K-Maps** - Color-coded groupings for easy understanding
- ✅ **Dual Implementation** - Compare NAND+NOT vs NOR+NOT designs
- ✅ **Technology-Aware** - Accurate parameters for 5 CMOS technologies
- ✅ **Optimization Engine** - Automated design recommendations

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🔧 Core Capabilities
- **Quine-McCluskey** logic minimization
- **K-map visualization** (2-4 variables)
- **Exact delay calculation** using non-linear models
- **Area optimization** with technology parameters
- **Power analysis** with switching voltage calculation
- **Comparative analysis** between implementations

</td>
<td width="50%" valign="top">

### 📊 Analysis Outputs
- **Propagation delays** (rise/fall separate)
- **Maximum bit rate** calculation
- **Silicon area** breakdown by gate
- **Power dissipation** estimates
- **Gate count** optimization
- **Design recommendations** with reasoning

</td>
</tr>
</table>

---

## 🔬 Supported Technologies

<div align="center">

| Technology | Gate Oxide | Vth (V) | μn (cm²/V·s) | μp (cm²/V·s) | Year |
|:----------:|:----------:|:-------:|:------------:|:------------:|:----:|
| **1.0µm** | 20 nm | ±0.9 | 450 | 180 | ~1985 |
| **0.8µm** | 16 nm | ±0.8 | 460 | 185 | ~1989 |
| **0.6µm** | 12 nm | ±0.75 | 470 | 190 | ~1994 |
| **0.5µm** | 10 nm | ±0.7 | 460 | 190 | ~1996 |
| **0.35µm** | 7 nm | ±0.5 | 500 | 200 | ~1998 |

</div>

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

```bash
# Clone repository
git clone https://github.com/Muhammad-296/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# Install dependencies
pip install colorama tabulate

# Run analyzer
python main.py
```

---

## 💡 Usage

### Interactive Mode

1. **Select CMOS technology** (1.0µm to 0.35µm)
2. **Enter MOSFET dimensions** (Wn, Ln, Wp, Lp)
3. **Input logic function** (SOP minterms or POS maxterms)
4. **View comprehensive analysis** with recommendations

### Sample Output

```
╔═══════════════════════════════════════════════════════════╗
║              ANALYSIS COMPLETE                            ║
╚═══════════════════════════════════════════════════════════╝

Technology: 0.35um CMOS
Function: F = A + B + C + D

┌────────────────────┬─────────────┬─────────────┐
│ Metric             │ NAND+NOT    │ NOR+NOT     │
├────────────────────┼─────────────┼─────────────┤
│ Delay (ns)         │ 2.456       │ 2.189       │
│ Bit Rate (MHz)     │ 407.18      │ 456.82      │
│ Area (μm²)         │ 45.23       │ 42.15       │
│ Power (μW)         │ 12.34       │ 11.02       │
└────────────────────┴─────────────┴─────────────┘

🏆 RECOMMENDED: NOR+NOT (4/4 criteria)
```

---

## 🧮 Mathematical Formulas

### Delay Calculation

**NOT Gate:**
```
Z_NOT⁻ = Rn × Cload    where Rn = 1/(Kn×(VDD - Vth_n))
Z_NOT⁺ = Rp × Cload    where Rp = 1/(Kp×(VDD - |Vth_p|))
```

**NAND/NOR Gates:**
```
Uses exact logarithmic equations accounting for:
- Multi-input transistor stacking
- Non-linear MOSFET characteristics
- Separate cutoff and triode capacitances
```

### Area Formula

```
Area = n×Wn(ln + 2LDn) + wp(lp + 2LDp) [μm²]

where:
  n   = number of inputs
  Wn  = NMOS width
  ln  = NMOS channel length
  LDn = NMOS lateral diffusion
  wp  = PMOS width
  lp  = PMOS channel length
  LDp = PMOS lateral diffusion
```

### Power Formula

```
Pmax = G × (Kn/2) × (V_inss - Vth_n)² × VDD [μW]

where:
  G = total gate count
  V_inss = input switching voltage
```

---

## 📂 Project Structure

```
cmos-logic-analyzer/
├── main.py                    # Main application entry
├── constants.py               # Physical constants & datasheets
├── mosfet.py                  # MOSFET parameter calculations
├── logic_minimizer.py         # Quine-McCluskey & K-map
├── design_implementer.py      # NAND/NOR implementations
├── delay_calculator.py        # Exact delay formulas
├── performance_analyzer.py    # Area, power, bit rate
├── comparator.py              # Design comparison engine
└── requirements.txt           # Dependencies
```

---

## 🎯 Optimization Criteria

<div align="center">

| Criterion | Weight | Measurement | Goal |
|:---------:|:------:|:-----------:|:----:|
| 🏆 **Area** | 25% | μm² | Minimize |
| ⚡ **Speed** | 25% | MHz | Maximize |
| 🔋 **Power** | 25% | μW | Minimize |
| 🎚️ **Gates** | 25% | Count | Minimize |

**Scoring:** Each design gets 1 point per criterion win. Highest score wins. Tie-breaker: smallest area.

</div>

---

## ⚠️ Assumptions & Limitations

<div align="center">

| Category | Details |
|:--------:|:--------|
| **Temperature** | Room temperature (300K) operation |
| **Supply Voltage** | Fixed VDD = 5.0V |
| **MOSFET Model** | Square-law (long-channel) |
| **Logic Style** | Static CMOS only |
| **Interconnects** | Parasitic wiring effects neglected |

</div>

### 🚀 Future Roadmap

- [ ] Deep submicron technologies (<180nm)
- [ ] Advanced BSIM models (BSIM4/6)
- [ ] Temperature/voltage variation analysis
- [ ] Interconnect delay modeling
- [ ] SPICE netlist export
- [ ] Web-based GUI interface

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Guidelines:**
- Follow PEP 8 style
- Add docstrings and type hints
- Include unit tests
- Update documentation

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Muhammad Abdulhamid**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/Muhammad-296)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/muhammad-abdulhamid/)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:muhammad.al.ajami.se@gmail.com)

*Created with ❤️ for Digital Circuit Designers & VLSI Engineers*

</div>

---

## 🙏 Acknowledgments

- **VLSI Design Community** - For continuous feedback and support
- **Open Source Contributors** - For testing and improvements
- **Academic Resources** - CMOS textbooks and research papers

---

## 📚 Key References

1. Weste, N. H. E., & Harris, D. (2010). *CMOS VLSI Design* (4th ed.). Addison-Wesley.
2. Rabaey, J. M., et al. (2003). *Digital Integrated Circuits* (2nd ed.). Prentice Hall.
3. Sedra, A. S., & Smith, K. C. (2015). *Microelectronic Circuits* (7th ed.). Oxford.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with Python • Powered by Mathematics • Optimized for Performance

</div>
