s = "   fly me   to   the moon  "
def lenght(s):
    s = s[::-1]
    b = ''
    for i, ch in enumerate(s):
        if ch == " ":
            b = s[:i]
            break
    return len(b)

#print(len(s))
def leng(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    print(i)
    j = i
    while j >= 0 and s[j] != ' ':
        j -= 1
    print(j)
    return i - j
#print(leng(s))
#print(b)
