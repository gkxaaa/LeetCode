# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    '''
    思路1: 对每个node满足三个条件:
    1. root.left.val<root.val<root.right.val
    2. root.left is BST
    3. root.right is BST
    可以用递归如下。但是这里对BST定义有偏差，满足上述3个条件并不一定是BST
    如：                    3
                           / \
                          1   6
                             /
                            2
    应该把1替换为：root.left subtree下面所有点都小于root.val，root.right subtree下面所有点都大于root.val
    '''
    def isValidBST_misunderstand(self, root): #Wrong Answer, 70/75 cases passed.
        if not root:
            return True
        left_sub = self.isValidBST(root.left)
        right_sub = self.isValidBST(root.right)
        left=right=True
        if root.left:
            left = root.left.val<root.val
        if root.right:
            right = root.right.val>root.val
        return left_sub and right_sub and left and right

    def isValidBST_rec(self, root, MAX=float('inf'), MIN=-float('inf')):
        if not root:
            return True
        res = False
        if MIN<root.val<MAX:
            res = self.isValidBST(root.left, root.val, MIN) and \
                self.isValidBST(root.right, MAX, root.val)
        return res

    def isValidBST(self, root):
        MIN, MAX = -float('inf'), float('inf')
        queue = [(root, MIN, MAX)]
        while queue:
            node, MIN, MAX = queue.pop(0)
            if node: 
                if MIN<node.val<MAX:
                    queue.append((node.left, MIN, node.val))
                    queue.append((node.right, node.val, MAX))
                else:
                    return False
        return True
