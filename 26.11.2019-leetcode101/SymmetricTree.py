# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    思路1:前序遍历(中左右)和从(中右左)遍历如果结果相同为True，时间复杂度O(2*n),空间O(2*n)
    思路2: 一棵树是对称代表:
    1) root.left.val==root.right.val
    2) root.left.right和root.right.left是节点数值都相同的子树
    3) root.left.left和root.right.right是节点数值都相同的子树
    思路3：bfs with itertion method. 如果是层序遍历，维护队列时出最左边的一个节点，同时最右端入这个节点的左右子节点。
    就是说用队列迭代时，左边出一个东西右边进一个东西，就应该解决了问题。看了答案迭代时每次出两个节点，若相同则把这
    两个节点的左右子节点按一定顺序进入队列，一次类推。把解决问题的步骤聚焦在队列的进和出。
    '''
    def isSymmetric(self, root):
        if not root:return True
        queue = [root,root]
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2: pass
            elif not t1 or not t2: return False
            elif t1.val==t2.val:
                queue.append(t1.left)
                queue.append(t2.right)
                queue.append(t1.right)
                queue.append(t2.left)
            else:
                return False
        return True
    
        
    def isSymmetric_rec(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        def rec(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            res = t1.val==t2.val and rec(t1.left, t2.right) \
                                 and rec(t2.left, t1.right)
            return res
        return rec(root.left, root.right)
