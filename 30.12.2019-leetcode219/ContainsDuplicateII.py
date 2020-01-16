class Solution(object):
    '''
    思路1: Brute Force. Time O(n**2), Space O(1)
    思路2: 字典记下上一个数字的idx，看当前重复数字idx之差。小于k结束，大于k更新字典
           Time O(n), Space O(n)
    '''
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False
