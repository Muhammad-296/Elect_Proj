import math
from tabulate import tabulate
from colorama import Fore

from delay_calculator import DelayCalculator
from constants import PhysicalConstants

class PerformanceAnalyzer:
    def __init__(self, mosfet):
        self.mosfet = mosfet
        self.delay_calc = DelayCalculator(mosfet)
        self.constants = PhysicalConstants()
    
    def calculate_area(self, gate_details):
        """Calculate total area using the formula: n×W_n(l_n+2L_Dn) + w_p(l_p+2L_Dp) μm²
        Where:
        - n = number of inputs for each gate
        - W_n = NMOS width per transistor (Wn)
        - w_p = PMOS width per transistor (Wp)
        - l_n = NMOS channel length (Ln)
        - l_p = PMOS channel length (Lp)
        - L_Dn = NMOS lateral diffusion length
        - L_Dp = PMOS lateral diffusion length
        
        For each gate: Area = n×W_n(l_n+2L_Dn) + w_p(l_p+2L_Dp)
        """
        
        print(f"\n{Fore.MAGENTA}Detailed Area Calculation (Exact Formula):")
        print(Fore.CYAN + "-"*60)
        print(f"{Fore.YELLOW}Formula: Area = n×W_n(l_n+2L_Dn) + w_p(l_p+2L_Dp) μm²")
        
        total_area = 0
        area_details = []
        gate_count = 1
        
        for gate_info in gate_details:
            gate_type, n_inputs, description = gate_info
            
            if n_inputs == 0:
                n_inputs = 1  # Minimum 1 input for area calculation
            
            print(f"\n{Fore.CYAN}Gate {gate_count}: {gate_type} with {n_inputs} inputs")
            print(f"{Fore.WHITE}Description: {description}")
            
            # Calculate NMOS area: n×W_n(l_n+2L_Dn)
            nmos_term = n_inputs * self.mosfet.Wn
            nmos_length_term = self.mosfet.Ln + 2 * self.mosfet.tech["L_Dn"]
            area_n = nmos_term * nmos_length_term
            
            # Calculate PMOS area: w_p(l_p+2L_Dp)
            pmos_term = self.mosfet.Wp
            pmos_length_term = self.mosfet.Lp + 2 * self.mosfet.tech["L_Dp"]
            area_p = pmos_term * pmos_length_term
            
            gate_area = area_n + area_p
            total_area += gate_area
            
            print(f"{Fore.GREEN}  NMOS area = n × W_n × (l_n + 2×L_Dn)")
            print(f"              = {n_inputs} × {self.mosfet.Wn:.2f} × ({self.mosfet.Ln:.2f} + 2×{self.mosfet.tech['L_Dn']:.2f})")
            print(f"              = {n_inputs} × {self.mosfet.Wn:.2f} × {nmos_length_term:.2f}")
            print(f"              = {area_n:.2f} μm²")
            
            print(f"{Fore.CYAN}  PMOS area = w_p × (l_p + 2×L_Dp)")
            print(f"              = {self.mosfet.Wp:.2f} × ({self.mosfet.Lp:.2f} + 2×{self.mosfet.tech['L_Dp']:.2f})")
            print(f"              = {self.mosfet.Wp:.2f} × {pmos_length_term:.2f}")
            print(f"              = {area_p:.2f} μm²")
            
            print(f"{Fore.MAGENTA}  Gate Total = {area_n:.2f} + {area_p:.2f} = {gate_area:.2f} μm²")
            
            area_details.append([gate_type, n_inputs, f"{gate_area:.2f} μm²"])
            gate_count += 1
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.YELLOW}AREA CALCULATION SUMMARY:")
        print(Fore.CYAN + "-"*60)
        
        if area_details:
            headers = [f"{Fore.CYAN}Gate Type", f"{Fore.CYAN}Inputs", f"{Fore.CYAN}Area (μm²)"]
            print(tabulate(area_details, headers=headers, tablefmt="fancy_grid"))
        
        print(f"\n{Fore.MAGENTA}TOTAL AREA = {total_area:.2f} μm²")
        
        return total_area
    
    def calculate_v_inss(self, Kn_total, Kp_total):
        """Calculate input switching voltage using formula:
        V_inss = (√(K_n) × V_th_n + √(K_p)(V_DD - V_th_p)) / (√(K_n) + √(K_p))
        """
        if Kn_total <= 0 or Kp_total <= 0:
            return self.constants.VDD / 2
        
        sqrt_Kn = math.sqrt(Kn_total)
        sqrt_Kp = math.sqrt(Kp_total)
        
        numerator = sqrt_Kn * self.mosfet.Vth_n + sqrt_Kp * (self.constants.VDD - abs(self.mosfet.Vth_p))
        denominator = sqrt_Kn + sqrt_Kp
        
        if denominator == 0:
            return self.constants.VDD / 2
        
        V_inss = numerator / denominator
        
        return V_inss
    
    def calculate_max_power(self, G, Kn_total):
        """Calculate maximum power dissipation using formula:
        Max Power = G × (K_n/2) × (V_inss - V_th_n)² × V_DD (in μW)
        """
        # Calculate V_inss
        V_inss = self.calculate_v_inss(Kn_total, Kn_total)
        
        # Calculate (V_inss - V_th_n)
        V_diff = V_inss - self.mosfet.Vth_n
        
        if V_diff <= 0:
            return 0
        
        # Calculate maximum power
        power_per_gate = (Kn_total / 2) * (V_diff ** 2) * self.constants.VDD
        max_power = G * power_per_gate * 1e6  # Convert to μW
        
        return max_power
    
    def analyze_nand_design(self, nand_gates, not_gates, gate_details):
        """Analyze NAND+NOT design performance"""
        print(f"\n{Fore.CYAN}PERFORMANCE ANALYSIS: NAND+NOT DESIGN")
        print(Fore.CYAN + "="*60)
        
        total_delay = 0
        delay_details = []
        
        # Analyze each gate delay
        for gate_info in gate_details:
            gate_type, n_inputs, description = gate_info
            
            if gate_type == "NOT":
                # NOT gate delay (n=1)
                Z_minus, Z_plus, _ = self.delay_calc.calculate_not_gate_delay(1)
                delay = max(Z_minus, Z_plus)
                total_delay += delay
                delay_details.append(["NOT", 1, f"{delay:.3f} ns"])
                
            elif "NAND" in gate_type:
                # NAND gate delay
                if n_inputs > 0:
                    Z_minus, Z_plus = self.delay_calc.calculate_nand_gate_delay(n_inputs)
                    delay = max(Z_minus, Z_plus)
                    total_delay += delay
                    delay_details.append([gate_type, n_inputs, f"{delay:.3f} ns"])
        
        # Calculate bit rate
        if total_delay <= 0:
            total_delay = 0.001
        
        bit_rate_hz = 1 / (total_delay * 1e-9)
        bit_rate_mhz = bit_rate_hz / 1e6
        
        # Calculate area using exact formula
        area = self.calculate_area(gate_details)
        
        # Calculate K_n total (sum of Kn for all gates)
        Kn_total = nand_gates * self.mosfet.Kn + not_gates * self.mosfet.Kn
        
        # Calculate total number of gates
        G = nand_gates + not_gates
        
        # Calculate max power
        max_power = self.calculate_max_power(G, Kn_total)
        
        # Display results
        if delay_details:
            print(f"\n{Fore.YELLOW}Delay Analysis:")
            headers = [f"{Fore.CYAN}Gate", f"{Fore.CYAN}Inputs", f"{Fore.CYAN}Delay (ns)"]
            print(tabulate(delay_details, headers=headers, tablefmt="fancy_grid"))
        
        print(f"\n{Fore.YELLOW}Performance Summary:")
        summary_data = [
            ["Total Delay", f"{total_delay:.3f} ns"],
            ["Bit Rate", f"{bit_rate_hz:.3e} Hz"],
            ["Bit Rate", f"{bit_rate_mhz:.3f} MHz"],
            ["Total Area (μm²)", f"{area:.2f} μm²"],
            ["Max Power (μW)", f"{max_power:.2f} μW"]
        ]
        print(tabulate(summary_data, tablefmt="fancy_grid"))
        
        return total_delay, bit_rate_hz, bit_rate_mhz, area, max_power
    
    def analyze_nor_design(self, nor_gates, not_gates, gate_details):
        """Analyze NOR+NOT design performance"""
        print(f"\n{Fore.CYAN}PERFORMANCE ANALYSIS: NOR+NOT DESIGN")
        print(Fore.CYAN + "="*60)
        
        total_delay = 0
        delay_details = []
        
        # Analyze each gate delay
        for gate_info in gate_details:
            gate_type, n_inputs, description = gate_info
            
            if gate_type == "NOT":
                # NOT gate delay (n=1)
                Z_minus, Z_plus, _ = self.delay_calc.calculate_not_gate_delay(1)
                delay = max(Z_minus, Z_plus)
                total_delay += delay
                delay_details.append(["NOT", 1, f"{delay:.3f} ns"])
                
            elif "NOR" in gate_type:
                # NOR gate delay
                if n_inputs > 0:
                    Z_minus, Z_plus = self.delay_calc.calculate_nor_gate_delay(n_inputs)
                    delay = max(Z_minus, Z_plus)
                    total_delay += delay
                    delay_details.append([gate_type, n_inputs, f"{delay:.3f} ns"])
        
        # Calculate bit rate
        if total_delay <= 0:
            total_delay = 0.001
        
        bit_rate_hz = 1 / (total_delay * 1e-9)
        bit_rate_mhz = bit_rate_hz / 1e6
        
        # Calculate area using exact formula
        area = self.calculate_area(gate_details)
        
        # Calculate K_n total (sum of Kn for all gates)
        Kn_total = nor_gates * self.mosfet.Kn + not_gates * self.mosfet.Kn
        
        # Calculate total number of gates
        G = nor_gates + not_gates
        
        # Calculate max power
        max_power = self.calculate_max_power(G, Kn_total)
        
        # Display results
        if delay_details:
            print(f"\n{Fore.YELLOW}Delay Analysis:")
            headers = [f"{Fore.CYAN}Gate", f"{Fore.CYAN}Inputs", f"{Fore.CYAN}Delay (ns)"]
            print(tabulate(delay_details, headers=headers, tablefmt="fancy_grid"))
        
        print(f"\n{Fore.YELLOW}Performance Summary:")
        summary_data = [
            ["Total Delay", f"{total_delay:.3f} ns"],
            ["Bit Rate", f"{bit_rate_hz:.3e} Hz"],
            ["Bit Rate", f"{bit_rate_mhz:.3f} MHz"],
            ["Total Area (μm²)", f"{area:.2f} μm²"],
            ["Max Power (μW)", f"{max_power:.2f} μW"]
        ]
        print(tabulate(summary_data, tablefmt="fancy_grid"))
        
        return total_delay, bit_rate_hz, bit_rate_mhz, area, max_power