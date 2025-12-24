import math

class PhysicalConstants:
    q = 1.602e-19
    eps_0 = 8.854e-12
    eps_si = 11.7 * eps_0
    Vt = 0.0259
    ni = 1.45e16
    VDD = 5.0  # Supply voltage

class CMOSDatasheet:
    datasheets = {
        "1.0um CMOS": {"T_ox":20, "E_ox":3.9, "mu_on":450, "mu_op":180,
                       "V_th_no":0.9, "V_th_po":-0.9, "K_1n":0.55, "K_1p":0.6,
                       "CGD_on":0.5, "CGD_op":0.45, "CJ_n":0.9, "CJ_p":0.8,
                       "CJSW_n":0.35, "CJSW_p":0.3, "V_FB_n":-1.0, "V_FB_p":-0.4,
                       "L_Dn":2.5, "L_Dp":2.5},
        "0.8um CMOS": {"T_ox":16, "E_ox":3.9, "mu_on":460, "mu_op":185,
                       "V_th_no":0.8, "V_th_po":-0.85, "K_1n":0.5, "K_1p":0.55,
                       "CGD_on":0.42, "CGD_op":0.38, "CJ_n":0.8, "CJ_p":0.7,
                       "CJSW_n":0.3, "CJSW_p":0.26, "V_FB_n":-0.95, "V_FB_p":-0.35,
                       "L_Dn":2.0, "L_Dp":2.0},
        "0.6um CMOS": {"T_ox":12, "E_ox":3.9, "mu_on":470, "mu_op":190,
                       "V_th_no":0.75, "V_th_po":-0.8, "K_1n":0.45, "K_1p":0.5,
                       "CGD_on":0.35, "CGD_op":0.3, "CJ_n":0.7, "CJ_p":0.6,
                       "CJSW_n":0.26, "CJSW_p":0.22, "V_FB_n":-0.9, "V_FB_p":-0.3,
                       "L_Dn":1.7, "L_Dp":1.7},
        "0.5um CMOS": {"T_ox":10, "E_ox":3.9, "mu_on":460, "mu_op":190,
                       "V_th_no":0.7, "V_th_po":-0.8, "K_1n":0.4, "K_1p":0.5,
                       "CGD_on":0.3, "CGD_op":0.25, "CJ_n":0.6, "CJ_p":0.5,
                       "CJSW_n":0.22, "CJSW_p":0.18, "V_FB_n":-0.9, "V_FB_p":-0.3,
                       "L_Dn":1.5, "L_Dp":1.5},
        "0.35um CMOS": {"T_ox":7, "E_ox":3.9, "mu_on":500, "mu_op":200,
                        "V_th_no":0.5, "V_th_po":-0.6, "K_1n":0.35, "K_1p":0.45,
                        "CGD_on":0.25, "CGD_op":0.2, "CJ_n":0.5, "CJ_p":0.4,
                        "CJSW_n":0.18, "CJSW_p":0.15, "V_FB_n":-0.8, "V_FB_p":-0.25,
                        "L_Dn":1.2, "L_Dp":1.2}
    }