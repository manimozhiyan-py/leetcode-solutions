sentence = "i love eating burger"
searchWord = "burg"
lent = len(sentence)


def data(sentence):
    if sentence[len(sentence) - 1] != " ":
        sentence = sentence + " "
    l, r, count = 0, 0, 0
    dic = {}
    for i in range(len(sentence)):
        if sentence[i] == " ":
            count += 1
            if sentence[l:r] not in dic:
                dic[sentence[l:r]] = count
                if i + 1 != len(sentence):
                    l = r + 1
                else:
                    break
        r += 1
    for word in dic.keys():
        if len(word) >= len(searchWord):
            if word[0:len(searchWord)] == search:
                return dic[word]
    return -1





#print(data(sentence))