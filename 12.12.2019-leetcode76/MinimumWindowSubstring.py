from collections import Counter
class Solution(object):
    '''
    思路1：暴力，从窗长len(T)开始往后扫，每次用一个set看T中元素是否都在里面。时间复杂度O(n**2)空间O(n)
    思路2：滑动窗，当窗里包含了所有的字母后(满足要求了)，比较最小长度记下答案后最左边字符出列，右边元素继续遍历入列。需要注意的细节:
           1) 怎样才是包含了所有字母？必须用字典，每个字母都有而且每个字母的频率大于要求
           2) 自己写的程序速度和空间都比较差，看了答案可以从两方面优化：
               1.可以不用队列操作元素入列出列，直接用两个变量l, r代表左右边界，节省空间并加速
               2.在字典中检查每个字母频率时，每次我用了遍历，可以用一个变量required，其大小表示有多少个字母满足要求了。
    '''
    def minWindow(self, s, t):
        win = []
        tmp_len, res = len(s), ''
        i, d, sorted_t = 0, Counter(t), sorted(t)
        win_d = {}
        for i in range(len(s)):
            if s[i] in d:
                win.append(i)
                win_d[s[i]] = win_d.get(s[i], 0) + 1
            while sum(win_d.get(char,0)>=d[char] for char in d)>=len(d):
                left_idx = win.pop(0)
                win_d[s[left_idx]] = 0 if win_d[s[left_idx]]==0 else win_d[s[left_idx]]-1
                if i - left_idx + 1 <= tmp_len:
                    tmp_len = i - left_idx + 1
                    res = s[left_idx:i+1]
        return res
