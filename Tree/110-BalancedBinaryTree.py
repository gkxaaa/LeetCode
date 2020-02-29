# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路：递归。判断当前节点所代表的数是否平衡树，需满足三点：
          1. 左子树为平衡树
          2. 右子树为平衡树
          3. 左右子树深度差小于等于1
          Time O(n) Space(n)
    '''
    def isBalanced(self, root: TreeNode) -> bool:
        def rec(root):
            if not root:
                return True, 0
            is_balance_l, d_l = rec(root.left)
            is_balance_r, d_r = rec(root.right)
            is_balance = is_balance_l and is_balance_r and abs(d_l-d_r)<=1
            depth = max(d_l, d_r)+1
            return (is_balance, depth)
        return rec(root)[0]
