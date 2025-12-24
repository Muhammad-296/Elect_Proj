<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CMOS Logic Analyzer - README</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            animation: fadeIn 1s ease-in;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
                opacity: 1;
            }
            50% {
                transform: scale(1.1);
                opacity: 0.5;
            }
        }

        h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: slideDown 1s ease-out;
            position: relative;
            z-index: 1;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .subtitle {
            font-size: 1.3em;
            opacity: 0.95;
            animation: slideUp 1s ease-out 0.3s both;
            position: relative;
            z-index: 1;
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 0.95;
                transform: translateY(0);
            }
        }

        .badges {
            margin-top: 20px;
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            position: relative;
            z-index: 1;
        }

        .badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            animation: bounceIn 1s ease-out;
        }

        @keyframes bounceIn {
            0% {
                opacity: 0;
                transform: scale(0.3);
            }
            50% {
                transform: scale(1.05);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        .content {
            padding: 40px;
        }

        .section {
            margin-bottom: 40px;
            animation: fadeInSection 0.8s ease-out;
        }

        @keyframes fadeInSection {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        h2 {
            color: #667eea;
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            position: relative;
        }

        h2::after {
            content: '';
            position: absolute;
            bottom: -3px;
            left: 0;
            width: 0;
            height: 3px;
            background: #764ba2;
            animation: expandLine 2s ease-out forwards;
        }

        @keyframes expandLine {
            to {
                width: 100%;
            }
        }

        h3 {
            color: #764ba2;
            font-size: 1.5em;
            margin: 20px 0 10px;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .feature-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            animation: scaleIn 0.6s ease-out;
        }

        @keyframes scaleIn {
            from {
                opacity: 0;
                transform: scale(0.8);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        .feature-card:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .feature-icon {
            font-size: 2.5em;
            margin-bottom: 15px;
            display: block;
            animation: rotate 3s linear infinite;
        }

        @keyframes rotate {
            from {
                transform: rotateY(0deg);
            }
            to {
                transform: rotateY(360deg);
            }
        }

        .feature-card:hover .feature-icon {
            animation: bounce 0.6s ease;
        }

        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-20px);
            }
        }

        .feature-title {
            font-weight: bold;
            color: #667eea;
            font-size: 1.2em;
            margin-bottom: 10px;
        }

        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            color: #e83e8c;
        }

        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            margin: 15px 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            animation: slideIn 1s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .code-block pre {
            margin: 0;
            font-family: 'Courier New', monospace;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
        }

        .tech-item {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
            animation: popIn 0.5s ease-out;
            transition: all 0.3s ease;
        }

        @keyframes popIn {
            0% {
                opacity: 0;
                transform: scale(0);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        .tech-item:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        }

        ul {
            list-style: none;
            padding-left: 0;
        }

        li {
            padding: 10px 0;
            padding-left: 30px;
            position: relative;
        }

        li::before {
            content: '▶';
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }

        .formula-box {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            border-left: 5px solid #ff6b6b;
            animation: slideInLeft 1s ease-out;
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-100px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .warning-box {
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }

        .info-box {
            background: #d1ecf1;
            border-left: 5px solid #17a2b8;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }

        .footer {
            background: #2d2d2d;
            color: white;
            padding: 30px;
            text-align: center;
        }

        .footer a {
            color: #667eea;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer a:hover {
            color: #764ba2;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
        }

        tr:hover {
            background: #f5f5f5;
        }

        .highlight {
            background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
            padding: 2px 8px;
            border-radius: 5px;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .container {
                margin: 10px;
            }

            h1 {
                font-size: 2em;
            }

            .content {
                padding: 20px;
            }

            .feature-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚡ CMOS Logic Analyzer ⚡</h1>
            <p class="subtitle">Advanced Digital Circuit Design & Performance Analysis Tool</p>
            <div class="badges">
                <span class="badge">🔬 Python 3.x</span>
                <span class="badge">⚙️ CMOS Technology</span>
                <span class="badge">📊 Performance Analysis</span>
                <span class="badge">🎨 Colorful CLI</span>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h2>📖 Overview</h2>
                <p>A comprehensive Python-based tool for analyzing and optimizing CMOS logic circuits. This analyzer implements exact delay calculations, area optimization, and power analysis for digital logic designs using both NAND+NOT and NOR+NOT implementations.</p>
                
                <div class="info-box">
                    <strong>🎯 Key Highlight:</strong> This tool uses <span class="highlight">EXACT mathematical formulas</span> derived from MOSFET physics for delay, area, and power calculations—not approximations!
                </div>
            </div>

            <div class="section">
                <h2>✨ Features</h2>
                <div class="feature-grid">
                    <div class="feature-card">
                        <span class="feature-icon">🔧</span>
                        <div class="feature-title">Logic Minimization</div>
                        <p>Quine-McCluskey algorithm for optimal Boolean function simplification with K-map visualization</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">⚡</span>
                        <div class="feature-title">Exact Delay Calculation</div>
                        <p>Precise propagation delay using MOSFET capacitance models and non-linear equations</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">📐</span>
                        <div class="feature-title">Area Optimization</div>
                        <p>Exact area calculation using formula: n×W_n(l_n+2L_Dn) + w_p(l_p+2L_Dp)</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">🔋</span>
                        <div class="feature-title">Power Analysis</div>
                        <p>Maximum power dissipation calculation with switching voltage analysis</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">🎨</span>
                        <div class="feature-title">Visual K-Maps</div>
                        <p>Color-coded Karnaugh maps with prime implicant grouping</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">📊</span>
                        <div class="feature-title">Comparative Analysis</div>
                        <p>Side-by-side comparison of NAND+NOT vs NOR+NOT implementations</p>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>🔬 Supported Technologies</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Technology</th>
                            <th>Gate Oxide (nm)</th>
                            <th>V<sub>th</sub> (V)</th>
                            <th>Applications</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>1.0µm CMOS</strong></td>
                            <td>20 nm</td>
                            <td>±0.9 V</td>
                            <td>Legacy systems, education</td>
                        </tr>
                        <tr>
                            <td><strong>0.8µm CMOS</strong></td>
                            <td>16 nm</td>
                            <td>±0.8 V</td>
                            <td>Moderate performance</td>
                        </tr>
                        <tr>
                            <td><strong>0.6µm CMOS</strong></td>
                            <td>12 nm</td>
                            <td>±0.75 V</td>
                            <td>Standard digital logic</td>
                        </tr>
                        <tr>
                            <td><strong>0.5µm CMOS</strong></td>
                            <td>10 nm</td>
                            <td>±0.7 V</td>
                            <td>High-speed circuits</td>
                        </tr>
                        <tr>
                            <td><strong>0.35µm CMOS</strong></td>
                            <td>7 nm</td>
                            <td>±0.5 V</td>
                            <td>Advanced applications</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="section">
                <h2>🚀 Installation</h2>
                <h3>Prerequisites</h3>
                <div class="tech-stack">
                    <span class="tech-item">Python 3.7+</span>
                    <span class="tech-item">colorama</span>
                    <span class="tech-item">tabulate</span>
                </div>

                <h3>Setup Instructions</h3>
                <div class="code-block">
<pre># Clone the repository
git clone https://github.com/yourusername/cmos-logic-analyzer.git
cd cmos-logic-analyzer

# Install dependencies
pip install colorama tabulate

# Run the analyzer
python main.py</pre>
                </div>
            </div>

            <div class="section">
                <h2>📂 Project Structure</h2>
                <div class="code-block">
<pre>cmos-logic-analyzer/
├── main.py                 # Main application entry point
├── constants.py            # Physical constants and CMOS datasheets
├── mosfet.py              # MOSFET parameter calculations
├── logic_minimizer.py     # Quine-McCluskey & K-map generation
├── design_implementer.py  # NAND/NOR design implementations
├── delay_calculator.py    # Exact delay calculation formulas
├── performance_analyzer.py # Area, power, bit rate analysis
└── comparator.py          # Design comparison and optimization</pre>
                </div>
            </div>

            <div class="section">
                <h2>💡 Usage Example</h2>
                <div class="code-block">
<pre><span style="color: #50fa7b;"># Start the analyzer</span>
python main.py

<span style="color: #50fa7b;"># Follow the interactive prompts:</span>
<span style="color: #8be9fd;">1.</span> Select CMOS technology (e.g., 0.35µm CMOS)
<span style="color: #8be9fd;">2.</span> Enter MOSFET dimensions (W<sub>n</sub>, L<sub>n</sub>, W<sub>p</sub>, L<sub>p</sub>)
<span style="color: #8be9fd;">3.</span> Input logic function (SOP minterms or POS maxterms)
<span style="color: #8be9fd;">4.</span> View minimized expression and K-map
<span style="color: #8be9fd;">5.</span> Compare NAND+NOT vs NOR+NOT implementations
<span style="color: #8be9fd;">6.</span> Get optimized design recommendation</pre>
                </div>

                <div class="info-box">
                    <strong>📝 Example Input:</strong><br>
                    Technology: 0.35µm CMOS<br>
                    W<sub>n</sub> = 2.0µm, L<sub>n</sub> = 0.35µm<br>
                    W<sub>p</sub> = 4.0µm, L<sub>p</sub> = 0.35µm<br>
                    Minterms: 1, 3, 5, 7, 9, 11, 13, 15
                </div>
            </div>

            <div class="section">
                <h2>🧮 Mathematical Formulas</h2>
                
                <div class="formula-box">
                    <h3>📊 NOT Gate Delay</h3>
                    <p><strong>For V<sub>BS</sub> ≠ 0:</strong></p>
                    <code>C_load = n(C_gd_pc + C_gd_nt + C_db_pt) + C_db_nc + C_gb_pc</code>
                    <p><strong>For V<sub>BS</sub> = 0:</strong></p>
                    <code>C_load = n(C_gd_pc + C_gd_nt) + C_db_pc + C_db_nc + C_gb_pc</code>
                </div>

                <div class="formula-box">
                    <h3>⚡ NAND Gate Delay</h3>
                    <p><strong>Falling edge (Z<sub>ND</sub><sup>-</sup>):</strong></p>
                    <code>a = V_DD - V_th_n</code><br>
                    <code>X₁ = a(1 - √(1/n))</code><br>
                    <code>X₂ = a(1 - √(1/n [1 + (1 - V_th_n/a)²(n-1)]))</code><br>
                    <code>Z_ND<sup>-</sup> = (n × C_load<sup>-</sup> × 10⁶) / ((n² - 1)K_n × a) × [...]</code>
                </div>

                <div class="formula-box">
                    <h3>🔄 NOR Gate Delay</h3>
                    <p><strong>Rising edge (Z<sub>NR</sub><sup>+</sup>):</strong></p>
                    <code>a = V_DD - |V_th_p|</code><br>
                    <code>Similar structure to NAND with PMOS parameters</code>
                </div>

                <div class="formula-box">
                    <h3>📐 Area Calculation</h3>
                    <code>Area = n×W_n(l_n + 2L_Dn) + w_p(l_p + 2L_Dp) [µm²]</code>
                </div>

                <div class="formula-box">
                    <h3>🔋 Maximum Power</h3>
                    <code>V_inss = (√K_n × V_th_n + √K_p(V_DD - V_th_p)) / (√K_n + √K_p)</code><br>
                    <code>P_max = G × (K_n/2) × (V_inss - V_th_n)² × V_DD [µW]</code>
                </div>
            </div>

            <div class="section">
                <h2>📊 Output Analysis</h2>
                <p>The tool provides comprehensive analysis including:</p>
                <ul>
                    <li><strong>Gate Count:</strong> Total NAND/NOR and NOT gates</li>
                    <li><strong>Propagation Delay:</strong> Exact delay calculation for each gate</li>
                    <li><strong>Bit Rate:</strong> Maximum operating frequency (Hz and MHz)</li>
                    <li><strong>Total Area:</strong> Silicon area in µm²</li>
                    <li><strong>Power Dissipation:</strong> Maximum power in µW</li>
                    <li><strong>Optimization Scores:</strong> 4-criteria comparison (area, power, speed, gates)</li>
                    <li><strong>Design Recommendation:</strong> Best implementation based on multiple metrics</li>
                </ul>
            </div>

            <div class="section">
                <h2>🎯 Design Optimization Criteria</h2>
                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-title">🏆 Area</div>
                        <p>Minimizes silicon real estate</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-title">⚡ Speed</div>
                        <p>Maximizes bit rate (MHz)</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-title">🔋 Power</div>
                        <p>Minimizes energy consumption</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-title">🎚️ Gates</div>
                        <p>Reduces circuit complexity</p>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>🔍 Technical Highlights</h2>
                <ul>
                    <li><strong>Non-linear delay models:</strong> Uses exact logarithmic equations, not RC approximations</li>
                    <li><strong>Body effect consideration:</strong> Accurate V<sub>th</sub> calculation with V<sub>BS</sub> variations</li>
                    <li><strong>Capacitance extraction:</strong> Separate cutoff and triode region capacitances</li>
                    <li><strong>Load calculation:</strong> Gate-drain, gate-source, drain-body, and gate-body components</li>
                    <li><strong>Multi-input gates:</strong> Supports 2-input to n-input NAND/NOR gates</li>
                    <li><strong>Technology scaling:</strong> Accurate parameters for 1.0µm down to 0.35µm processes</li>
                </ul>
            </div>

            <div class="section">
                <h2>⚠️ Limitations & Assumptions</h2>
                <div class="warning-box">
                    <strong>Note:</strong>
                    <ul style="margin-top: 10px;">
                        <li>Assumes ideal switching conditions</li>
                        <li>Room temperature operation (300K)</li>
                        <li>5V supply voltage (V<sub>DD</sub> = 5.0V)</li>
                        <li>Neglects interconnect parasitics</li>
                        <li>Square-law MOSFET model for hand calculations</li>
                    </ul>
                </div>
            </div>

            <div class="section">
                <h2>🤝 Contributing</h2>
                <p>Contributions are welcome! Please feel free to submit pull requests or open issues for:</p>
                <ul>
                    <li>Adding more CMOS technologies (e.g., sub-0.18µm processes)</li>
                    <li>Implementing additional logic styles (DCVSL, Pass-transistor logic)</li>
                    <li>Enhancing visualization features</li>
                    <li>Improving calculation accuracy</li>
                    <li>Adding export functionality (PDF reports, CSV data)</li>
                </ul>
            </div>

            <div class="section">
                <h2>📜 License</h2>
                <p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
            </div>

            <div class="section">
                <h2>👨‍💻 Author</h2>
                <p>Created with ❤️ for digital circuit designers and VLSI engineers</p>
            </div>

            <div class="section">
                <h2>📚 References</h2>
                <ul>
                    <li>Weste & Harris - "CMOS VLSI Design"</li>
                    <li>Rabaey, Chandrakasan & Nikolic - "Digital Integrated Circuits"</li>
                    <li>Sedra & Smith - "Microelectronic Circuits"</li>
                    <li>BSIM Model Documentation</li>
                </ul>
            </div>
        </div>

        <div class="footer">
            <p>⭐ If you find this tool useful, please star the repository! ⭐</p>
            <p style="margin-top: 10px;">
                <a href="https://github.com/yourusername/cmos-logic-analyzer">GitHub</a> • 
                <a href="https://github.com/yourusername/cmos-logic-analyzer/issues">Report Bug</a> • 
                <a href="https://github.com/yourusername/cmos-logic-analyzer/issues">Request Feature</a>
            </p>
            <p style="margin-top: 20px; font-size: 0.9em; opacity: 0.8;">
                © 2024 CMOS Logic Analyzer. All Rights Reserved.
            </p>
        </div>
    </div>
</body>
</html>
