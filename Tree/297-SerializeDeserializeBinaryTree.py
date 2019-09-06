################05.09.2019 Wed##################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:  
    def serialize_bfs(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue, res = [], []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(node)
                
        return str(res)
    '''
    [root.val] + dfs(root.left) + dfs(root.right)
    递归的看，当下root节点所代表树的序列（preorder）可以写成，中左右：先是root节点，接着是左子树序列，接着是右子树序列
    '''
    def serialize(self, root):
        def dfs(root):
            if not root:
                return [None]
            return [root.val] + dfs(root.left) + dfs(root.right)
        return str(dfs(root)) 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 算法核心思想：利用调用时从下往上的调用路径，每次给左右孩子节点赋值。
        # 在走到边界时调用TreeNode生成叶子节点，返回并赋值到上一递归层左右孩子节点
        ########################################################################
        # 用dfs前序遍历走，往下时每次data数组缩短一个，问题是当下面走完再回到当前
        # 递归层时，data数组又回到当初，但根据算法的设计它走完下面叶子节点后数组
        # 应该永久的被缩短。
        
        # 划重点：python数组切片其实是复制原数组不会被改变，当修改data[i]或者数组
        # pop，append时，数组内存会被改变。
        
        # 这里当返回当前递归层时正好想利用数组被永久改变的特征，虽然两次递归用的
        # 都是变量名'data'，变量其实已被修改（pop）

        data = data[1:-1].split(', ')
        def dfs_generate(data):
            # 也不用担心data为空越界，[1,2,3,None,None,4,None,None,5,None,None]
            # 3作为叶子节点，下两个是None所以递归到了边界会返回None。但是程序不会
            # 结束，因为节点3的父亲节点在上一层调用了2, 2的父亲节点调用了5。
            
            # 最后到了节点5，作为右节点，在递归函数里是最后一行，它的所有祖上节点
            # 运行到它都要结束，所用调用函数栈都被执行，函数返回值往回传，传到
            # 根节点，程序运行终止

            if data[0]=='None':
                data.pop(0)
                return None
            subroot = TreeNode(data[0])
            data.pop(0)
            subroot.left = dfs_generate(data)
            subroot.right = dfs_generate(data)
            return subroot   

        return dfs_generate(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
