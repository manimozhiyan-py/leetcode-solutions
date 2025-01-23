def palindrome(x):
    x = [x]  #str object is not iteratable so coverting is as list
    if x == x.reverse():
        return True
    return False
