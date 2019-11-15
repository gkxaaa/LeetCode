class Solution(object):
    def minPathSum(self, grid):
        n, m = len(grid[0]),len(grid) 
        for i in range(m):
            for j in range(n):
                if i==j==0:pass
                elif i==0:grid[i][j] += grid[i][j-1]
                elif j==0:grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    
    def minPathSum_dp(self, grid):
        n, m = len(grid[0]),len(grid) 
        dp = [[grid[0][0]]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==j==0:pass
                elif i==0:dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j==0:dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
    
    
    
    def minPathSum_rec(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i, j = len(grid)-1, len(grid[0])-1
        def rec(grid, i, j):
            if i==0:
                return sum(grid[i][:j+1])
            elif j==0:
                return sum([grid[k][j] for k in range(i+1)])
            return min(rec(grid,i-1,j), rec(grid,i,j-1)) + grid[i][j]
        return rec(grid, i, j)
        
