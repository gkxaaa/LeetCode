# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
1. 遍历
从每个节点开始，分别计算到其它任一点最大路径。时间复杂度O(n**2)。
访问树上节点最常用的是遍历，遍历只能从上往下，所以需要先遍历一遍保存节点到root距离信息的字典。第二遍遍历的时候为每个点更新这个字典，后面统计全局最大的时候还得遍历字典，复杂度太高
2. 递归回传返回值的特征
遍历只能从上往下走一遍得到想要的东西，就是说当遍历到某个父亲节点时，对它的子树信息毫无头绪。但是利用返回值，它是从下往上，树天然就有这种递归的结构。自然而言想到动态规划的思想，利用递归/迭代把目标问题化解为子问题。

我们的问题：求root节点代表的树的最大路径和。把它化解成子问题有三种情况：
1. root节点的左或右子树已经有了最大路径和，所以不需要通过当前root节点
2. 通过root节点并终止与此
3. 通过root并向下拐
4. 只取了root节点，因为子树全是负数
那么函数返回什么呢? 递归从最末端叶子节点向上返回，那么它肯定不能返回拐弯的情况，以为它已经拐了不可能再想上。对于第一种情况，相当于不返回，中间断开了，但是不能这么贪心的看事物，当下root的一个子树取得了最大增益，但不能保证子树损失一点增益，继续往上走万一后面又向下拐弯而获得更大的增益。所以返回2,3情况。return max(root.val, max(root.left), max(root.right))+root.val)
P.S: 等式可以简化，left_gain = max(root.left, 0)如果root.left小于零直接忽略它
right_gain = max(root.right, 0), return max(left_gain,right_gain)+root.val
'''
class Ans:
    def __init__(self):
        self.global_max = -float('inf')
        
class Solution(object):
    def maxPathSum(self, root):
        def rec_max(root):
            if not root:
                return 0
            left_gain = max(rec_max(root.left), 0)
            right_gain = max(rec_max(root.right), 0)
            turn_gain = left_gain + right_gain + root.val
            if res.global_max < turn_gain:
                res.global_max = turn_gain
            return max(left_gain, right_gain) + root.val
        res = Ans()
        rec_max(root)
        return res.global_max
