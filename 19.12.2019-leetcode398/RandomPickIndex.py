from random import randrange
class Solution(object):
    '''
    思路1: 统计所有index，然后用random.choice, 时间复杂度O(n), 空间O(m), m为重复数的个数
    思路2：排序，然后找到重复数字开始和结束的位置，后用randomint. 时间O(n*logn), 空间O(1)
    思路3: 对思路1空间改进到O(1)，时间复杂度变成O(2*n). 第一遍pass统计重复target的数量，
           第二遍随机选择第n个重复数的编号，遍历找到重复n次时的idx。
           Tip: 调用pick接口时，保存访问过数的count，省去一遍的pass
    '''
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.memoCount = {}
    
    def getCount(self, target): #返回target重复的次数(若访问过直接从memo中取出)
        if target in self.memoCount:
            return self.memoCount[target]
        count = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                count += 1
        self.memoCount[target] = count
        return count
    
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = self.getCount(target)
        randomCount = randrange(count) # [0,...count)#
        duplicateCount = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                if duplicateCount == randomCount:
                    return i
                duplicateCount += 1
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
