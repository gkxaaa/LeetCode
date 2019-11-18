import math
class Solution(object):
    '''
    思路1: DP
    思路2: BFS
    '''
    def numSquares(self, target):
        queue = []
        queue.append((target,1))
        while queue:
            node, depth = queue.pop(0)
            n = int(math.sqrt(node))
            for j in range(n,0,-1):
                newnode = node-j**2
                if newnode==0:return depth
                queue.append((newnode, depth+1))
            
    def numSquares_dp(self, target):
        dp = [k for k in range(target+1)]
        for tar in range(1,target+1):
            n = int(math.sqrt(tar))
            for j in range(n):
                dp[tar] = min(dp[tar-(j+1)**2]+1, dp[tar])            
        return dp[-1]
            
    def numSquares_2d_wrong(self, tar):
        """
        :type n: int
        :rtype: int
        """
        n = int(math.ceil((math.sqrt(tar))))
        dp = [[0]*tar for _ in range(n)]
        for j in range(tar):
            dp[0][j] = j+1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1,n):
            for j in range(1,tar):
                if i**2<=j:
                    dp[i][j] = min(dp[i][i-j**2]+1, dp[i-1][j])
        return dp[-1][-1]
