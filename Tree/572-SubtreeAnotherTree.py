# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路：两个函数。遍历树s，每次比较s和t是否是相同的树，是则返回True
    '''
    def isSame(self, s, t):
        if not s and not t: return True
        elif not s: return False
        elif not t: return False
        left_subtree = self.isSame(s.left, t.left)
        right_subtree = self.isSame(s.right, t.right)
        return left_subtree and right_subtree and s.val==t.val
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.ans = False
        def dfs(s):
            if not s or self.ans:
                return 
            if s.val==t.val:
                self.ans = self.isSame(s, t)
            dfs(s.left)
            dfs(s.right)
        dfs(s)
        return self.ans
        
    def isSubtree_rec(self, s: TreeNode, t: TreeNode) -> bool:
        def rec(s):
            if not s:
                return False
            is_same = False
            if s.val==t.val:
                is_same = self.isSame(s, t)
            left = rec(s.left)
            right = rec(s.right)
            return left or right or is_same
        return rec(s)
