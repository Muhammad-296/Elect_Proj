from colorama import Fore, Style, init

# Import modules
try:
    from constants import CMOSDatasheet
    from mosfet import MOSFET
    from logic_minimizer import LogicMinimizer
    from design_implementer import DesignImplementer
    from comparator import Comparator
except ImportError as e:
    print(f"{Fore.RED}Import Error: {e}")
    print(f"{Fore.YELLOW}Please ensure all modules are in the same directory.")
    exit(1)

# Initialize colorama
init(autoreset=True)

def main():
    print("\n" + Fore.CYAN + "="*80)
    print(Fore.CYAN + "   CMOS LOGIC ANALYZER WITH EXACT DELAY AND AREA CALCULATIONS")
    print(Fore.CYAN + "="*80)
    
    try:
        # Technology selection
        print("\n" + Fore.CYAN + "Available CMOS Technologies:")
        tech_names = list(CMOSDatasheet.datasheets.keys())
        for i, name in enumerate(tech_names, 1):
            print(f"{Fore.YELLOW}{i}. {Fore.GREEN}{name}")
        
        choice = int(input(f"\n{Fore.CYAN}Select technology number: "))
        tech_name = tech_names[choice-1]
        tech = CMOSDatasheet.datasheets[tech_name]
        
        print(f"\n{Fore.GREEN}Selected: {tech_name}")
        
        # MOSFET parameters
        Wn = float(input(f"{Fore.CYAN}Enter NMOS width Wn (µm): "))
        Ln = float(input(f"{Fore.CYAN}Enter NMOS length Ln (µm): "))
        Wp = float(input(f"{Fore.CYAN}Enter PMOS width Wp (µm): "))
        Lp = float(input(f"{Fore.CYAN}Enter PMOS length Lp (µm): "))
        VBS = float(input(f"{Fore.CYAN}Enter body-source voltage VBS (V): "))
        
        mosfet = MOSFET(tech, Wn, Ln, Wp, Lp, VBS)
        mosfet.display_parameters()
        
        # Logic minimization
        logic = LogicMinimizer(mosfet)
        logic.input_function()
        logic.quine_mccluskey()
        logic.generate_kmap()
        sop_terms = logic.generate_sop_expression()
        
        print("\n" + Fore.CYAN + "="*80)
        print(Fore.CYAN + "DESIGN IMPLEMENTATIONS WITH EXACT ANALYSIS")
        print(Fore.CYAN + "="*80)
        
        # Design implementations
        implementer = DesignImplementer(mosfet, sop_terms)
        nand_results = implementer.convert_to_nand_not()
        nor_results = implementer.convert_to_nor_not()
        
        # Comprehensive comparison
        comparator = Comparator(nand_results, nor_results, mosfet)
        winner, scores, areas, powers, bit_rates = comparator.compare_implementations()
        
        # Final summary
        print(f"\n{Fore.CYAN}{'='*80}")
        print(Fore.CYAN + "ANALYSIS COMPLETE - DESIGN SUMMARY")
        print(Fore.CYAN + "="*80)
        
        print(f"\n{Fore.GREEN}Recommended Design: {Fore.YELLOW}{winner}")
        print(f"{Fore.CYAN}Technology: {tech_name}")
        print(f"{Fore.CYAN}Key Metrics Comparison:")
        print(f"  • Area: {areas[0]:.2f} μm² (NAND) vs {areas[1]:.2f} μm² (NOR)")
        print(f"  • Power: {powers[0]:.2f} μW (NAND) vs {powers[1]:.2f} μW (NOR)")
        print(f"  • Speed: {bit_rates[0]/1e6:.2f} MHz (NAND) vs {bit_rates[1]/1e6:.2f} MHz (NOR)")
        
        print(f"\n{Fore.MAGENTA}Analysis Features Used:")
        print(f"{Fore.CYAN}  ✓ Exact NOT gate delay formulas")
        print(f"{Fore.CYAN}  ✓ Exact NAND gate delay formulas")
        print(f"{Fore.CYAN}  ✓ Exact NOR gate delay formulas")
        print(f"{Fore.CYAN}  ✓ Exact area calculation: n×W_n(l_n+2L_Dn) + w_p(l_p+2L_Dp)")
        print(f"{Fore.CYAN}  ✓ Maximum power calculation")
        
    except ValueError as e:
        print(f"{Fore.RED}Value Error: Please enter valid numerical values. {e}")
    except IndexError as e:
        print(f"{Fore.RED}Index Error: Invalid selection. {e}")
    except ZeroDivisionError as e:
        print(f"{Fore.RED}Calculation Error: Division by zero. {e}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected Error: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"\n{Fore.CYAN}{'='*80}")
    print(Fore.CYAN + "Analysis Complete. Thank you for using the CMOS Logic Analyzer!")
    print(Fore.CYAN + "="*80)

if __name__ == "__main__":
    main()