def repeatedSubstringPattern(s: str) -> bool:
    substring = []
    string = []
    sub = ""
    i = 0
    while i < len(s):
        if s[i] not in substring:
            substring.append(s[i])
        else:
            sub = s[i:i + len(substring)]
            i += len(substring) - 1
        i += 1
    print(sub)
    if len(sub) <= len(substring):
        for j in sub:
            string.append(j)
        print(string)
        if string == substring:
            return True
        else:
            return False


#print(repeatedSubstringPattern("babbabbabbabbab"))
#s = "abababab"

#print(s[1:-1])