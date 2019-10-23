class Solution:
    def __init__(self):
        self.mapping_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def letterCombinations_dfs(self, digits):
        res = []
        if not digits:return res
        def dfs(digits, comb=''):
            if not digits:
                res.append(comb)
                return
            for l in self.mapping_dict[digits[0]]:
                dfs(digits[1:], comb+l)
        
        dfs(digits)
        return res
