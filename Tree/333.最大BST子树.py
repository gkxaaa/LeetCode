给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，其中最大指的是子树节点数最多的。

注意:
子树必须包含其所有后代。

示例:

输入: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

输出: 3
解释: 高亮部分为最大的 BST 子树。
     返回值 3 在这个样例中为子树大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-bst-subtree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路1：自底而上的递归。左子树的BST节点数，右子树的节点数，取max。不是BST返回0.
    思路2: 思路1有问题，原因在于判断BST的方法是自顶而下的，中间有一个点不符合要求它下面的所有子树直接跳过
          需要一种自底而上的判断BST方法2: 左子树最大的数<根节点<右子树最小的数
          每次需要返回左子树最小的数l_min，和右子树最大的数r_max。但边界会有问题，负无穷和正无穷会使所有点
          都满足要求。在边界问题需要一个小技巧，平常情况下min(root.val,l_min)==l_min
          max(root.val,r_max)==r_max, 边界时l_min=正无穷，r_max=负无穷，正好统一等式
    '''
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def rec(root):
            if not root:
                return float('inf'), -float('inf'), 0
            l_min, l_max, count_l = rec(root.left)
            r_min, r_max, count_r = rec(root.right)
            if l_max < root.val < r_min:
                return min(root.val, l_min), max(root.val, r_max), count_l+count_r+1
            return -float('inf'), float('inf'), max(count_l, count_r)
        return rec(root)[-1]

    def largestBSTSubtree1(self, root: TreeNode) -> int:
        def rec(root, left=-float('inf'), right=float('inf')):
            if not root or not left < root.val < right:
                return 0
            count_l = rec(root.left, left, root.val)
            count_r = rec(root.right, root.val, right)
            count = max(count_l, count_r)
            return count+1
        return rec(root)
