'''
1. Brute Force: 先对nums排序，然后全排列，到了目标数组序列时标记一下，下一个序列就是答案。时间复杂度O(nlogn)+2**n
2. 只对当前数组操作，尝试从当前变到下一个字典序。最直接的想法是从后往前便利，碰到变小的情况就交换，尽管如此但有些情况不能满足。但比如1432，正确结果应该是2134，而直接换得到4132.
那如何处理呢? 这里是思维的难点，首先这不是递归回溯问题，也不是最优解问题，也不需要哈希，它是一个纯数组问题，没有别的巧思，只能通过遍历，写出一个规则让它得到结果。

1423->2143有什么规律呢，仔细思考一下规律就是，4碰到1时不直接换，而是回头再向右遍历找到一个刚好大于1的一个数，交换数值。最后从4开始后面的数排序. 进一步看，交换后4开始往后的数组是一个倒叙的数组，只需要首末两端两两呼唤即可
'''
class Solution(object):    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = len(nums)-1
        while idx>0 and nums[idx]<=nums[idx-1]:
            idx -= 1
        if idx==0:
            return nums.reverse()
        else:
            i = idx
            while i<len(nums) and nums[i]>nums[idx-1]:
                i += 1
            nums[idx-1], nums[i-1] = nums[i-1], nums[idx-1]
            left, right = idx, len(nums)-1
            while right>left:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
