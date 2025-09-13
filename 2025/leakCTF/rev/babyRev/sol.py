

# build the forward remap
remap = { i: chr(i) for i in range(128) }
qwerty = "qwertyuiopasdfghjklzxcvbnm"
for idx, ch in enumerate(qwerty):
    remap[ord('a') + idx] = ch

# build the inverse map
inv = { v: chr(k) for k, v in remap.items() }


flag = "L3AK{ngx_qkt_fgz_ugffq_uxtll_dt}"

# compute what to type:
translated = []
for c in flag:
    if c in inv:
        translated.append(inv[c])
    else:
        # pass through bytes that weren’t in remap
        translated.append(c)
print("Type this at the prompt:")
print("".join(translated))
