# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路：每次出队列一个节点时把它的孩子节点入队列，刚好符合层序遍历顺序
          Time O(n) Space O(n)
    '''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, res = [(root,1)], []
        while queue:
            node, depth = queue.pop(0)
            if node:
                if depth>len(res):
                    res.append([])
                res[depth-1].append(node.val)
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
        return res 
