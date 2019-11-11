class Solution(object):
    def lengthOfLIS(self, nums):
        '''
        思路一：Brute Forst之dfs遍历。一般关于遍历的问题可以用loop循环，如果遍历的路程和递归树形结构相符的话用dfs
        第一层for循环，第二层从每个起点开始一个分支是当前数小于上一个数（不选），另一个分支是大于（选），O(n*2**n)
        思路二：动态规划思想（递归）。从后往前看，是否可以把问题化为子问题。[1,2,10,5]最后一个数选不选，要看前面
        nums[:-1]中的最长上升子序列的MAX是否小于当前数。小于当前则选，大于则不选。把前面的问题概括用一个打包的函数实现
        --递归思想。DP是用来优化递归，因递归函数会做很多重复计算，DP是从开始开始往后把状态保存在数组中，用时取
        '''
        def rec(nums,MAX=float('inf')):
            if len(nums)==0:
                return 0
            taken = 0
            if MAX>nums[-1]:
                taken = rec(nums[:-1], nums[-1]) + 1
            nottaken = rec(nums[:-1], MAX)
            return max(taken, nottaken)
        return rec(nums)
    
    def lengthOfLIS(self, nums):
        if not nums:return 0
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
