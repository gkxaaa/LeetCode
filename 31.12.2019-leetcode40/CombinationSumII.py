class Solution(object):
    '''
    思路1: dfs遍历结构，每个数都可以选或者不选。当和超过target时或到头时返回
    '''
        
    def combinationSum2(self, candidates, target):
        res = set()
        candidates.sort()
        def dfs(candidates, i=0, comb=[], SUM=0):
            if i >= len(candidates):
                if SUM == target:
                    res.add(tuple(comb))
                return
            if SUM+candidates[i]<=target:
                dfs(candidates, i+1, comb+[candidates[i]], SUM+candidates[i])
            dfs(candidates, i+1, comb, SUM)
        dfs(candidates)
        return map(list, res)
        
