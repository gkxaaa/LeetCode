class Solution:
    '''
    思路1: 暴力。从长到短在字符串上移动，每次判断里面是否有重复，知道第一次没重复，
          返回长度。Time O(n**2) Space O(1)
    思路2: 滑动窗口。窗里没有重复项时右移直到有重复项，有重复项时左移直到没有重复项
           直到右边界溢出. 窗中字母用哈希表记录，判断是否有重复项
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        d, res = dict(), 0
        while r<len(s):
            if s[r] not in d: #右移
                d[s[r]] = True
                r += 1
            else: #左移
                d.pop(s[l])
                l += 1
            res = max(res, r-l)
        return res
    
    def lengthOfLongestSubstring1(self, s: str) -> int:
        l = r = 0
        d, res = dict(), 0
        while r<len(s):
            while r<len(s) and s[r] not in d: #右移
                d[s[r]] = True
                r += 1
            res = max(res, r-l)
            while r<len(s) and s[r] in d: #左移
                d.pop(s[l])
                l += 1
        return res
