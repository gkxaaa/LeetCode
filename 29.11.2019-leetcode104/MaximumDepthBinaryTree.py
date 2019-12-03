# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def maxDepth_bfs(self, root):
        queue = []
        queue.append((root,0))
        while queue:
            node, d = queue.pop(0)
            if node:
                queue.append((node.left, d+1))
                queue.append((node.right, d+1))
        return d
    
    def maxDepth(self, root):
        stack, res = [], -1
        stack.append((root,0))
        while stack:
            node, d = stack.pop()
            res = max(res, d)
            if node:
                stack.append((node.right, d+1))
                stack.append((node.left ,d+1))
        return res
