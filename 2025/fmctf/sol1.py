# import random
# import time
# seed = int(time.time())
# flag = list('o1me0T3}h_hTuvar_M4vdCFF3__{l3TY')
# random.seed(seed)
# random.shuffle(flag)
# flag = ''.join(flag)
# if 'FMCTF' in flag:
#     print(f'flag = {flag!r}')



import random

# Original flag characters in fixed order (unscrambled)
flag_chars = list('o1me0T3}h_hTuvar_M4vdCFF3__{l3TY')

# Choose a seed range (here we use an arbitrary range; adjust as needed)
# In practice you might choose a range around when the challenge was issued.
for seed in range(1678900000, 1678903600):
    random.seed(seed)
    candidate_chars = flag_chars.copy()
    random.shuffle(candidate_chars)
    candidate_flag = ''.join(candidate_chars)
    if "FMCTF" in candidate_flag:
        print(f"Seed: {seed}")
        print(f"Flag: {candidate_flag}")
        break

