class Bar:
    def __init__(self):
        self.res = False
        
class Solution(object):
    '''
    思路一：Brute Force。从第一个数开始跳，从最大步数开始尝试所有可能，遇到0 break，若能到达最后返回True。
    可以用for循环遍历上述所有情况，但遍历过程是一个完美的树形递归结构，dfs或者递归都可以解决此问题，复杂度指数级别具体不好算
    思路二：其实核心问题是解决数组里面有0的问题，没有零返回true，有0的话看前面的数字是否能跳过0.时间复杂度O(n)
    '''
    def canJump_dp(self, nums): #Time Limit Exceeded
        if len(nums)==1:return True
        if nums[0]==0:return False
        dp = [False]*len(nums)
        dp[0] = True
        for i in range(1,len(nums)):
            for j in range(i):
                if dp[j] and nums[j]+j>=i:
                    dp[i] = True
                    break
        return dp[-1]
    
    # greedy 
    def canJump(self, nums):
        idx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i]>= idx:
                idx = i
        return True if idx==0 else False
    
    def canJump_dfs(self, nums): #Time Limit Exceeded
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_index = len(nums)-1
        bar = Bar()
        def dfs(nums, index=0):
            if index>=last_index:
                bar.res = True
                return 
            elif nums[index] == 0:
                return

            for i in range(nums[index],0,-1):
                dfs(nums, index+i)
        dfs(nums)
        return bar.res
    
    def canJump_rec(self, nums): #Time Limit Exceeded
        last_index = len(nums)-1
        def rec(nums, index=0):
            if index>=last_index:
                return True
            elif nums[index] == 0:
                return False
            tmp = False
            for i in range(nums[index],0,-1):
                tmp = tmp or rec(nums, index+i)
            return tmp
        return rec(nums)
    
    def canJump_wrong(self, nums):
        if len(nums)==0:return True
        if nums[0]==0:return False
        index = 0
        while index<len(nums):
            n = 0           
            while nums[index+n]==0:
                n += 1
            if nums[index-1] <= n and index+n < len(nums)-1:
                return False
            index += n+1
        return True
