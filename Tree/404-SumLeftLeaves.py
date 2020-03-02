# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路：递归，Time O(n), Space O(n), 左子树中所有左叶子和加上右子树所有左叶子和.
          当node.left和node.right都为空是为叶子节点，但是到了叶子节点是本身是做节
          点还是右节点之根据当前node是不知道的，所以需要记下当前节点是最近父亲节点
          的左孩子还是右孩子。
    '''
    def sumOfLeftLeaves(self, root, cur_node='root'):
        if not root:
            return 0
        sum_left = self.sumOfLeftLeaves(root.left, 'left')
        sum_right = self.sumOfLeftLeaves(root.right, 'right')
        if cur_node=='left' and not root.left and not root.right:
            sum_left += root.val
        return sum_left + sum_right
        
