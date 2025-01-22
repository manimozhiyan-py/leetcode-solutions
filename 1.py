''' test case
nums = [1, 3, 2, 4]
target = 6
'''
'''
def twoSum(nums,target):
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if i !=j  and  nums[i] + nums[j] == target:
                return [i,j]
'''
'''
def twosum1(nums,target):
    dic = {}
    for index,num in enumerate(nums):
        comp = target - num
        if comp not in dic:
            dic[num] = index
        else :
            return[dic[comp],index]
'''


def hash(nums, target):
    dic = {}
    for i, val in enumerate(nums):
        balance = target - val
        if balance in dic.keys():
            return [dic[balance], i]
        else:
            dic[val] = i
    return False
