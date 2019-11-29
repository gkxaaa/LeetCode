class Board:
    def __init__(self):
        self.res = 0
class Solution(object):
    '''
    思路1: 这到题的难点在于本身构造或者检查BST是一个递归，要完成题目也需要递归，那么就把两种递归混淆到一起。凡是涉及到递归只需要思考两个问题：1. 目标是什么--求n为4时的BST数目 2.怎么通过递归得到目标。而不用去思考怎么遍历BST。
    动态规划的编程或数学意义上的本质就是当前状态可以由上一个状态，或者由之前的所有状态经过某种运算得到，类似于数学公式的递推式。在理解上的本质是大问题化解为子问题解决。
    '''
    def numTrees(self, n):
        dp = [1]+[0]*n
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[-1]
        
    def numTrees_confused(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = range(1,n+1)
        board = Board()
        def rec(nums_left, nums_right, i=0):
            if not num:
                if k==n:
                    return True
                return False
            for j in range(len(nums_left)):
                left = rec(nums_left[:j], nums_left[j+1:])
            for j in range(len(nums_right)):
                right = rec(nums_right[:j], nums_right[j+1:])
