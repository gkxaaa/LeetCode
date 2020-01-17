class Solution(object):
    '''
    思路1: dfs递归
    思路2: dfs非递归
    '''
    def combinationSum(self, candidates, target):
        dp = [[()]] + [set() for _ in range(target)]
        candidates.sort()
        for n in candidates:
            for i in range(1,target+1):
                if i>=n:
                    dp[i] |= {elt + (n,) for elt in dp[i-n]}
        return map(list,dp[target])
    
    def combinationSum_dp(self, candidates, target):
        dp = [[()]] + [set() for _ in range(target)]
        candidates.sort()
        for i in range(1,target+1):
            for n in candidates:
                if i>=n:
                    dp[i] |= {tuple(sorted(elt + (n,))) for elt in dp[i-n]}
        return map(list,dp[target])
    
    def combinationSum_dfs2(self, candidates, target):
        stack = [(target, 0, ())]
        res = set()
        while stack:
            rest, idx, comb = stack.pop()
            if rest==0:
                res.add(comb)
            elif rest>0:
                for i in range(idx, len(candidates)):
                    stack.append((rest-candidates[i], i, comb+(candidates[i],)))
        return map(list, res)
    
    def combinationSum_dfs(self, candidates, target):
        res = set()
        def dfs(candidates, idx=0, SUM=0, comb=()):
            if SUM==target:
                res.add(comb)
            elif SUM>target:
                return
            for i in range(idx, len(candidates)):
                dfs(candidates, i, SUM+candidates[i], comb+(candidates[i],))
        dfs(candidates)
        return map(list, res)
