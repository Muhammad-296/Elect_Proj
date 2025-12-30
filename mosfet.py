import math
from tabulate import tabulate
from colorama import Fore, Style

from constants import PhysicalConstants

class MOSFET:
    def __init__(self, tech, Wn, Ln, Wp, Lp, VBS=0):
        self.tech = tech
        self.Wn, self.Ln = Wn, Ln  # in μm
        self.Wp, self.Lp = Wp, Lp  # in μm
        self.VBS = VBS  # in V
        self.constants = PhysicalConstants()
        self.calculate_parameters()
        self.calculate_capacitances()

    def calculate_parameters(self):
        # Convert to SI units
        Tox = self.tech["T_ox"] * 1e-9  # Convert nm to m
        mu_on = self.tech["mu_on"] * 1e-4  # Convert cm²/V·s to m²/V·s
        mu_op = self.tech["mu_op"] * 1e-4  # Convert cm²/V·s to m²/V·s
        Wn_m = self.Wn * 1e-6  # Convert μm to m
        Ln_m = self.Ln * 1e-6  # Convert μm to m
        Wp_m = self.Wp * 1e-6  # Convert μm to m
        Lp_m = self.Lp * 1e-6  # Convert μm to m
        
        # 1. Calculate C_ox
        # C_ox = ε_ox / T_ox = (E_ox × ε_0) / T_ox
        self.Cox = (self.tech["E_ox"] * self.constants.eps_0) / Tox  # F/m²
        
        # 2. Calculate K_n and K_p
        # K_n = μ_on × C_ox × W_n / L_n (in μA/V²)
        Kn_si = mu_on * self.Cox * (Wn_m / Ln_m)  # A/V²
        self.Kn = Kn_si * 1e6  # Convert to μA/V²
        
        # K_p = μ_op × C_ox × W_p / L_p (in μA/V²)
        Kp_si = mu_op * self.Cox * (Wp_m / Lp_m)  # A/V²
        self.Kp = Kp_si * 1e6  # Convert to μA/V²
        
        # 3. Calculate N_Bn and N_Bp
        # N_Bn = (K_1n × C_ox)² / (2qε_si)
        K1n_Cox = self.tech["K_1n"] * self.Cox
        self.NB_n = (K1n_Cox ** 2) / (2 * self.constants.q * self.constants.eps_si)  # C/m³
        
        # N_Bp = (K_1p × C_ox)² / (2qε_si)
        K1p_Cox = self.tech["K_1p"] * self.Cox
        self.NB_p = (K1p_Cox ** 2) / (2 * self.constants.q * self.constants.eps_si)  # C/m³
        
        # 4. Calculate ψ_on and ψ_op
        # ψ_on = 2V_t ln(N_Bn / n_i)
        self.psi_n = 2 * self.constants.Vt * math.log(self.NB_n / self.constants.ni)  # V
        
        # ψ_op = 2V_t ln(N_Bp / n_i)
        self.psi_p = 2 * self.constants.Vt * math.log(self.NB_p / self.constants.ni)  # V
        
        # 5. Calculate threshold voltages
        # V_th_n = V_th_no
        self.Vth_n = self.tech["V_th_no"]  # V
        
        # V_th_p = V_th_po if V_BS = 0, otherwise V_th_p = V_th_po + K_1p × (√(ψ_op + V_BS) - √(ψ_op))
        if self.VBS == 0:
            self.Vth_p = self.tech["V_th_po"]  # V
        else:
            term = math.sqrt(self.psi_p + self.VBS) - math.sqrt(self.psi_p)
            self.Vth_p = self.tech["V_th_po"] + self.tech["K_1p"] * term  # V
        
        # 6. Calculate flat-band voltages
        # V_FB_n = V_th_n0 - K_1n √(ψ_on) - ψ_on
        self.V_FB_n = self.tech["V_th_no"] - self.tech["K_1n"] * math.sqrt(self.psi_n) - self.psi_n
        
        # V_FB_p = V_th_po - K_1p √(ψ_op) - ψ_op
        self.V_FB_p = self.tech["V_th_po"] - self.tech["K_1p"] * math.sqrt(self.psi_p) - self.psi_p

    def calculate_capacitances(self):
        """Calculate MOSFET capacitances with exact formulas (all in Farads)"""
        
        # Convert dimensions to meters for capacitance calculations
        Wn_m = self.Wn * 1e-6  # Convert μm to m
        Ln_m = self.Ln * 1e-6  # Convert μm to m
        Wp_m = self.Wp * 1e-6  # Convert μm to m
        Lp_m = self.Lp * 1e-6  # Convert μm to m
        
        # Convert diffusion lengths from technology parameters (μm to m)
        L_Dn_m = self.tech["L_Dn"] * 1e-6  # Convert μm to m
        L_Dp_m = self.tech["L_Dp"] * 1e-6  # Convert μm to m
        
        # 1. Gate-body capacitances (cutoff)
        # Cgb_nc = (W_n × C_ox × L_n) / √(1 + 4(V_FB)_n / (K_1n)²) × 10^(-12)
        denominator_nc = math.sqrt(1 + (4 * abs(self.V_FB_n)) / (self.tech["K_1n"] ** 2))
        Cgb_nc_si = (Wn_m * self.Cox * Ln_m) / denominator_nc
        self.Cgb_nc = Cgb_nc_si  # Already in F
        
        # Cgb_pc = (W_p × C_ox × L_p) / √(1 + 4(V_FB)_p / (K_1p)²) × 10^(-12)
        denominator_pc = math.sqrt(1 + (4 * abs(self.V_FB_p)) / (self.tech["K_1p"] ** 2))
        Cgb_pc_si = (Wp_m * self.Cox * Lp_m) / denominator_pc
        self.Cgb_pc = Cgb_pc_si  # Already in F
        
        # 2. Gate-drain/source capacitances (cutoff)
        # Cgs_nc = Cgd_nc = W_n × CGD_on × 10^(-6)
        self.Cgs_nc = self.Cgd_nc = Wn_m * self.tech["CGD_on"] * 1e-6  # F
        
        # Cgs_pc = Cgd_pc = W_p × CGD_op × 10^(-6)
        self.Cgs_pc = self.Cgd_pc = Wp_m * self.tech["CGD_op"] * 1e-6  # F
        
        # 3. Gate-drain/source capacitances (triode)
        # Cgs_nt = Cgd_nt = Cgs_nc + (W_n × L_n)/2 × C_ox × 10^(-12)
        C_ox_F_m2 = self.Cox  # F/m²
        additional_nt = (Wn_m * Ln_m / 2) * C_ox_F_m2
        self.Cgs_nt = self.Cgd_nt = self.Cgs_nc + additional_nt  # F
        
        # Cgs_pt = Cgd_pt = Cgs_pc + (W_p × L_p)/2 × C_ox × 10^(-12)
        additional_pt = (Wp_m * Lp_m / 2) * C_ox_F_m2
        self.Cgs_pt = self.Cgd_pt = self.Cgs_pc + additional_pt  # F
        
        # 4. Drain-body/source-body capacitances (cutoff)
        # Cdb_nc = Csb_nc = CJ_n × W_n × L_Dn × 10^(-12) + CJSW_n × 2(W_n + L_Dn) × 10^(-6)
        term1_nc = self.tech["CJ_n"] * Wn_m * L_Dn_m  # Already in F
        perimeter_n = 2 * (Wn_m + L_Dn_m)  # Perimeter in m
        term2_nc = self.tech["CJSW_n"] * perimeter_n  # F/m × m = F
        self.Cdb_nc = self.Csb_nc = term1_nc + term2_nc  # F
        
        # Cdb_pc = Csb_pc = CJ_p × W_p × L_Dp × 10^(-12) + CJSW_p × 2(W_p + L_Dp) × 10^(-6)
        term1_pc = self.tech["CJ_p"] * Wp_m * L_Dp_m  # Already in F
        perimeter_p = 2 * (Wp_m + L_Dp_m)  # Perimeter in m
        term2_pc = self.tech["CJSW_p"] * perimeter_p  # F/m × m = F
        self.Cdb_pc = self.Csb_pc = term1_pc + term2_pc  # F
        
        # 5. Drain-body/source-body capacitances (triode)
        # Cdp_nt = Csb_nt = Cdb_nc + (W_n × L_n)/2 × CJ_n × 10^(-12)
        additional_nt_db = (Wn_m * Ln_m / 2) * self.tech["CJ_n"]  # F
        self.Cdb_nt = self.Csb_nt = self.Cdb_nc + additional_nt_db  # F
        
        # Cdp_pt = Csb_pt = Cdb_pc + (W_p × L_p)/2 × CJ_p × 10^(-12)
        additional_pt_db = (Wp_m * Lp_m / 2) * self.tech["CJ_p"]  # F
        self.Cdb_pt = self.Csb_pt = self.Cdb_pc + additional_pt_db  # F
        
        # 6. Gate-body capacitances (triode) - typically half of cutoff
        self.Cgb_nt = self.Cgb_nc * 0.5  # F
        self.Cgb_pt = self.Cgb_pc * 0.5  # F

    def display_parameters(self):
        """Display all calculated parameters with units"""
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}MOSFET PARAMETERS CALCULATION")
        print(f"{Fore.CYAN}{'='*60}")
        
        # Basic parameters
        basic_params = [
            [f"{Fore.YELLOW}Parameter", f"{Fore.YELLOW}Value", f"{Fore.YELLOW}Unit"],
            ["C_ox (Gate oxide capacitance)", f"{self.Cox:.3e}", "F/m²"],
            ["K_n (NMOS transconductance)", f"{self.Kn:.3e}", "μA/V²"],
            ["K_p (PMOS transconductance)", f"{self.Kp:.3e}", "μA/V²"],
            ["N_Bn (NMOS bulk doping)", f"{self.NB_n:.3e}", "m⁻³"],
            ["N_Bp (PMOS bulk doping)", f"{self.NB_p:.3e}", "m⁻³"],
            ["ψ_on (NMOS surface potential)", f"{self.psi_n:.3f}", "V"],
            ["ψ_op (PMOS surface potential)", f"{self.psi_p:.3f}", "V"],
            ["V_th_n (NMOS threshold)", f"{self.Vth_n:.3f}", "V"],
            ["V_th_p (PMOS threshold)", f"{self.Vth_p:.3f}", "V"],
            ["V_FB_n (NMOS flat-band)", f"{self.V_FB_n:.3f}", "V"],
            ["V_FB_p (PMOS flat-band)", f"{self.V_FB_p:.3f}", "V"]
        ]
        
        print(f"\n{Fore.CYAN}BASIC PARAMETERS:")
        print(tabulate(basic_params, tablefmt="fancy_grid"))
        
        # Capacitances
        cap_params = [
            [f"{Fore.YELLOW}Capacitance", f"{Fore.YELLOW}Value", f"{Fore.YELLOW}Unit"],
            ["Cgb_nc (NMOS gate-body cutoff)", f"{self.Cgb_nc:.3e}", "F"],
            ["Cgb_pc (PMOS gate-body cutoff)", f"{self.Cgb_pc:.3e}", "F"],
            ["Cgs_nc (NMOS gate-source cutoff)", f"{self.Cgs_nc:.3e}", "F"],
            ["Cgd_nc (NMOS gate-drain cutoff)", f"{self.Cgd_nc:.3e}", "F"],
            ["Cgs_pc (PMOS gate-source cutoff)", f"{self.Cgs_pc:.3e}", "F"],
            ["Cgd_pc (PMOS gate-drain cutoff)", f"{self.Cgd_pc:.3e}", "F"],
            ["Cgs_nt (NMOS gate-source triode)", f"{self.Cgs_nt:.3e}", "F"],
            ["Cgd_nt (NMOS gate-drain triode)", f"{self.Cgd_nt:.3e}", "F"],
            ["Cgs_pt (PMOS gate-source triode)", f"{self.Cgs_pt:.3e}", "F"],
            ["Cgd_pt (PMOS gate-drain triode)", f"{self.Cgd_pt:.3e}", "F"],
            ["Cdb_nc (NMOS drain-body cutoff)", f"{self.Cdb_nc:.3e}", "F"],
            ["Cdb_pc (PMOS drain-body cutoff)", f"{self.Cdb_pc:.3e}", "F"],
            ["Cdb_nt (NMOS drain-body triode)", f"{self.Cdb_nt:.3e}", "F"],
            ["Cdb_pt (PMOS drain-body triode)", f"{self.Cdb_pt:.3e}", "F"],
            ["Cgb_nt (NMOS gate-body triode)", f"{self.Cgb_nt:.3e}", "F"],
            ["Cgb_pt (PMOS gate-body triode)", f"{self.Cgb_pt:.3e}", "F"]
        ]
        
        print(f"\n{Fore.CYAN}MOS CAPACITANCES (ALL IN FARADS):")
        print(tabulate(cap_params, tablefmt="fancy_grid"))
