class Bar:
    def __init__(self):
        self.res = 0
class Solution(object):
    def findTargetSumWays_rec(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        bar = Bar()
        def dfs(nums, i=0, s=0): # 34/139 cases passed, Time Limit Exceeded
            if i==len(nums):
                if s==S: bar.res += 1
                return
            dfs(nums,i+1, s+nums[i])
            dfs(nums,i+1, s-nums[i])
        #dfs(nums)
        
        def rec(nums,i=len(nums)-1,s=S): # 36/139 cases passed, Time Limit Exceeded
            if i==-1:
                return 1 if s==0 else 0
            return rec(nums,i-1,s-nums[i]) + rec(nums, i-1, s+nums[i])
        return rec(nums)
    
    def findTargetSumWays(self, nums, S):
        if not nums:return 0
        elif len(nums)==1:return 1 if nums[0]==abs(S) else 0
        MAX = sum(nums)
        dp = [[0]*(MAX+1) for _ in range(len(nums))] 
        if nums[0]==0:dp[0][nums[0]] = 4
        else: dp[0][nums[0]] = 2
        for i in range(1, len(nums)):
            for s in range(MAX+1):
                if abs(s-nums[i]) <= MAX:
                    dp[i][s] += dp[i-1][abs(s-nums[i])]
                if abs(s+nums[i]) <= MAX:
                    dp[i][s] += dp[i-1][abs(s+nums[i])]
                if i==len(nums)-1 and s==abs(S):return dp[i][s]/2
        return 0
