import re
from z3 import Solver, Int, Sum, sat

def parse_equations(content):
    equations = []
    idx = 0
    while len(equations) < 28 and idx < len(content):
        start_if = content.find("if (*piVar28 *", idx)
        if start_if == -1:
            break
        start_paren = start_if + 3
        end_paren = content.find(')', start_paren)
        if end_paren == -1:
            break
        
        condition_str = content[start_paren + 1:end_paren]
        if '==' not in condition_str:
            idx = end_paren
            continue
        
        parts = condition_str.split('==', 1)
        expr_str = parts[0].strip()
        const_str = parts[1].strip()
        
        terms = [term.strip() for term in re.split(r'\+', expr_str)]
        if len(terms) < 28:
            idx = end_paren
            continue
        
        coeffs = [0] * 28
        term0 = terms[0]
        parts0 = term0.split('*')
        if not parts0:
            idx = end_paren
            continue
        coeff27_str = parts0[-1].strip()
        try:
            coeff27 = int(coeff27_str, 0)
        except:
            idx = end_paren
            continue
        coeffs[27] = coeff27
        
        for i in range(1, 28):
            term = terms[i]
            parts_term = term.split('*')
            if not parts_term:
                coeff = 0
            else:
                coeff_str = parts_term[-1].strip()
                try:
                    coeff = int(coeff_str, 0)
                except:
                    coeff = 0
            coeffs[i - 1] = coeff
        
        try:
            constant = int(const_str, 0)
        except:
            constant = 0
        
        equations.append((coeffs, constant))
        idx = end_paren
    
    return equations

def main():
    with open('pass_check.txt', 'r') as file:
        content = file.read()
    
    equations = parse_equations(content)
    if len(equations) != 28:
        print(f"Found {len(equations)} equations, need 28.")
        return
    
    A = []
    b = []
    for coeffs, const in equations:
        A.append(coeffs)
        b.append(const)
    
    s = Solver()
    x = [Int(f'x_{i}') for i in range(28)]
    for i in range(28):
        s.add(Sum([A[i][j] * x[j] for j in range(28)]) == b[i])
    for i in range(28):
        s.add(x[i] >= 32, x[i] <= 126)
    
    if s.check() == sat:
        m = s.model()
        flag = ''.join(chr(m[x[i]].as_long()) for i in range(28))
        print("Flag:", flag)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()