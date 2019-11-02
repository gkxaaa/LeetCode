# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    思路：要构建一颗二叉树或者一个链表，能想到的方法是遍历所有单独的节点，并用node=node.next推进依次赋值的进行
    '''
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes_val = []
        def dfs(root):
            if not root:
                return
            nodes_val.append(root.val)
            dfs(root.left)
            dfs(root.right)        
        dfs(root)
        
        node = root
        for val in nodes_val[1:]:
            node.right = TreeNode(val)
            node.left = None
            node = node.right
