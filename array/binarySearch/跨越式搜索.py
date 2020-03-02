# 整数数组nums，相邻数字相差绝对值为1,给定target，求target在数组中index
# 思路：类似于桶的想法，数组第一个数为array[0], 要找的数为y，设t = abs(y - array[0]).就是从
       第一个数开始到第y个中间差t，可以是增的也可以是减的.

def find(nums, target):
    idx = 0
    while idx<len(nums):
        t = abs(target-nums[idx])
        if idx+t<len(nums) and nums[idx+t] == target:
            return idx+t
        else:
            idx += t
    return None
