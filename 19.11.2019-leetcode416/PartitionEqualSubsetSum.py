class Bar:
    def __init__(self):
        self.res = False

class Solution(object):
    '''
    问题拆解：数组加起来和是奇数不可能。若是偶数则有两个sum/2，问题变为是否能在数组中找到若干数和为target
    思路1：Brute Force之dfs遍历。每个数字都有可能选或者不选两种情况，遍历中一旦碰到和为target返回True
    思路2：DP动态规划
    '''
    def canPartition(self, nums): #Time Limit Exceeded, 28/105 cases passed.
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        if _sum%2==1:return False
        target = int(_sum/2)
        bar = Bar()
        
        def dfs(nums, i=0, s=0):
            if s==target:
                bar.res = True
                return
            if i==len(nums) or s+nums[i]>target: 
                return
            
            dfs(nums, i+1, s+nums[i])
            dfs(nums, i+1, s)
        dfs(nums)
        return bar.res
    
    def canPartition(self, nums):
        _sum = sum(nums)
        if _sum%2==1:return False
        target = int(_sum/2)
        dp = [[False]*(target+1) for _ in range(len(nums)+1)]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1, len(dp)):
            for v in range(1, target+1):
                if v-nums[i-1] >= 0:
                    dp[i][v] = dp[i-1][v-nums[i-1]] or dp[i-1][v]
                else:
                    dp[i][v] = dp[i-1][v]
        return dp[-1][-1]
