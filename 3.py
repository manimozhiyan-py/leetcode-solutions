#Longest Substring Without Repeating Characters
s = "pwwkew"
store = ""
for i in s :
    if i not in store :
        store = store + i
    else :
        continue
print(store)
print(len(store))