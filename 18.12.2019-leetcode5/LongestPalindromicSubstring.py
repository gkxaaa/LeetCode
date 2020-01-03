class Solution(object):
    '''
    思路1: Brute Force，从长到短检查每一个substring是否是回文串。
           遍历时间复杂度O(n**2),第一层是每个substring的起点，第二层是每个substring的长度，
           检查每个substring是否是回文平均需要O(n). 总体时间复杂度O(n**3)
    思路2：DP，问题可以被分解成子问题。dp[i,j] = True if dp[i+1, j-1] and s[i+1]==s[j-1]
           二维DP，Time O(n**2)，Space O(n**2)
    思路3: Expand，遍历每个字符和两两字符的空隙，膨胀到最大. Time O(n**2), Space O(1)
    '''
    def longestPalindrome(self, s):
        MAX, res = -1, ''
        for i in range(2*len(s)-1):
            (l,r) = (i-1,i+1) if i&1 else (i, i)
            while l>=0 and r<2*len(s)-1 and s[l//2]==s[r//2]:
                l -= 2
                r += 2
            start, end = (l+2)//2, (r-2)//2
            if end - start > MAX:
                MAX = end - start 
                res = s[start : end+1]
        return res
        
    def longestPalindrome_expand(self, s):
        MAX, res = -1, ''
        for i in range(2*len(s)-1):
            (l,r) = (i-1,i+1) if i&1 else (i, i)
            while l>=0 and r<2*len(s)-1:
                if s[l//2]==s[r//2]:
                    if r//2 - l//2 > MAX:
                        MAX = r//2 - l//2
                        res = s[l//2:r//2+1]
                    l -= 2
                    r += 2
                else:
                    break
        return res
        
    def longestPalindrome_bruteForce(self, s): # Time Limit Exceeded, 102/103 cases passed.
        if not s: return ''
        for length in range(len(s),0,-1):
            for start in range(len(s)+1-length):
                if self.is_palindromic(s[start:start+length]):
                    return s[start:start+length]
    def is_palindromic(self,s):
        l, r = 0, len(s)-1
        while r>l and s[l]==s[r]:
            l += 1
            r -= 1
        return r<=l
    
    def longestPalindrome_dp(self, s):
        if not s: return ''
        MAX, res = -1, s[0]
        dp = [[True]*len(s) for _ in range(len(s))]
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                is_palindrome = s[i]==s[j] and dp[i+1][j-1]
                dp[i][j] = is_palindrome
                if is_palindrome and j-i>MAX:
                    MAX, res = j-i, s[i:j+1]
        return res
        
        
    def longestPalindrome_old1(self, s):
        if len(s)<=1:return s
        max_len = 1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                l, r =i, i+1                
            else:
                l = r = i
            while l>0 and r<len(s)-1 and s[l] == s[r]:
                    if r - l + 1> max_len:
                        max_len = r - l + 1
                        res = s[l:r+1]
                    l -= 1
                    r += 1
        return max_len  
    
    def longestPalindrome_old2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:return s
        max_len, res = 1, s[0]
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i+1<len(s) and s[i]==s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                res = s[i:i+2]
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2, len(s)):
                dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                if dp[i][j] and j-i+1>max_len:
                    max_len = j - i + 1
                    res = s[i:j+1]
        return res
