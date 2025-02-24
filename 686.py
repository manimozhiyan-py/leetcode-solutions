a = "abcd"
b = "cdabcdab"
def repeatedStringMatch(a: str, b: str) -> int:
    limit = 0
    if len(b) != 0:
        limit = int(len(b)/len(a))
    if b in a :
        return 1
    elif not b:
        return 0
    else:
        for i in range(2, limit + 3):
            c = a*i
            print(c)
            if b in c:
                return i
        return -1
#print(repeatedStringMatch(a,b))
