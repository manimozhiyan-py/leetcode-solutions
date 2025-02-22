haystack = "mississippi"
needle = "issipi"
needle_count = len(needle) - 1
re = -1
def First_occurence(haystack,needle):
    if len(needle) > len(haystack):
        return -1
    else:
        for j, ne in enumerate(needle):
            for i in range(len(haystack) - len(needle)):
                if needle[j] == haystack[i]:
                    if needle[needle_count] == haystack[i + needle_count]:
                        return i

            return -1
def First(haystack,needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:len(needle)] == needle :
            return i
    return -1
def First_find(haystack,needle):
    return haystack.find(needle)
print(First_find(haystack,needle))