# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路1:层序遍历，统计每一层最大长度。不同的是，若当前节点为None，还需要添加两个
          分别为None的左右子孩子。
    思路2: bfs每新的一层最左边的点记为left，然后每过一个节点更新一次.
    思路3: dfs, 每次新的一层需要记下来当前层最左边非空节点序号。首先想到用全局变量，
          每当depth增加时更新全局变量,但前面的会被后面的覆盖掉。
          所以用数组或者字典保存每层最左边非空节点编号 a)数组用当前长度表示当前层数 b)字典
    '''
    def widthOfBinaryTree(self, root):
        left = {}
        self.res = 0
        def dfs(root, depth=1, pos=1):
            if not root:
                return
            left[depth] = left.get(depth, pos)
            self.res = max(self.res, pos-left[depth]+1)
            dfs(root.left, depth+1, pos*2)
            dfs(root.right, depth+1, pos*2+1)
        dfs(root)
        return self.res
    
    def widthOfBinaryTree_dfs(self, root):
        left = []
        self.res = 0
        def dfs(root, depth=1, pos=1):
            if not root:
                return
            if depth>len(left):
                left.append(pos)
            self.res = max(self.res, pos-left[depth-1]+1)
            dfs(root.left, depth+1, pos*2)
            dfs(root.right, depth+1, pos*2+1)
        dfs(root)
        return self.res
        
    def widthOfBinaryTree_dfs_wrong(self, root):#不管当前节点坐孩子是否是None，下一层计算宽度时都以它为起点
        self.res = 0
        def dfs(root, pos=1, left=1):
            if not root:
                return
            self.res = max(self.res, pos-left+1)
            dfs(root.left, pos*2, left*2)
            dfs(root.right, pos*2+1, left*2)
        dfs(root)
        return self.res
        
    def widthOfBinaryTree_bfs(self, root):
        queue = [(root, 1, 1)]
        cur_depth = left = res = 0
        while queue:
            node, depth, pos = queue.pop(0)
            if node:
                if depth>cur_depth:
                    left = pos
                    cur_depth = depth
                res = max(res, pos-left+1)
                queue.append((node.left, depth+1, 2*pos))
                queue.append((node.right, depth+1, 2*pos+1))
        return res
    
    def widthOfBinaryTree1(self, root: TreeNode) -> int:
        queue, nodes_layer = [(root, 1)], []
        max_depth, pre_depth = 0, 0
        while queue:
            node, depth = queue.pop(0)
            if depth>pre_depth: # 开始了新的一层，统计上一层最大宽度（节点个数）
                if len(nodes_layer)>max_depth:
                    nax_depth = len(nodes_layer)
                    pre_depth = depth # 更新pre_depth
                    nodes_layer = [] #统计完上一层最大长度后，释放以储存下一层节点
            if node:
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
            else:
                queue.append((None,depth+1))
                queue.append((None,depth+1))
