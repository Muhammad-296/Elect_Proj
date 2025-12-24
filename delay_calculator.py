import math
from constants import PhysicalConstants

class DelayCalculator:
    def __init__(self, mosfet):
        self.mosfet = mosfet
        self.constants = PhysicalConstants()
    
    def calculate_not_gate_delay(self, n=1):
        """Calculate NOT gate delays using EXACT equations:
        
        For V_BS of PMOS ≠ 0:
        C_load^(-/+) = n(C_gd_pc/T + C_gd_nT/C + C_db_pc/T) + C_db_nT/C + C_gb_p/nC
        
        For V_BS of PMOS = 0:
        C_load^(-/+) = n(C_gd_pc/T + C_gd_nT/C) + C_db_pC/T + C_db_nT/C + C_gb_p/nC
        """
        
        print(f"\n{'='*60}")
        print(f"NOT Gate Delay Calculation (n={n}) - EXACT FORMULA")
        print(f"{'='*60}")
        
        # Calculate load capacitances based on V_BS
        if self.mosfet.VBS != 0:
            # V_BS of PMOS ≠ 0
            print(f"Case: V_BS = {self.mosfet.VBS}V ≠ 0")
            print(f"Using formula: C_load^(-/+) = n(C_gd_pc/T + C_gd_nT/C + C_db_pc/T) + C_db_nT/C + C_gb_p/nC")
            
            # Using specific choices: pc/T → pc, nT/C → nt, pC/T → pt, nC/T → nc
            C_load = n * (self.mosfet.Cgd_pc + self.mosfet.Cgd_nt + self.mosfet.Cdb_pt) + \
                     self.mosfet.Cdb_nc + self.mosfet.Cgb_pc
            
            print(f"\nNumerical calculation:")
            print(f"  n(C_gd_pc + C_gd_nT + C_db_pT) = {n} × ({self.mosfet.Cgd_pc:.2e} + {self.mosfet.Cgd_nt:.2e} + {self.mosfet.Cdb_pt:.2e})")
            print(f"                               = {n} × {self.mosfet.Cgd_pc + self.mosfet.Cgd_nt + self.mosfet.Cdb_pt:.2e}")
            print(f"                               = {n * (self.mosfet.Cgd_pc + self.mosfet.Cgd_nt + self.mosfet.Cdb_pt):.2e}")
            print(f"  C_db_nC = {self.mosfet.Cdb_nc:.2e}")
            print(f"  C_gb_pC = {self.mosfet.Cgb_pc:.2e}")
            
        else:
            # V_BS of PMOS = 0
            print(f"Case: V_BS = 0V")
            print(f"Using formula: C_load^(-/+) = n(C_gd_pc/T + C_gd_nT/C) + C_db_pC/T + C_db_nT/C + C_gb_p/nC")
            
            # Using specific choices: pc/T → pc, nT/C → nt, pC/T → pc, nC/T → nc
            C_load = n * (self.mosfet.Cgd_pc + self.mosfet.Cgd_nt) + \
                     self.mosfet.Cdb_pc + self.mosfet.Cdb_nc + self.mosfet.Cgb_pc
            
            print(f"\nNumerical calculation:")
            print(f"  n(C_gd_pc + C_gd_nT) = {n} × ({self.mosfet.Cgd_pc:.2e} + {self.mosfet.Cgd_nt:.2e})")
            print(f"                      = {n} × {self.mosfet.Cgd_pc + self.mosfet.Cgd_nt:.2e}")
            print(f"                      = {n * (self.mosfet.Cgd_pc + self.mosfet.Cgd_nt):.2e}")
            print(f"  C_db_pC = {self.mosfet.Cdb_pc:.2e}")
            print(f"  C_db_nC = {self.mosfet.Cdb_nc:.2e}")
            print(f"  C_gb_pC = {self.mosfet.Cgb_pc:.2e}")
        
        print(f"\n  C_load = {C_load:.2e} F")
        
        # Calculate NOT gate delays using simple RC model
        # Fall time (NMOS discharging)
        R_n = 1 / (self.mosfet.Kn * (self.constants.VDD - self.mosfet.Vth_n))
        Z_not_minus = R_n * C_load * 1e9  # Convert to ns
        
        # Rise time (PMOS charging)
        R_p = 1 / (self.mosfet.Kp * (self.constants.VDD - abs(self.mosfet.Vth_p)))
        Z_not_plus = R_p * C_load * 1e9  # Convert to ns
        
        print(f"\nFall delay (NMOS discharging):")
        print(f"  R_n = 1 / (K_n × (V_DD - V_th_n))")
        print(f"      = 1 / ({self.mosfet.Kn:.2e} × ({self.constants.VDD} - {self.mosfet.Vth_n:.3f}))")
        print(f"      = {R_n:.2e} Ω")
        print(f"  Z_not^- = R_n × C_load × 10^9")
        print(f"          = {R_n:.2e} × {C_load:.2e} × 10^9")
        print(f"          = {Z_not_minus:.3f} ns")
        
        print(f"\nRise delay (PMOS charging):")
        print(f"  R_p = 1 / (K_p × (V_DD - |V_th_p|))")
        print(f"      = 1 / ({self.mosfet.Kp:.2e} × ({self.constants.VDD} - {abs(self.mosfet.Vth_p):.3f}))")
        print(f"      = {R_p:.2e} Ω")
        print(f"  Z_not^+ = R_p × C_load × 10^9")
        print(f"          = {R_p:.2e} × {C_load:.2e} × 10^9")
        print(f"          = {Z_not_plus:.3f} ns")
        
        return Z_not_minus, Z_not_plus, C_load
    
    def calculate_nor_gate_delay(self, n):
        """Calculate NOR gate delays using EXACT equations:
        
        a = V_DD - |V_th_p|
        X₁ = a(1 - √(1/n))
        X₂ = a(1 - √(1/n [1 + (1 - V_th_p/a)² (n-1)]))
        Z_NR^+ = (n × C_load^+ × 10^6) / ((n^2 - 1)K_p × a) × [
                (n-1)ln((a - X₂/2)/(a - X₁/2)) + 
                2ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) + 
                (n+1)ln(X₁/X₂)]
        Z_NR^- = Z_I^-
        
        C_load^+ = n×Cgd_pT + Cdb_pC/n + n×Cgb_pC + n×Cgd_nC + n×Cdb_nC
        C_load^- = n×Cgd_pC + Cdb_pC/n + n×Cgb_pC + n×Cgd_nT + Cdb_nT
        """
        
        print(f"\n{'='*60}")
        print(f"NOR Gate Delay Calculation (n={n} inputs) - EXACT FORMULA")
        print(f"{'='*60}")
        
        if n == 1:
            print("NOR with 1 input = NOT gate")
            Z_minus, Z_plus, _ = self.calculate_not_gate_delay(1)
            return Z_minus, Z_plus
        
        print("\n1. LOAD CAPACITANCE CALCULATIONS:")
        
        # C_load^+ for rising edge
        C_load_plus = n * self.mosfet.Cgd_pt + self.mosfet.Cdb_pc/n + \
                     n * self.mosfet.Cgb_pc + n * self.mosfet.Cgd_nc + \
                     n * self.mosfet.Cdb_nc
        
        print(f"\nFor rising edge (C_load^+):")
        print(f"  C_load^+ = n×C_gd_pT + C_db_pC/n + n×C_gb_pC + n×C_gd_nC + n×C_db_nC")
        print(f"           = {n}×{self.mosfet.Cgd_pt:.2e} + {self.mosfet.Cdb_pc:.2e}/{n} + {n}×{self.mosfet.Cgb_pc:.2e} + {n}×{self.mosfet.Cgd_nc:.2e} + {n}×{self.mosfet.Cdb_nc:.2e}")
        print(f"           = {C_load_plus:.2e} F")
        
        # C_load^- for falling edge
        C_load_minus = n * self.mosfet.Cgd_pc + self.mosfet.Cdb_pc/n + \
                      n * self.mosfet.Cgb_pc + n * self.mosfet.Cgd_nt + \
                      self.mosfet.Cdb_nt
        
        print(f"\nFor falling edge (C_load^-):")
        print(f"  C_load^- = n×C_gd_pC + C_db_pC/n + n×C_gb_pC + n×C_gd_nT + C_db_nT")
        print(f"           = {n}×{self.mosfet.Cgd_pc:.2e} + {self.mosfet.Cdb_pc:.2e}/{n} + {n}×{self.mosfet.Cgb_pc:.2e} + {n}×{self.mosfet.Cgd_nt:.2e} + {self.mosfet.Cdb_nt:.2e}")
        print(f"           = {C_load_minus:.2e} F")
        
        print("\n2. RISING EDGE DELAY (Z_NR^+):")
        
        # Calculate a = V_DD - |V_th_p|
        a = self.constants.VDD - abs(self.mosfet.Vth_p)
        print(f"  a = V_DD - |V_th_p|")
        print(f"    = {self.constants.VDD} - {abs(self.mosfet.Vth_p):.3f}")
        print(f"    = {a:.3f} V")
        
        # Calculate X₁
        sqrt_term = math.sqrt(1/n)
        X1 = a * (1 - sqrt_term)
        print(f"\n  X₁ = a × (1 - √(1/n))")
        print(f"     = {a:.3f} × (1 - √(1/{n}))")
        print(f"     = {a:.3f} × (1 - {sqrt_term:.3f})")
        print(f"     = {X1:.3f} V")
        
        # Calculate X₂
        vth_a_ratio = abs(self.mosfet.Vth_p) / a
        bracket_term = 1 + (1 - vth_a_ratio)**2 * (n-1)
        sqrt_arg = (1/n) * bracket_term
        X2 = a * (1 - math.sqrt(sqrt_arg))
        
        print(f"\n  X₂ = a × (1 - √(1/n [1 + (1 - V_th_p/a)² (n-1)]))")
        print(f"     = {a:.3f} × (1 - √(1/{n} [1 + (1 - {abs(self.mosfet.Vth_p):.3f}/{a:.3f})² × ({n}-1)]))")
        print(f"     = {X2:.3f} V")
        
        print(f"\n  Z_NR^+ formula:")
        print(f"    Z_NR^+ = (n × C_load^+ × 10⁶) / ((n² - 1)K_p × a) × [")
        print(f"            (n-1)ln((a - X₂/2)/(a - X₁/2)) + ")
        print(f"            2ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) + ")
        print(f"            (n+1)ln(X₁/X₂)]")
        
        # Calculate Z_NR^+
        numerator = n * C_load_plus * 1e6
        denominator = (n**2 - 1) * self.mosfet.Kp * a
        
        # Calculate logarithmic terms
        n_over_n_minus_1 = n/(n-1) if n > 1 else 1
        
        term1_numer = a - X2/2
        term1_denom = a - X1/2
        term1_ratio = term1_numer / term1_denom if term1_denom != 0 else 1
        
        term2_numer = 1 - n_over_n_minus_1 * X2/2
        term2_denom = 1 - n_over_n_minus_1 * X1/2
        term2_ratio = term2_numer / term2_denom if term2_denom != 0 else 1
        
        term3_ratio = X1 / X2 if X2 != 0 else 1
        
        if term1_ratio > 0 and term2_ratio > 0 and term3_ratio > 0 and denominator != 0:
            log_term1 = (n-1) * math.log(term1_ratio)
            log_term2 = 2 * math.log(term2_ratio)
            log_term3 = (n+1) * math.log(term3_ratio)
            
            log_sum = log_term1 + log_term2 + log_term3
            Z_NR_plus = (numerator / denominator) * log_sum
            
            print(f"\n  Numerical calculation:")
            print(f"    Numerator = n × C_load^+ × 10⁶ = {n} × {C_load_plus:.2e} × 10⁶ = {numerator:.2e}")
            print(f"    Denominator = (n² - 1)K_p × a = ({n}² - 1) × {self.mosfet.Kp:.3e} × {a:.3f} = {denominator:.2e}")
            print(f"    ln((a - X₂/2)/(a - X₁/2)) = ln({term1_numer:.3f}/{term1_denom:.3f}) = {math.log(term1_ratio):.3f}")
            print(f"    ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) = ln({term2_numer:.3f}/{term2_denom:.3f}) = {math.log(term2_ratio):.3f}")
            print(f"    ln(X₁/X₂) = ln({X1:.3f}/{X2:.3f}) = {math.log(term3_ratio):.3f}")
            print(f"    Sum of log terms = {log_sum:.3f}")
            print(f"    Z_NR^+ = ({numerator:.2e}/{denominator:.2e}) × {log_sum:.3f} = {Z_NR_plus:.3f} ns")
        else:
            # Fallback to RC model
            print(f"\n  Warning: Invalid logarithmic arguments, using RC model")
            R_p = 1 / (self.mosfet.Kp * (self.constants.VDD - abs(self.mosfet.Vth_p)))
            Z_NR_plus = R_p * C_load_plus * 1e9
            print(f"    R_p = 1 / (K_p × (V_DD - |V_th_p|)) = {R_p:.2e} Ω")
            print(f"    Z_NR^+ = R_p × C_load^+ × 10⁹ = {R_p:.2e} × {C_load_plus:.2e} × 10⁹ = {Z_NR_plus:.3f} ns")
        
        print("\n3. FALLING EDGE DELAY (Z_NR^-):")
        print(f"  Using NOT gate delay Z_I^-")
        Z_not_minus, Z_not_plus, _ = self.calculate_not_gate_delay(1)
        Z_NR_minus = Z_not_minus
        print(f"  Z_NR^- = Z_I^- = {Z_NR_minus:.3f} ns")
        
        return Z_NR_minus, Z_NR_plus
    
    def calculate_nand_gate_delay(self, n):
        """Calculate NAND gate delays using EXACT equations:
        
        a = V_DD - V_th_n
        X₁ = a(1 - √(1/n))
        X₂ = a(1 - √(1/n [1 + (1 - V_th_n/a)² (n-1)]))
        Z_ND^- = (n × C_load^- × 10^6) / ((n^2 - 1)K_n × a) × [
                (n-1)ln((a - X₂/2)/(a - X₁/2)) + 
                2ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) + 
                (n+1)ln(X₁/X₂)]
        Z_ND^+ = I^+
        
        C_load^- = n×Cgd_pC + n×Cdb_pc + n×Cgb_nT + Cdb_nT/n + n×Cgd_nT
        C_load^+ = n×Cgd_pT + n×Cdb_pT + n×Cgb_nC + Cdb_nc/n + n×Cgd_nC
        """
        
        print(f"\n{'='*60}")
        print(f"NAND Gate Delay Calculation (n={n} inputs) - EXACT FORMULA")
        print(f"{'='*60}")
        
        if n == 1:
            print("NAND with 1 input = NOT gate")
            Z_minus, Z_plus, _ = self.calculate_not_gate_delay(1)
            return Z_minus, Z_plus
        
        print("\n1. LOAD CAPACITANCE CALCULATIONS:")
        
        # C_load^- for falling edge
        C_load_minus = n * self.mosfet.Cgd_pc + n * self.mosfet.Cdb_pc + \
                      n * self.mosfet.Cgb_nt + self.mosfet.Cdb_nt/n + \
                      n * self.mosfet.Cgd_nt
        
        print(f"\nFor falling edge (C_load^-):")
        print(f"  C_load^- = n×C_gd_pC + n×C_db_pc + n×C_gb_nT + C_db_nT/n + n×C_gd_nT")
        print(f"           = {n}×{self.mosfet.Cgd_pc:.2e} + {n}×{self.mosfet.Cdb_pc:.2e} + {n}×{self.mosfet.Cgb_nt:.2e} + {self.mosfet.Cdb_nt:.2e}/{n} + {n}×{self.mosfet.Cgd_nt:.2e}")
        print(f"           = {C_load_minus:.2e} F")
        
        # C_load^+ for rising edge
        C_load_plus = n * self.mosfet.Cgd_pt + n * self.mosfet.Cdb_pt + \
                     n * self.mosfet.Cgb_nc + self.mosfet.Cdb_nc/n + \
                     n * self.mosfet.Cgd_nc
        
        print(f"\nFor rising edge (C_load^+):")
        print(f"  C_load^+ = n×C_gd_pT + n×C_db_pT + n×C_gb_nC + C_db_nc/n + n×C_gd_nC")
        print(f"           = {n}×{self.mosfet.Cgd_pt:.2e} + {n}×{self.mosfet.Cdb_pt:.2e} + {n}×{self.mosfet.Cgb_nc:.2e} + {self.mosfet.Cdb_nc:.2e}/{n} + {n}×{self.mosfet.Cgd_nc:.2e}")
        print(f"           = {C_load_plus:.2e} F")
        
        print("\n2. FALLING EDGE DELAY (Z_ND^-):")
        
        # Calculate a = V_DD - V_th_n
        a = self.constants.VDD - self.mosfet.Vth_n
        print(f"  a = V_DD - V_th_n")
        print(f"    = {self.constants.VDD} - {self.mosfet.Vth_n:.3f}")
        print(f"    = {a:.3f} V")
        
        # Calculate X₁
        sqrt_term = math.sqrt(1/n)
        X1 = a * (1 - sqrt_term)
        print(f"\n  X₁ = a × (1 - √(1/n))")
        print(f"     = {a:.3f} × (1 - √(1/{n}))")
        print(f"     = {X1:.3f} V")
        
        # Calculate X₂
        vth_a_ratio = self.mosfet.Vth_n / a
        bracket_term = 1 + (1 - vth_a_ratio)**2 * (n-1)
        sqrt_arg = (1/n) * bracket_term
        X2 = a * (1 - math.sqrt(sqrt_arg))
        
        print(f"\n  X₂ = a × (1 - √(1/n [1 + (1 - V_th_n/a)² (n-1)]))")
        print(f"     = {a:.3f} × (1 - √(1/{n} [1 + (1 - {self.mosfet.Vth_n:.3f}/{a:.3f})² × ({n}-1)]))")
        print(f"     = {X2:.3f} V")
        
        print(f"\n  Z_ND^- formula:")
        print(f"    Z_ND^- = (n × C_load^- × 10⁶) / ((n² - 1)K_n × a) × [")
        print(f"            (n-1)ln((a - X₂/2)/(a - X₁/2)) + ")
        print(f"            2ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) + ")
        print(f"            (n+1)ln(X₁/X₂)]")
        
        # Calculate Z_ND^-
        numerator = n * C_load_minus * 1e6
        denominator = (n**2 - 1) * self.mosfet.Kn * a
        
        # Calculate logarithmic terms
        n_over_n_minus_1 = n/(n-1) if n > 1 else 1
        
        term1_numer = a - X2/2
        term1_denom = a - X1/2
        term1_ratio = term1_numer / term1_denom if term1_denom != 0 else 1
        
        term2_numer = 1 - n_over_n_minus_1 * X2/2
        term2_denom = 1 - n_over_n_minus_1 * X1/2
        term2_ratio = term2_numer / term2_denom if term2_denom != 0 else 1
        
        term3_ratio = X1 / X2 if X2 != 0 else 1
        
        if term1_ratio > 0 and term2_ratio > 0 and term3_ratio > 0 and denominator != 0:
            log_term1 = (n-1) * math.log(term1_ratio)
            log_term2 = 2 * math.log(term2_ratio)
            log_term3 = (n+1) * math.log(term3_ratio)
            
            log_sum = log_term1 + log_term2 + log_term3
            Z_ND_minus = (numerator / denominator) * log_sum
            
            print(f"\n  Numerical calculation:")
            print(f"    Numerator = n × C_load^- × 10⁶ = {n} × {C_load_minus:.2e} × 10⁶ = {numerator:.2e}")
            print(f"    Denominator = (n² - 1)K_n × a = ({n}² - 1) × {self.mosfet.Kn:.3e} × {a:.3f} = {denominator:.2e}")
            print(f"    ln((a - X₂/2)/(a - X₁/2)) = ln({term1_numer:.3f}/{term1_denom:.3f}) = {math.log(term1_ratio):.3f}")
            print(f"    ln((1 - (n/(n-1))X₂/2)/(1 - (n/(n-1))X₁/2)) = ln({term2_numer:.3f}/{term2_denom:.3f}) = {math.log(term2_ratio):.3f}")
            print(f"    ln(X₁/X₂) = ln({X1:.3f}/{X2:.3f}) = {math.log(term3_ratio):.3f}")
            print(f"    Sum of log terms = {log_sum:.3f}")
            print(f"    Z_ND^- = ({numerator:.2e}/{denominator:.2e}) × {log_sum:.3f} = {Z_ND_minus:.3f} ns")
        else:
            # Fallback to RC model
            print(f"\n  Warning: Invalid logarithmic arguments, using RC model")
            R_n = 1 / (self.mosfet.Kn * (self.constants.VDD - self.mosfet.Vth_n))
            Z_ND_minus = R_n * C_load_minus * 1e9
            print(f"    R_n = 1 / (K_n × (V_DD - V_th_n)) = {R_n:.2e} Ω")
            print(f"    Z_ND^- = R_n × C_load^- × 10⁹ = {R_n:.2e} × {C_load_minus:.2e} × 10⁹ = {Z_ND_minus:.3f} ns")
        
        print("\n3. RISING EDGE DELAY (Z_ND^+):")
        print(f"  Using NOT gate delay I^+")
        Z_not_minus, Z_not_plus, _ = self.calculate_not_gate_delay(1)
        Z_ND_plus = Z_not_plus
        print(f"  Z_ND^+ = I^+ = {Z_ND_plus:.3f} ns")
        
        return Z_ND_minus, Z_ND_plus