# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
1. 类似的，显然要类用返回值递归。当当前root节点返回了p and q，当前root就是答案。
'''
class Solution(object):
    def __init__(self):
        self.res = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def rec_find(root):
            if not root:
                return False
            root_has = root==p or root==q
            left_has = rec_find(root.left) or root_has
            right_has = rec_find(root.right) or root_has          
            if int(left_has+right_has+root_has)>=2:
                self.res = root
            return left_has or right_has
        rec_find(root)
        return self.res
