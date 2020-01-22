class Solution:
    '''
    思路1: dfs或bfs遍历，每一层子孩子数为当前number. 时间复杂度mean(nums)**n
    思路2: dp一维, Time O(n**3)， Space O(n)
    思路3: 贪心，从后往前看，每次都选择距离最远的上一步。O(n**2)
    思路4: 贪心，从前往后，每次跳时，跳到当前所能跳到范围内所有位置里下一步能跳到最远的
    '''
    def jump(self, nums):
        if len(nums)==1: return 0
        i, res = 0, 0
        while i<len(nums):
            furthest, best_step = -1, None
            for step in range(1,nums[i]+1):
                if i+step>=len(nums)-1:
                    return res+1
                elif nums[i+step]+i+step > furthest:
                    furthest = nums[i+step]+i+step
                    best_step = step
            i += best_step
            res += 1
        
    def jump_dp(self, nums: List[int]) -> int: # Time Limit Exceeded, 90 / 92 test cases passed.
        dp = [len(nums)]*(len(nums)+1)
        dp[1] = 0
        for i in range(1, len(dp)):
            for j in range(1, i):
                if nums[i-j-1] >= j:
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]

    def jump1(self, nums): # Time Limit Exceeded, 90 / 92 test cases passed.
        i, res = len(nums)-1, 0
        while i>0:
            for j in range(i):
                if nums[j] + j >= i:
                    i = j
                    res += 1
                    break
        return res
        
