class Solution(object):
    '''
    思路1：Brute Force。依次为边长为1,2,3...n的正方形扫描。时间复杂度O(n**3)
    思路2: 动态规划。空间换时间，判断当前点是否是正方形的右下角顶点，看比它斜上方的点以及左边和上边的点，通过一种逻辑关系，可以是if语句也可以是运算符，得到当前值。
    '''
    def maximalSquare_mn(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                else:
                    dp[i+1][j+1] = 0
        return max(k for col in dp for k in col)**2
                        
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                else:
                    matrix[i][j] = 0
        return max(k for col in matrix for k in col)**2                
