from itertools import product
from tabulate import tabulate
from colorama import Fore, Style

class LogicMinimizer:
    def __init__(self, mosfet):
        self.num_vars = 0
        self.minterms = []
        self.dont_cares = []
        self.prime_implicants = []
        self.sop_mode = True
        self.mosfet = mosfet
    
    def input_function(self):
        print("\n" + Fore.CYAN + "LOGIC FUNCTION INPUT")
        while True:
            choice = input(f"{Fore.YELLOW}Use SOP (minterms) or POS (maxterms)? [S/P]: ").upper()
            if choice in ['S','P']: break
            print(Fore.RED + "Invalid input. Enter S or P.")

        self.sop_mode = (choice=='S')
        self.num_vars = int(input(f"{Fore.CYAN}Enter number of variables (2-6 recommended): "))
        
        if self.sop_mode:
            self.minterms = list(map(int,input(f"{Fore.CYAN}Enter minterms separated by commas: ").split(',')))
            dc_input = input(f"{Fore.CYAN}Enter don't care terms separated by commas (optional): ")
            self.dont_cares = list(map(int, dc_input.split(','))) if dc_input.strip() else []
        else:
            maxterms = list(map(int,input(f"{Fore.CYAN}Enter maxterms separated by commas: ").split(',')))
            all_terms = set(range(2**self.num_vars))
            self.minterms = list(all_terms - set(maxterms))
            dc_input = input(f"{Fore.CYAN}Enter don't care terms separated by commas (optional): ")
            self.dont_cares = list(map(int, dc_input.split(','))) if dc_input.strip() else []

    def quine_mccluskey(self):
        terms = self.minterms + self.dont_cares
        groups = {}
        for t in terms:
            ones = bin(t).count('1')
            groups.setdefault(ones, []).append((t, bin(t)[2:].zfill(self.num_vars)))
        
        prime_implicants = set()
        while groups:
            new_groups = {}
            marked = set()
            all_keys = sorted(groups.keys())
            for i in range(len(all_keys)-1):
                for a in groups[all_keys[i]]:
                    for b in groups[all_keys[i+1]]:
                        diff = [k for k in range(self.num_vars) if a[1][k]!=b[1][k]]
                        if len(diff)==1:
                            new_bin = ''.join(['-' if a[1][k]!=b[1][k] else a[1][k] for k in range(self.num_vars)])
                            new_groups.setdefault(new_bin.count('1'),[]).append((a[0],new_bin))
                            marked.add(a)
                            marked.add(b)
            
            for grp in groups.values():
                for item in grp:
                    if item not in marked:
                        prime_implicants.add(item[1])
            
            groups = new_groups
        
        self.prime_implicants = list(prime_implicants)

    def implicant_to_minterms(self, pi):
        dash_pos=[i for i,ch in enumerate(pi) if ch=='-']
        fixed_pos=[(i,int(ch)) for i,ch in enumerate(pi) if ch!='-']
        positions=[]
        
        for combo in product([0,1], repeat=len(dash_pos)):
            bin_list=list(pi)
            for idx,val in zip(dash_pos,combo): 
                bin_list[idx]=str(val)
            for idx,val in fixed_pos: 
                bin_list[idx]=str(val)
            positions.append(int(''.join(bin_list),2))
        
        return positions

    def generate_kmap(self):
        print("\n" + Fore.CYAN + "K-MAP WITH PRIME IMPLICANT GROUPS")
        size = 2**self.num_vars
        kmap = ['0']*size
        
        for m in self.minterms: 
            kmap[m]='1'
        for d in self.dont_cares: 
            kmap[d]='X'

        cell_groups=[[] for _ in range(size)]
        for i,pi in enumerate(self.prime_implicants):
            for idx in self.implicant_to_minterms(pi):
                cell_groups[idx].append(i)

        colors=[Fore.GREEN,Fore.MAGENTA,Fore.CYAN,Fore.YELLOW,Fore.BLUE,Fore.RED]
        
        def display_cell(idx):
            val = kmap[idx]
            grps = cell_groups[idx]
            if val=='X': 
                return Fore.WHITE + val + Style.RESET_ALL
            if grps:
                color = colors[grps[0]%len(colors)]
                if len(grps)>1:
                    return color + f"[{val}]" + Style.RESET_ALL
                return color + f"[{val}]" + Style.RESET_ALL
            return val

        if self.num_vars==2:
            table=[[display_cell(0),display_cell(1)],[display_cell(2),display_cell(3)]]
            headers=["B=0","B=1"]
            print(tabulate(table,headers=headers,showindex=["A=0","A=1"],tablefmt="fancy_grid"))
        elif self.num_vars==3:
            table=[[display_cell(0),display_cell(1),display_cell(3),display_cell(2)],
                   [display_cell(4),display_cell(5),display_cell(7),display_cell(6)]]
            headers=["C=0","C=1","C=3","C=2"]
            print(tabulate(table,headers=headers,showindex=["A=0","A=1"],tablefmt="fancy_grid"))
        elif self.num_vars==4:
            table=[[display_cell(0),display_cell(1),display_cell(3),display_cell(2)],
                   [display_cell(4),display_cell(5),display_cell(7),display_cell(6)],
                   [display_cell(12),display_cell(13),display_cell(15),display_cell(14)],
                   [display_cell(8),display_cell(9),display_cell(11),display_cell(10)]]
            headers=["CD=00","CD=01","CD=11","CD=10"]
            print(tabulate(table,headers=headers,showindex=["AB=00","AB=01","AB=11","AB=10"],tablefmt="fancy_grid"))

    def generate_sop_expression(self):
        print("\n" + Fore.CYAN + "MINIMIZED LOGIC FUNCTION (SOP)")
        print(Fore.CYAN + "="*60)
        
        sop_terms=[]
        for pi in self.prime_implicants:
            term=[]
            for i,ch in enumerate(pi):
                var=chr(65+i)
                if ch=='1': 
                    term.append(var)
                elif ch=='0': 
                    term.append(f"{var}'")
            sop_terms.append(''.join(term))
        
        sop_expression=' + '.join(sop_terms)
        print(f"{Fore.YELLOW}SOP Expression: {Fore.GREEN}F = {sop_expression}")
        return sop_terms