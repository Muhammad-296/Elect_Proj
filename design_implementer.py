from tabulate import tabulate
from colorama import Fore

from performance_analyzer import PerformanceAnalyzer

class DesignImplementer:
    def __init__(self, mosfet, sop_terms):
        self.mosfet = mosfet
        self.sop_terms = sop_terms
        self.analyzer = PerformanceAnalyzer(mosfet)
    
    def convert_to_nand_not(self):
        print("\n" + Fore.CYAN + "="*60)
        print(Fore.CYAN + "DESIGN 1: NAND + NOT IMPLEMENTATION")
        print(Fore.CYAN + "="*60)
        
        gate_details = []
        
        # Count NOT gates for complemented variables
        all_complements = []
        for term in self.sop_terms:
            i = 0
            while i < len(term):
                if i + 1 < len(term) and term[i+1] == "'":
                    all_complements.append(term[i])
                    i += 2
                else:
                    i += 1
        
        unique_complements = list(set(all_complements))
        not_count = len(unique_complements)
        for var in unique_complements:
            gate_details.append(("NOT", 1, f"Complement: {var}'"))
        
        # Count NAND gates for product terms
        nand_count_for_terms = 0
        for idx, term in enumerate(self.sop_terms):
            literals = []
            i = 0
            while i < len(term):
                if i + 1 < len(term) and term[i+1] == "'":
                    literals.append(f"{term[i]}'")
                    i += 2
                else:
                    literals.append(term[i])
                    i += 1
            
            if len(literals) > 0:
                nand_count_for_terms += 1
                gate_details.append(("NAND", len(literals), f"Product term: {term}"))
        
        # Inverters for De Morgan's
        inverter_count = len(self.sop_terms)
        for i in range(inverter_count):
            gate_details.append(("NOT", 1, f"Inverter for De Morgan's"))
        
        # Final NAND gate
        gate_details.append(("NAND_Final", len(self.sop_terms), "Final OR implementation"))
        
        total_nand = nand_count_for_terms + 1  # +1 for final NAND
        total_not = not_count + inverter_count
        total_gates = total_nand + total_not
        
        # Display implementation
        print(f"\n{Fore.YELLOW}Implementation Steps:")
        print(f"{Fore.GREEN}1. NOT gates for complemented variables:")
        if unique_complements:
            for var in unique_complements:
                print(f"   NOT Gate: {var}' = NOT({var})")
        
        print(f"\n{Fore.GREEN}2. NAND gates for product terms:")
        for i, term in enumerate(self.sop_terms):
            literals = [c for c in term if c not in ["'", "+"]]
            if len(literals) > 0:
                print(f"   NAND Gate {i+1}: {len(literals)} inputs → {term}")
        
        print(f"\n{Fore.GREEN}3. Invert first-level outputs:")
        print(f"   {inverter_count} NOT gates")
        
        print(f"\n{Fore.GREEN}4. Final NAND gate (implements OR):")
        print(f"   NAND Gate: {len(self.sop_terms)} inputs → F")
        
        print(f"\n{Fore.CYAN}Gate Count Summary:")
        summary_data = [
            ["NAND gates for product terms", nand_count_for_terms],
            ["NOT gates for complements", not_count],
            ["NOT gates for inversion", inverter_count],
            ["Final NAND gate", 1],
            ["Total NAND gates", total_nand],
            ["Total NOT gates", total_not],
            ["TOTAL GATES", total_gates]
        ]
        print(tabulate(summary_data, tablefmt="fancy_grid"))
        
        # Performance analysis
        perf_results = self.analyzer.analyze_nand_design(total_nand, total_not, gate_details)
        
        return total_gates, total_nand, total_not, perf_results, gate_details
    
    def convert_to_nor_not(self):
        print("\n" + Fore.CYAN + "="*60)
        print(Fore.CYAN + "DESIGN 2: NOR + NOT IMPLEMENTATION")
        print(Fore.CYAN + "="*60)
        
        gate_details = []
        
        # Count NOT gates for complemented variables
        all_complements = []
        for term in self.sop_terms:
            i = 0
            while i < len(term):
                if i + 1 < len(term) and term[i+1] == "'":
                    all_complements.append(term[i])
                    i += 2
                else:
                    i += 1
        
        unique_complements = list(set(all_complements))
        not_count = len(unique_complements)
        for var in unique_complements:
            gate_details.append(("NOT", 1, f"Complement: {var}'"))
        
        # Count NOR gates for product terms
        nor_count_for_terms = 0
        for idx, term in enumerate(self.sop_terms):
            literals = []
            i = 0
            while i < len(term):
                if i + 1 < len(term) and term[i+1] == "'":
                    literals.append(f"{term[i]}'")
                    i += 2
                else:
                    literals.append(term[i])
                    i += 1
            
            if len(literals) > 0:
                nor_count_for_terms += 1
                gate_details.append(("NOR", len(literals), f"Product term: {term}"))
        
        # Final NOR gate
        gate_details.append(("NOR_Final", len(self.sop_terms), "Final OR implementation"))
        
        total_nor = nor_count_for_terms + 1  # +1 for final NOR
        total_not = not_count
        total_gates = total_nor + total_not
        
        # Display implementation
        print(f"\n{Fore.YELLOW}Implementation Steps:")
        print(f"{Fore.GREEN}1. NOT gates for complemented variables:")
        if unique_complements:
            for var in unique_complements:
                print(f"   NOT Gate: {var}' = NOT({var})")
        
        print(f"\n{Fore.GREEN}2. NOR gates for product terms:")
        for i, term in enumerate(self.sop_terms):
            literals = [c for c in term if c not in ["'", "+"]]
            if len(literals) > 0:
                print(f"   NOR Gate {i+1}: {len(literals)} inputs → {term}")
        
        print(f"\n{Fore.GREEN}3. Final NOR gate (implements OR):")
        print(f"   NOR Gate: {len(self.sop_terms)} inputs → F")
        
        print(f"\n{Fore.CYAN}Gate Count Summary:")
        summary_data = [
            ["NOT gates for complements", not_count],
            ["NOR gates for product terms", nor_count_for_terms],
            ["Final NOR gate", 1],
            ["Total NOR gates", total_nor],
            ["Total NOT gates", total_not],
            ["TOTAL GATES", total_gates]
        ]
        print(tabulate(summary_data, tablefmt="fancy_grid"))
        
        # Performance analysis
        perf_results = self.analyzer.analyze_nor_design(total_nor, total_not, gate_details)
        
        return total_gates, total_nor, total_not, perf_results, gate_details