s = "race a car"
chardict = {}
for i in range(97, 123):
    chardict[chr(i)] = i


def valid_palindrome(s):
    chardict = {}
    for i in range(97, 123):
        chardict[chr(i)] = i
    pl = ""
    s = s.lower()
    for i in s:
        if i in chardict:
            pl += i
    print(pl)
    print(pl[::-1])
    return True if pl == pl[::-1] else False


def isal(s):
    s = s.lower()
    pl = ""
    for i in s:
        if i.isalpha():
          pl += i
    return True  if pl == pl[::-1] else False


def isPalindrome(s):
        chardict = {}
        for i in range(97, 123):
            chardict[chr(i)] = i
        pl = ""
        for i in s:
            if 65 <= ord(i) <= 90:
                pl += chr(ord(i) + 32)
            elif 97 <= ord(i) <= 122:
                pl += i
            elif 48 <= ord(i) <= 57:
                pl += i
        print(pl)
        return True if pl == pl[::-1] else False

#print(ord('0'),ord('P'))


def TwoPointer(s):
    l = 0
    pl = ''
    for i in s:
        if 65 <= ord(i) <= 90:
            pl += chr(ord(i) + 32)
        elif 87 <= ord(i) <= 112:
            pl += i
        elif 48 <= ord(i) <= 57:
            pl += i
    r = len(pl) - 1

    while r >= l:
        if pl[l] != pl[r]:
            return False
        r -= 1
        l += 1
    return True


#print(TwoPointer(s))