def RomanToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    add = 0
    i = 0
    while i < len(s):
        print(i)
        if i != len(s)-1 and dic[s[i]] < dic[s[i+1]]:
            print(add)
            add += dic[s[i+1]] - dic[s[i]]
            print(f'at loop {add}')
            i += 1
            print(i)
        else:
            add += dic[s[i]]
            print(f'end : {add}')
        i += 1
        #print(add)
    return add
#print(RomanToInt("MCMXCIV"))