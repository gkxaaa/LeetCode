class Solution(object):
    '''
    方法一: 回溯。对于一个二叉递归树，如果没有限制先访问左节点后访问右节点，那就是二叉树的前序遍历。本情况中左右括号有两个限制
           1.左括号数不能超过n个 2.必须先有左括号才能有右括号不能(()))，即在任意一个位置往前统计右括号数小于等于左括号数。
           对于右括号数不超过n规定好边界条件自然满足
    方法二：动态规划思想。把问题化成子问题去解决，比如n=2可以由n=1的结果得来
    1. 在n=1的第一个括号（左括号）前面添加一对括号 --> ()()
    2. 第二个括号（右括号）前面添加一对括号 --> (())
    3. 在末尾添加一对括号 --> ()()， 此时和情况1重复
    此时可用递归或者迭代两种方法
    '''
    def generateParenthesis_rec(self,n):
        if n==1:return ['()']
        res = set()
        for bracket in self.generateParenthesis(n-1):
            for i in range(len(bracket)):
                res.add(bracket[0:i] + '()' + bracket[i:])
        return list(res)
    
    def generateParenthesis_dp(self,n):
        res = ['()']
        for j in range(n-1):
            tmp = set()
            for bracket in res:
                for i in range(len(bracket)):
                    tmp.add(bracket[0:i] + '()' + bracket[i:])
            res = tmp
        return list(res)
        
    def generateParenthesis_dfs(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(s='', left=0, right=0):
            if len(s)==2*n:
                res.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if left > right:
                backtrack(s+')', left, right+1)
        backtrack()
        return res
