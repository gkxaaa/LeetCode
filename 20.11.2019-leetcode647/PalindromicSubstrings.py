class Solution(object):
    '''
    思路1：Brute Force。两层loop O(n**2)，每次检查子字符串是否是回文O(n)。共O(n**3)
    思路2：DP, 状态dp[i][j]：字符串s从位置i到j回文串的个数，为0或1两种可能。
              递推：dp[i][j] = 1, if dp[i+1][j-1]>0 and s[i]==s[j]
           难点在于i+1和j-1造成的遍历顺序调整。利用2D思维这样理解：dp[i+1][j-1]是dp[i][j]
           左下角的数。所以i应该从下往上遍历，j从左到右或从右到左都可以。O(n**2)
    思路3：膨胀气泡
    '''
    def countSubstrings_dp(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:return 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j] = 1
                elif j-i==1 and s[i]==s[j]:
                    dp[i][j] = 1
                elif dp[i+1][j-1] > 0 and s[i]==s[j]:
                    dp[i][j] = 1
        return sum(value for col in dp for value in col)
    
    def countSubstrings(self, s):
        if not s:return 0
        n, res = len(s), 0
        for i in range(1,2*n):
            if i & 1: l, r = i, i
            else: l, r = i-1, i+1
            while 0<=l<=r<2*n and s[l//2]==s[r//2]:
                res += 1
                l -= 2
                r += 2
        return res
