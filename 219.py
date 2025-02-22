nums = [1, 0, 1, 1]
k = 1

def contains(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic.keys():
            dic[nums[i]] = i
        else:
            if abs(i - dic[nums[i]]) <= k:
                return True
            else:
                dic.update({nums[i]:i})
                print(dic)
    return False

def test():
    dic = {1:0, 2:1}
    for i in range(2):
        dic[i] = i + 1
    print(dic)

#test()

#print(contains(nums, k))