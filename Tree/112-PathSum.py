# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路1: dfs. O(n) O(n)
    ''' 
    def hasPathSum_dfs(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        self.ans = False
        def dfs(root, path_sum=0):
            if not root:
                return
            if not root.left and not root.right and path_sum+root.val==sum:
                self.ans = True
            dfs(root.left, path_sum+root.val)
            dfs(root.right, path_sum+root.val)
        dfs(root)
        return self.ans
