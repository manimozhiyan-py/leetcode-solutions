import self


def prefix(strs):
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for other in strs:
            if i == len(other) or ch != other[i]:
                return strs[0][:i]
    return strs[0]

#print(prefix(["ab","a"]))


def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    lis = []
    for i in strs:
        lis.append(len(i))
    for i in range(min(lis)):
        new = set()
        for j in strs:
            new.add(j[i])
            print(new)
        if len(new) == 1:
            new = list(new)
            ans = ans + new[0]
            print(ans)
        else:
            break
    return (ans)
#print(longestCommonPrefix(self,["flower","flow","flight"]))