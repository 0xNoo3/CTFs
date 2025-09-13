# Search v0-v7 solution and create full flag string.

# Precompute valid S1 values:
valid_s1 = set([11,22,33,44,55,66,77,88,99])

# Precompute triples v0,v1,v2:
triples = []
for v0 in range(10,36):
    for v1 in range(0,36):
        if v1 == v0: continue
        for v2 in range(0,36):
            if v2 == v1: continue
            if v0 + v1 + v2 in valid_s1:
                triples.append((v0,v1,v2))
print(f"Triples count: {len(triples)}") # should be 2895

# iterate triples
def val2char(v):
    if v < 10:
        return chr(ord('0') + v)
    else:
        return chr(ord('A') + (v-10))

solution = None
for (v0,v1,v2) in triples:
    S1 = v0+v1+v2
    threshold = 101 - S1
    # loop v3
    for v3 in range(0,36):
        if v3 == v2: continue
        leftover1 = threshold - v3
        # loop v7
        for v7 in range(0,36):
            # no adjacency constraint for v7 yet except with v6; will check later
            v5 = abs(v7 - v3)
            leftover2 = leftover1 - v5
            # skip if leftover2 > max possible v4+v6 which = 35+35=70
            if leftover2 > 70: continue
            # loop v4
            for v4 in range(0,36):
                if v4 == v3 or v4 == v5: continue
                leftover3 = leftover2 - v4
                min_v6 = max(0, leftover3)
                if min_v6 > 35: continue
                # loop v6 in domain [min_v6,35] excluding v4,v5,v7
                for v6 in range(min_v6,36):
                    if v6 == v4 or v6 == v5 or v6 == v7: continue
                    # adjacency constraints: ensure v6 != v5, v7 != v6; second holds.
                    # sumFirst8: v0+..+v7 >= 101?
                    # Already ensure by leftover3 <= v6 ensures threshold
                    # Now ensure v0+..+v7 >100: 
                    if (v0+v1+v2+v3+v4+v5+v6+v7) <= 100: 
                        continue
                    # V4 != V5, V6 != V4 and V6 != V5 already enforced.
                    # Now v0>=10 and v15 condition for later.
                    # v7 might be 0 or not. Choose quadruple x:
                    if v7 != 0:
                        x = 0
                    else:
                        x = 3
                    # ensure x<=32 for x+3 <=35 => x candidate valid set {0,3,...,33}
                    # here x is 0 or 3, so ok.
                    v8 = x
                    v9 = x+1
                    v10 = x+2
                    v11 = x+3
                    # ensure v8 != v7
                    if v8 == v7:
                        # skip and choose next x? Try x=3 for v7!=3
                        if x == 0:
                            x2 = 3
                            v8 = x2; v9 = x2+1; v10 = x2+2; v11 = x2+3
                            if v8 == v7: 
                                continue
                        else:
                            continue
                    # adjacency inside quadruple holds.
                    # Now greedy for v12..v15
                    # v12 != v11
                    if 0 != v11:
                        v12 = 0
                    else:
                        v12 = 1
                    # v13 != v12
                    if 0 != v12:
                        v13 = 0
                    else:
                        v13 = 1
                    # v14 != v13
                    if 0 != v13:
                        v14 = 0
                    else:
                        v14 = 1
                    # v15 <10 and !=v14
                    if 0 != v14:
                        v15 = 0
                    else:
                        v15 = 1
                    if v15 >= 10:
                        continue
                    # adjacency v15!=v14 ensures by choice
                    # v15<10 satisfied
                    # Now check all adjacency across v7-v8 and v11-v12
                    if v8 == v7: continue
                    if v12 == v11: continue
                    # For carefulness, check adjacency across v11-v12, v12-v13, v13-v14, v14-v15
                    if v13 == v12 or v14 == v13 or v15 == v14: continue
                    # Now we have full vector v[0..15]
                    v = [v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15]
                    # Final domain constraint: v15<10 and each v <=35
                    if any([x<0 or x>35 for x in v]): continue
                    if v15 >=10: continue
                    # last check for domain: all Vs <=35
                    # Also initial domain for all so ok.
                    solution = v
                    break
                if solution: break
            if solution: break
        if solution: break
    if solution: break

print("Solution vector v:", solution)
if solution:
    flag = ''.join(val2char(v) for v in solution)
    print("Flag string:", flag)
