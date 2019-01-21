sDict = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
         "8" : 8, "9" : 9, "a" : 10, "b" : 11, "c" : 12, "d" : 13, "e" : 14, "f" : 15,
         "g" : 16, "h" : 17, "i" : 18, "j" : 19, "k" : 20, "l" : 21, "m" : 22, "n" : 23,
         "o" : 24, "p" : 25, "q" : 26, "r" : 27, "s" : 28, "t" : 29, "u" : 30, "v" : 31,
         "w" : 32, "x" : 33, "y" : 34, "z" : 35}


def eval_strfrac (s, base = 2):
    flt = 0.0
    if "." not in s:
        left = s
    else:
        left, right = s.split(".")
    for i in enumerate(reversed(left)):
        integer = sDict[i[1]]
        if integer >= base:
            raise ValueError
        flt += base**i[0] * integer
    if "." not in s:
        return flt
    for i in enumerate(right):
        integer = sDict[i[1]]
        if integer >= base:
            raise ValueError
        flt += base**-(i[0] + 1) * integer
    return flt
    

bDict = {"0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111",
         "8" : "1000", "9" : "1001", "a" : "1010", "b" : "1011", "c" : "1100", "d" : "1101", "e" : "1110", "f" : "1111",
        }


def fp_bin(v):
    vhex = v.hex()
    s_sign, r = vhex.split("0x")
    if s_sign == "":
        s_sign = "+"
    sig, v_exp = r.split("p")
    v_exp = int(v_exp)
    sig = sig.replace(".", "")
    s_bin = ""
    
    for i in enumerate(sig):
        bin_i = bDict[i[1]]
        s_bin += bin_i

        
    if float(v) != 0:
        while s_bin[0] == "0":
            s_bin = s_bin[1:]
          
    s_bin = s_bin[0] + "." + s_bin[1:].zfill(52)
    print ((s_sign, s_bin, v_exp))
    return (s_sign, s_bin, v_exp)

def eval_fp(sign, significand, exponent, base=2):
    assert sign in ['+', '-'], "Sign bit must be '+' or '-', not '{}'.".format(sign)
    #assert is_valid_strfrac(significand, base), "Invalid significand for base-{}: '{}'".format(base, significand)
    assert type(exponent) is int
    if sign == "+":
        sign = 1
    else:
        sign = -1
        
    s = eval_strfrac(significand, base)
    return (sign * s * (base**exponent))

def add_fp_bin(u, v, signif_bits):
    u_sign, u_signif, u_exp = u
    v_sign, v_signif, v_exp = v
    
    # You may assume normalized inputs at the given precision, `signif_bits`.
    assert u_signif[:2] == '1.' and len(u_signif) == (signif_bits+1)
    assert v_signif[:2] == '1.' and len(v_signif) == (signif_bits+1)

    u_num = eval_fp(u_sign, u_signif, u_exp)
    v_num = eval_fp(v_sign, v_signif, v_exp)

    sum_uv = u_num + v_num

    bin_sign, bin_signif, bin_exp = fp_bin(sum_uv)
    signif = bin_signif[:signif_bits]

    return (bin_sign, signif, bin_exp)
    
    
    
    
