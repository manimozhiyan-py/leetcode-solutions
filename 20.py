def isvalid(s):
    stack = []
    dic = {"(" : ")", "[" : "]", "{" : "}"}
    for i in s:
        if i in dic.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                if dic[stack[-1]] == i:
                    print(stack[-1])
                    stack.pop()
                else:
                    return False
    return True if stack == [] else False



#print(isvalid("([])"))