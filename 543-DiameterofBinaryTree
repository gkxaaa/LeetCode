# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec_max(root):
            if not root:
                return -1
            left_len = rec_max(root.left) + 1
            right_len = rec_max(root.right) + 1
            self.ans = max(self.ans, left_len+right_len)
            return max(left_len, right_len)
        rec_max(root)
        return self.ans
        
