class Solution(object):
    '''
    思路一：Brute Force, 去掉非正整数并排序（n+n*log(n)），第一个数不为1返回1, 是1则往后遍
    历找到第一个不连续的数，如果都连续，返回最后一个数加一(n), 总共时间复杂度n*log(n)
    
    思路二；此题难点在于判断一个数组是否是连续整数并若不是找出开始不连续的数，可以找最小值和最
    大值求差看和数组长度是否相同，但这种方法不能定位不连续的数字位置。想到转化为set，从1开始递
    增，循环的判断是否在set中. 
    
    思路三：利用排序的思想（桶排序），从1开始把数字尽可能放在对的位置上，即[1,2,3,4,5...,N], 
    则第一个出现不和谐数的地方，即为所求数。需要注意的是数组内同时用index和nums[index]映射的问题
    '''
    def firstMissingPositive_set(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        MAX = max(nums)
        if MAX < 0: return 1
        nums_set = set(nums)
        for n in xrange(1, MAX+1):
            if n not in nums_set:
                return n
        return MAX+1
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def firstMissingPositive(self, nums):
        if not nums: return 1
        MAX = len(nums)
        # Sort array
        for i in range(len(nums)):
            # 这里有一个边界条件没考虑到，比如[3,1,3], 若nums[0] = nums[nums[0]-1]时，会
            # 一直互相交换死循环，需加上nums[i] != nums[nums[i]-1]. 同时发现条件nums[i]!=i+1已被包含在内, 可省去
            while 0<nums[i]<MAX+1 and nums[i]!=i+1 and nums[i] != nums[nums[i]-1]:
                self.swap(nums, i, nums[i]-1)
                #nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        # Check the unharmonious number
        for i in range(len(nums)):
            n = nums[i]
            if i+1!=n:
                return i+1
        return MAX+1
