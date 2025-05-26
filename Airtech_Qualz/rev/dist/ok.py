    # reconstruct encoded_data
    import struct

    # values in hex
    vals = [
        0x3535556c4e62315b,
        0x4063312478402b40,
        0x4041432e4077246a,
        0x2d40356140333864,
    ]
    val5 = 0x5e31773b6523352d

    # initialize
    buf = bytearray(39)
    # fill first 4 values
    offsets = [0,8,16,24]
    for off, val in zip(offsets, vals):
        buf[off:off+8] = struct.pack("<Q", val)
    # fill val5 at offset31
    buf[31:31+8] = struct.pack("<Q", val5)

    # Represent encoded_data (list of ints)
    encoded = list(buf)
    # print hex
    print("Encoded hex:", "".join(f"{b:02x}" for b in encoded))

    # mapping function f(x) as per decompiled
    def compute_cVar3(x):
        # x: input byte int 0..255
        # char x: signed? But mapping uses byte operations.
        if x == 9:
            cVar3 = -0x14  # -20
        else:
            bVar2 = x ^ 9
            cVar3 = -5
            if bVar2 != 0x11:
                # compute new bVar2: (bVar2 -8) ^9
                bVar2 = ( (bVar2 - 8) & 0xFF ) ^ 9
                # case1 uppercase: if (bVar2 +0xBF)%256 <26
                if ((bVar2 + 0xBF) & 0xFF) < 0x1A:
                    b_temp = ((bVar2 - 0x34) % 0x1A) + 0x37
                    bVar2 = b_temp
                    c = (bVar2 ^ 9) - 3
                    cVar3 = c if c != 0 else 1
                # case2 lowercase: elif (bVar2 +0x9F)%256 <26
                elif ((bVar2 + 0x9F) & 0xFF) < 0x1A:
                    b_temp = ((bVar2 - 0x54) % 0x1A) + 0x57
                    cVar3 = (b_temp ^ 9) - 3
                else:
                    bVar2_2 = bVar2 - 10
                    cVar3 = -2
                    if bVar2_2 != 9:
                        c = (bVar2_2 ^ 9) - 3
                        cVar3 = c if c != 0 else 1
                    else:
                        cVar3 = -2
        # cVar3 is signed char? We treat cVar3 as signed int
        # But return range can be outside -128..127? Let's mod?
        # But treat direct int
        # cast to signed 8-bit
        if cVar3 < -128 or cVar3 > 127:
            # wrap into signed char
            cVar3 = ((cVar3 + 256) & 0xFF)
            if cVar3 >= 128:
                cVar3 -= 256
        return cVar3

    # Let's test mapping for some sample x values for encoded[0] to see mapping.
    encoded_signed = [(b if b < 128 else b-256) for b in encoded]
    print("encoded_signed:", encoded_signed)
    # Now for each position, find x in 0..255 such that compute_cVar3(x)==encoded_signed[i]
    flags = []
    for idx, target in enumerate(encoded_signed):
        candidates = []
        for x in range(256):
            if compute_cVar3(x) == target:
                candidates.append(x)
        flags.append(candidates)
        print(idx, target, len(candidates), candidates[:10])



    # build flag string using unique candidate per position
    flag = "".join(chr(cands[0]) for cands in flags)
    print(flag)