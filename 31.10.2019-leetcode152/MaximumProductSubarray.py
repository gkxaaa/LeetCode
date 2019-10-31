class Solution(object):
    '''
    思路一Brute Force：从左到右分别每个元素作为起点开始往后扫，记录最大乘积序列，1+2+3...+n时间复杂度O(n**2),空间复杂度O(1).
    思路二：dp
    '''
    def maxProduct_BruteForce(self, nums):
        res = -float('inf')
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                res = max(res, product)
        return res
    
    def maxProduct(self, nums):
        # First row is mins, second row is maxs
        res = -float('inf')
        dp = [[1]*(len(nums)+1) for _ in range(2)]
        for i in range(1, len(nums)+1):   
            dp[1][i] = max(dp[1][i-1]*nums[i-1], dp[0][i-1]*nums[i-1], nums[i-1])
            dp[0][i] = min(dp[1][i-1]*nums[i-1], dp[0][i-1]*nums[i-1], nums[i-1])
            res = max(dp[1][i], res)   
        return res
    
    def maxProduct_genius(self, nums):
        A, B = nums, nums[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(A+B)
