from tabulate import tabulate
from colorama import Fore

class Comparator:
    def __init__(self, nand_results, nor_results, mosfet):
        self.nand_results = nand_results
        self.nor_results = nor_results
        self.mosfet = mosfet
    
    def compare_implementations(self):
        """Compare both implementations with exact analysis"""
        nand_total, nand_nand, nand_not, nand_perf, nand_gates = self.nand_results
        nor_total, nor_nor, nor_not, nor_perf, nor_gates = self.nor_results
        
        nand_delay, nand_bit_hz, nand_bit_mhz, nand_area, nand_power = nand_perf
        nor_delay, nor_bit_hz, nor_bit_mhz, nor_area, nor_power = nor_perf
        
        print("\n" + Fore.CYAN + "="*80)
        print(Fore.CYAN + "COMPREHENSIVE IMPLEMENTATION COMPARISON")
        print(Fore.CYAN + "="*80)
        
        # Gate count comparison
        gate_data = [
            ["NAND Gates", nand_nand, "N/A"],
            ["NOR Gates", "N/A", nor_nor],
            ["NOT Gates", nand_not, nor_not],
            ["Total Gates", nand_total, nor_total]
        ]
        
        print(f"\n{Fore.YELLOW}Gate Count Comparison:")
        headers = [f"{Fore.CYAN}Metric", f"{Fore.GREEN}NAND+NOT", f"{Fore.YELLOW}NOR+NOT"]
        print(tabulate(gate_data, headers=headers, tablefmt="fancy_grid"))
        
        # Performance comparison
        perf_data = [
            ["Total Delay (ns)", f"{nand_delay:.3f}", f"{nor_delay:.3f}"],
            ["Bit Rate (Hz)", f"{nand_bit_hz:.3e}", f"{nor_bit_hz:.3e}"],
            ["Bit Rate (MHz)", f"{nand_bit_mhz:.3f}", f"{nor_bit_mhz:.3f}"],
            ["Total Area (μm²)", f"{nand_area:.2f}", f"{nor_area:.2f}"],
            ["Max Power (μW)", f"{nand_power:.2f}", f"{nor_power:.2f}"]
        ]
        
        print(f"\n{Fore.YELLOW}Performance Comparison:")
        print(tabulate(perf_data, headers=headers, tablefmt="fancy_grid"))
        
        # Optimization Analysis
        print("\n" + Fore.CYAN + "="*80)
        print(Fore.CYAN + "OPTIMIZATION ANALYSIS")
        print(Fore.CYAN + "="*80)
        
        scores = {"NAND+NOT": 0, "NOR+NOT": 0}
        
        # Area comparison
        if nand_area < nor_area:
            area_saving = ((nor_area - nand_area) / nor_area) * 100
            print(f"\n{Fore.YELLOW}1. OPTIMUM AREA:")
            print(f"{Fore.GREEN}  • NAND+NOT design has optimum area: {nand_area:.2f} μm²")
            print(f"{Fore.CYAN}  • Area saving: {area_saving:.1f}% compared to NOR+NOT")
            scores["NAND+NOT"] += 1
            area_optimum = "NAND+NOT"
        elif nor_area < nand_area:
            area_saving = ((nand_area - nor_area) / nand_area) * 100
            print(f"\n{Fore.YELLOW}1. OPTIMUM AREA:")
            print(f"{Fore.GREEN}  • NOR+NOT design has optimum area: {nor_area:.2f} μm²")
            print(f"{Fore.CYAN}  • Area saving: {area_saving:.1f}% compared to NAND+NOT")
            scores["NOR+NOT"] += 1
            area_optimum = "NOR+NOT"
        else:
            area_optimum = "BOTH"
        
        # Power comparison
        if nand_power < nor_power:
            power_saving = ((nor_power - nand_power) / nor_power) * 100
            print(f"\n{Fore.YELLOW}2. MAXIMUM POWER:")
            print(f"{Fore.GREEN}  • NAND+NOT design has lower power: {nand_power:.2f} μW")
            print(f"{Fore.CYAN}  • Power saving: {power_saving:.1f}% compared to NOR+NOT")
            scores["NAND+NOT"] += 1
            power_optimum = "NAND+NOT"
        elif nor_power < nand_power:
            power_saving = ((nand_power - nor_power) / nand_power) * 100
            print(f"\n{Fore.YELLOW}2. MAXIMUM POWER:")
            print(f"{Fore.GREEN}  • NOR+NOT design has lower power: {nor_power:.2f} μW")
            print(f"{Fore.CYAN}  • Power saving: {power_saving:.1f}% compared to NAND+NOT")
            scores["NOR+NOT"] += 1
            power_optimum = "NOR+NOT"
        else:
            power_optimum = "BOTH"
        
        # Speed comparison
        if nand_bit_hz > nor_bit_hz:
            speed_improvement = ((nand_bit_hz - nor_bit_hz) / nor_bit_hz) * 100
            print(f"\n{Fore.YELLOW}3. MAXIMUM BIT RATE:")
            print(f"{Fore.GREEN}  • NAND+NOT design has higher bit rate: {nand_bit_mhz:.2f} MHz")
            print(f"{Fore.CYAN}  • Speed improvement: {speed_improvement:.1f}% compared to NOR+NOT")
            scores["NAND+NOT"] += 1
            speed_optimum = "NAND+NOT"
        elif nor_bit_hz > nand_bit_hz:
            speed_improvement = ((nor_bit_hz - nand_bit_hz) / nand_bit_hz) * 100
            print(f"\n{Fore.YELLOW}3. MAXIMUM BIT RATE:")
            print(f"{Fore.GREEN}  • NOR+NOT design has higher bit rate: {nor_bit_mhz:.2f} MHz")
            print(f"{Fore.CYAN}  • Speed improvement: {speed_improvement:.1f}% compared to NAND+NOT")
            scores["NOR+NOT"] += 1
            speed_optimum = "NOR+NOT"
        else:
            speed_optimum = "BOTH"
        
        # Gate count comparison
        if nand_total < nor_total:
            scores["NAND+NOT"] += 1
        elif nor_total < nand_total:
            scores["NOR+NOT"] += 1
        
        # Overall Recommendation
        print("\n" + Fore.CYAN + "="*80)
        print(Fore.CYAN + "OVERALL RECOMMENDATION")
        print(Fore.CYAN + "="*80)
        
        print(f"\n{Fore.MAGENTA}Optimization Scores:")
        print(f"{Fore.CYAN}  • NAND+NOT: {scores['NAND+NOT']}/4 optimization criteria")
        print(f"{Fore.CYAN}  • NOR+NOT: {scores['NOR+NOT']}/4 optimization criteria")
        
        if scores["NAND+NOT"] > scores["NOR+NOT"]:
            winner = "NAND+NOT"
            reason = "Superior in more optimization criteria"
        elif scores["NOR+NOT"] > scores["NAND+NOT"]:
            winner = "NOR+NOT"
            reason = "Superior in more optimization criteria"
        else:
            # Tie breaker based on area
            if nand_area < nor_area:
                winner = "NAND+NOT"
                reason = "Smaller area (tie breaker)"
            else:
                winner = "NOR+NOT"
                reason = "Smaller area (tie breaker)"
        
        print(f"\n{Fore.GREEN}RECOMMENDED DESIGN: {Fore.YELLOW}{winner}")
        print(f"{Fore.CYAN}Primary Reason: {reason}")
        
        # Key advantages
        print(f"\n{Fore.MAGENTA}Key Advantages of {winner}:")
        
        advantages = []
        if winner == "NAND+NOT":
            if nand_area < nor_area: 
                advantages.append(f"Smaller area by {abs(nor_area-nand_area):.2f} μm²")
            if nand_power < nor_power: 
                advantages.append(f"Lower power by {abs(nor_power-nand_power):.2f} μW")
            if nand_bit_hz > nor_bit_hz: 
                advantages.append(f"Higher speed by {abs(nand_bit_mhz-nor_bit_mhz):.1f} MHz")
            if nand_total < nor_total: 
                advantages.append(f"Fewer gates by {abs(nor_total-nand_total)}")
        else:
            if nor_area < nand_area: 
                advantages.append(f"Smaller area by {abs(nand_area-nor_area):.2f} μm²")
            if nor_power < nand_power: 
                advantages.append(f"Lower power by {abs(nand_power-nor_power):.2f} μW")
            if nor_bit_hz > nand_bit_hz: 
                advantages.append(f"Higher speed by {abs(nor_bit_mhz-nand_bit_mhz):.1f} MHz")
            if nor_total < nand_total: 
                advantages.append(f"Fewer gates by {abs(nand_total-nor_total)}")
        
        if advantages:
            for adv in advantages:
                print(f"{Fore.CYAN}  • {adv}")
        else:
            print(f"{Fore.CYAN}  • Similar performance across all metrics")
        
        return winner, scores, (nand_area, nor_area), (nand_power, nor_power), (nand_bit_hz, nor_bit_hz)