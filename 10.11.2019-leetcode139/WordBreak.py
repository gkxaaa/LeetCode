class Bar:
    def __init__(self):
        self.res = False
class Solution(object):
    '''
    思路1：把问题想复杂了。以为s中间有一个词匹配成功消掉后，两边的次拼起来作为新的s继续重复上述步骤，
    看最后能消完。其实不需要拼，下面在每次消除时加了一个空格，最后若全是空格返回True
    思路2: 其实有些隐含条件，这里有一个条件是，s若从第一个字符开始往后匹配，只有匹配到了才有后续内容。
    '''
    def wordBreak(self, s, wordDict):
        if not s:return False
        wordSet = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[j] and s[j:i+1] in wordSet:
                    dp[i+1] = True
        return dp[-1]
    def wordBreak_dfs(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict.sort()
        bar = Bar()
        def dfs(s, wordDict):
            if not s.split():
                bar.res = True
            for cur_word in wordDict:
                if cur_word in s:
                    start = s.index(cur_word)
                    dfs(s[:start]+' '+s[start+len(cur_word):], wordDict)      
        dfs(s, wordDict)
        return bar.res
    
    def wordBreak_rec(self, s, wordDict):
        def rec(s, wordDict):
            if not s.split():
                return True
            valid = False
            for cur_word in wordDict:
                if cur_word in s:
                    start = s.index(cur_word)
                    valid = valid or rec(s[:start]+' '+s[start+len(cur_word):], wordDict)
            return valid
        return rec(s, wordDict)
        
