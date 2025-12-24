import math
from tabulate import tabulate
from colorama import Fore, Style

from constants import PhysicalConstants

class MOSFET:
    def __init__(self, tech, Wn, Ln, Wp, Lp, VBS=0):
        self.tech = tech
        self.Wn, self.Ln = Wn, Ln
        self.Wp, self.Lp = Wp, Lp
        self.VBS = VBS
        self.constants = PhysicalConstants()
        self.calculate_parameters()
        self.calculate_capacitances()

    def calculate_parameters(self):
        self.Tox = self.tech["T_ox"] * 1e-9
        self.mu_n = self.tech["mu_on"] * 1e-4
        self.mu_p = self.tech["mu_op"] * 1e-4
        self.Cox = (self.tech["E_ox"] * self.constants.eps_0) / self.Tox
        self.Kn = self.mu_n * self.Cox * (self.Wn / self.Ln) * 1e6
        self.Kp = self.mu_p * self.Cox * (self.Wp / self.Lp) * 1e6
        self.NB_n = (self.tech["K_1n"] * self.Cox)**2 / (2 * self.constants.q * self.constants.eps_si)
        self.NB_p = (self.tech["K_1p"] * self.Cox)**2 / (2 * self.constants.q * self.constants.eps_si)
        self.psi_n = 2 * self.constants.Vt * math.log(self.NB_n / self.constants.ni)
        self.psi_p = 2 * self.constants.Vt * math.log(self.NB_p / self.constants.ni)
        self.Vth_n = self.tech["V_th_no"]
        self.Vth_p = self.tech["V_th_po"] if self.VBS == 0 else self.tech["V_th_po"] + self.tech["K_1p"] * (
            math.sqrt(self.psi_p + self.VBS) - math.sqrt(self.psi_p)
        )

    def calculate_capacitances(self):
        # Gate-body capacitances (cutoff)
        self.Cgb_nc = (self.Wn * self.Ln * self.Cox) / math.sqrt(1 + (4 * abs(self.tech["V_FB_n"])) / (self.tech["K_1n"]**2))
        self.Cgb_pc = (self.Wp * self.Lp * self.Cox) / math.sqrt(1 + (4 * abs(self.tech["V_FB_p"])) / (self.tech["K_1p"]**2))
        
        # Gate-drain/source capacitances (cutoff)
        self.Cgs_nc = self.Cgd_nc = self.Wn * self.tech["CGD_on"] * 1e-6
        self.Cgs_pc = self.Cgd_pc = self.Wp * self.tech["CGD_op"] * 1e-6
        
        # Gate-drain/source capacitances (triode)
        self.Cgs_nt = self.Cgd_nt = self.Cgs_nc + (self.Wn * self.Ln / 2) * self.Cox * 1e-12
        self.Cgs_pt = self.Cgd_pt = self.Cgs_pc + (self.Wp * self.Lp / 2) * self.Cox * 1e-12
        
        # Gate-body capacitances (triode)
        self.Cgb_nt = self.Cgb_nc * 0.5
        self.Cgb_pt = self.Cgb_pc * 0.5
        
        # Drain-body/source-body capacitances (cutoff)
        self.Cdb_nc = self.Csb_nc = self.tech["CJ_n"] * self.Wn * self.tech["L_Dn"] * 1e-12 + \
                                   self.tech["CJSW_n"] * 2 * (self.Wn + self.tech["L_Dn"]) * 1e-6
        self.Cdb_pc = self.Csb_pc = self.tech["CJ_p"] * self.Wp * self.tech["L_Dp"] * 1e-12 + \
                                   self.tech["CJSW_p"] * 2 * (self.Wp + self.tech["L_Dp"]) * 1e-6
        
        # Drain-body/source-body capacitances (triode)
        self.Cdb_nt = self.Csb_nt = self.Cdb_nc + (self.Wn * self.Ln / 2) * self.tech["CJ_p"] * 1e-12
        self.Cdb_pt = self.Csb_pt = self.Cdb_pc + (self.Wp * self.Lp / 2) * self.tech["CJ_n"] * 1e-12
        
        # Additional capacitances for exact delay formulas
        self.Cgd_pt = self.Cgs_pt  # Gate-drain PMOS triode
        self.Cgd_pc = self.Cgs_pc  # Gate-drain PMOS cutoff
        self.Cgd_nt = self.Cgs_nt  # Gate-drain NMOS triode
        self.Cgd_nc = self.Cgs_nc  # Gate-drain NMOS cutoff
        self.Cdb_pt = self.Cdb_pt  # Drain-body PMOS triode
        self.Cdb_pc = self.Cdb_pc  # Drain-body PMOS cutoff
        self.Cdb_nt = self.Cdb_nt  # Drain-body NMOS triode
        self.Cdb_nc = self.Cdb_nc  # Drain-body NMOS cutoff
        self.Cgb_pc = self.Cgb_pc  # Gate-body PMOS cutoff
        self.Cgb_pt = self.Cgb_pt  # Gate-body PMOS triode
        self.Cgb_nc = self.Cgb_nc  # Gate-body NMOS cutoff
        self.Cgb_nt = self.Cgb_nt  # Gate-body NMOS triode

    def display_parameters(self):
        params_table = [
            [f"{Fore.CYAN}Parameter", f"{Fore.CYAN}Value"],
            ["Cox (F/m²)", f"{Fore.YELLOW}{self.Cox:.3e}"],
            ["Kn (μA/V²)", f"{Fore.YELLOW}{self.Kn:.3e}"],
            ["Kp (μA/V²)", f"{Fore.YELLOW}{self.Kp:.3e}"],
            ["Vth_n (V)", f"{Fore.BLUE}{self.Vth_n:.3f}"],
            ["Vth_p (V)", f"{Fore.BLUE}{self.Vth_p:.3f}"]
        ]
        
        cap_table = [
            [f"{Fore.CYAN}Capacitance", f"{Fore.CYAN}Value (F)"],
            ["Cgd_pt (PMOS triode)", f"{Fore.YELLOW}{self.Cgd_pt:.3e}"],
            ["Cgd_pc (PMOS cutoff)", f"{Fore.YELLOW}{self.Cgd_pc:.3e}"],
            ["Cgd_nt (NMOS triode)", f"{Fore.YELLOW}{self.Cgd_nt:.3e}"],
            ["Cgd_nc (NMOS cutoff)", f"{Fore.YELLOW}{self.Cgd_nc:.3e}"],
            ["Cdb_pt (PMOS triode)", f"{Fore.YELLOW}{self.Cdb_pt:.3e}"],
            ["Cdb_pc (PMOS cutoff)", f"{Fore.YELLOW}{self.Cdb_pc:.3e}"],
            ["Cdb_nt (NMOS triode)", f"{Fore.YELLOW}{self.Cdb_nt:.3e}"],
            ["Cdb_nc (NMOS cutoff)", f"{Fore.YELLOW}{self.Cdb_nc:.3e}"],
            ["Cgb_pc (PMOS cutoff)", f"{Fore.YELLOW}{self.Cgb_pc:.3e}"],
            ["Cgb_pt (PMOS triode)", f"{Fore.YELLOW}{self.Cgb_pt:.3e}"],
            ["Cgb_nc (NMOS cutoff)", f"{Fore.YELLOW}{self.Cgb_nc:.3e}"],
            ["Cgb_nt (NMOS triode)", f"{Fore.YELLOW}{self.Cgb_nt:.3e}"]
        ]
        
        print("\n" + Fore.CYAN + "="*50)
        print(Fore.CYAN + "TRANSISTOR PARAMETERS")
        print(Fore.CYAN + "="*50)
        print(tabulate(params_table, tablefmt="fancy_grid"))
        print("\n" + Fore.CYAN + "MOS CAPACITANCES (F) FOR DELAY CALCULATIONS")
        print(Fore.CYAN + "="*50)
        print(tabulate(cap_table, tablefmt="fancy_grid"))