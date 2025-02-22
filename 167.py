def twosum(numbers, target):
    l, r = 0, len(numbers) - 1
    #sums = numbers[l] + numbers[r]
    while l < r:
        sums = numbers[l] + numbers[r]
        if sums > target:
            print(sums)
            r -= 1
            print(str(r) + " r")
        elif sums < target:
            l += 1
            print(l)
        if sums == target:
            return [l + 1, r + 1]


#print(twosum([2, 7, 11, 15], 9))
