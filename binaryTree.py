class BinTreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data,self.left,self.right = data,left,right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root
        
    @classmethod
    def build_from(cls,node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            # data map data
            node_dict[data]=BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
        
    @classmethod
    def build(cls,node_list2):
        node_dict = {}
        # build each node with the data
        for data in node_list2.keys():
            node_dict[data] = BinTreeNode(data)
        # build each node with left and right children    
        for data,node in node_dict.items():
            if data==node_list2.keys()[0]:
                root = node
            node.left = node_dict.get(node_list2[data][0])    
            node.right = node_dict.get(node_list2[data][1])  
        return cls(root)
      
    def dfs(self,subtree):
        if subtree is not None:
            print(subtree.data)
            self.dfs(subtree.left)
            self.dfs(subtree.right)      

    def layer_trav(self,subtree):
        queue = []
        queue.append(subtree)
        while len(queue)>0:
            vertex_node = queue.pop(0)
            if vertex_node.left:
                queue.append(vertex_node.left)
            if vertex_node.right:    
                queue.append(vertex_node.right)
            print(vertex_node.data)

    def preorder_trav(self,subtree):
        stack = []
        stack.append(subtree)
        while len(stack)>0:
            vertex_node = stack.pop()
            
            if vertex_node.right:
                stack.append(vertex_node.right)
            if vertex_node.left:    
                stack.append(vertex_node.left)
            print(vertex_node.data)    

    def reverse(self,subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
        subtree          
      
node_list2 = {
       'A':('B','C'),
       'B':('D','E'),
       'D':(None,None),
       'E':('H',None),
       'H':(None,None),
       'C':('F','G'),
       'F':(None,None),
       'G':('I','J'),
       'I':(None,None),
       'J':(None,None)}            
            
            
node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

btree = BinTree.build_from(node_list)  
btree2 = BinTree.build(node_list2)   
#btree2.layer_trav(btree2.root)
btree2.preorder_trav(btree2.root)  

