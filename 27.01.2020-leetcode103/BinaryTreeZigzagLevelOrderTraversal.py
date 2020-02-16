# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路：保持queue层序遍历的出入队列顺序，只有当偶数层时向res中添加数字时从左边添加。
          Time O(n), Space O(n)
    '''
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, res = [(root, 1)], []
        while queue:
            node, depth = queue.pop(0)
            if node:
                if depth>len(res):
                    res.append([])
                if depth & 1:
                    res[depth-1].append(node.val)
                else:
                    res[depth-1] = [node.val] +  res[depth-1]
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
        return res
