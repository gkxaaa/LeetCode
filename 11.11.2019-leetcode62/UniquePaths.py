class Solution(object):
    '''
    思路：这道题和Fibo数列几乎一样，除了是二维。每个dp[x][y]=dp[x-1][y] + dp[x][y-1]
    '''
    def uniquePaths_rec(self, m, n):
        if m==1 or n==1:
            return 1
        return self.uniquePaths(n-1, m) + self.uniquePaths(n, m-1)
    
    def uniquePaths(self, m, n):
        dp = [[1]*m for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
