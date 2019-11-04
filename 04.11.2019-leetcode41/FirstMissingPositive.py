class Solution(object):
    '''
    思路一：Brute Force, 去掉非正整数并排序（n+n*log(n)），第一个数不为1返回1, 是1则往后遍
    历找到第一个不连续的数，如果都连续，返回最后一个数加一(n), 总共时间复杂度n*log(n)
    思路二；此题难点在于判断一个数组是否是连续整数并若不是找出开始不连续的数，可以找最小值和最
    大值求差看和数组长度是否相同，但这种方法不能定位不连续的数字位置。想到转化为set，从1开始递
    增，循环的判断是否在set中
    '''
    def firstMissingPositive(self, nums):
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
