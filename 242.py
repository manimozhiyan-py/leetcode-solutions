s = "a"
t = "ab"


def valid(s, t):
    Sdic, Tdic = {}, {}
    minVal = min(len(s), len(t))
    for i in range(minVal):
        if s[i] not in Sdic.keys():
            Sdic[s[i]] = 1
        elif s[i] in Sdic.keys():
            Sdic[s[i]] += 1
        if t[i] not in Tdic.keys():
            Tdic[t[i]] = 1
        elif t[i] in Tdic.keys():
            Tdic[t[i]] += 1
    #if Sdic.keys() != Tdic.keys():
    #    return False
    if Sdic == Tdic:
        print(Sdic, Tdic)
    return False
#print(valid(s, t))