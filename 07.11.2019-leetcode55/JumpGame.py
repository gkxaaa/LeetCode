class Bar:
    def __init__(self):
        self.res = False
        
class Solution(object):
    '''
    思路一：Brute Force。从第一个数开始跳，从最大步数开始尝试所有可能，遇到0 break，若能到达最后返回True。
    可以用for循环遍历上述所有情况，但遍历过程是一个完美的树形递归结构，dfs或者递归都可以解决此问题，复杂度指数级别具体不好算
    思路二：核心问题是解决数组里面有0的问题，没有零返回true，有0的话依次看前面的数字是否能跳过0, 时间复杂度O(n**2).
    思路三：DP动态规划. 问题可以转换为子问题，前面是否有一个位置可以到达最后一个位置，并且，前面这个位置也是可以到达的。可以把是否能
    到达最后一个位置的问题转化为-->是否能到达前面某一个位置的问题。每次缩小问题规模都需要对前面所有位置遍历，
    因为不一定从哪个位置跳过来，时间复杂度O(n**2)
    思路四：Greedy贪心算法。从后往前遍历，只要碰到前面一个可以到达最后位置的一点，那么后面的遍历只需关注是否能到当前点，先当与DP中省去了
    缩小问题规模时的遍历，就是只考虑当前最优解。
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
