"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    '''
    一道类似于有向图遍历的题。
    思路1: bfs，每次遍历当前节点的next和random后并标记当前节点，然后对next和random节点重复操作（注意如果next和random节点是一个节点的话操作一次）。用队列存放接下来还需要遍历的节点，若队列空说明所有节点都被访问。
    思路2：dfs，停止边界是每个节点的next和random若都被访问过，标记当前节点。但有一个问题，若先访问next节点一直到头发现有环，那么递归将不会停止maximum recursion depth exceeded.所以另一个边界是每个节点的next或者random都被访问过。
    '''
    def copyRandomList_bfs(self, head):
        if not head: return None
        node = Node(head.val, None, None)
        queue = [(head,node)]
        res, d = node, {}
        d[node.val] = node
        while queue:
            head, node = queue.pop(0)
            if head.next:
                node.next = d.get(head.next.val, Node(head.next.val, None, None))
                if node.next.val not in d:
                    queue.append((head.next, node.next))
                d[head.next.val] = node.next
            if head.random:   
                node.random = d.get(head.random.val, Node(head.random.val, None, None))
                if node.random.val not in d:
                    queue.append((head.random, node.random))
                d[head.random.val] = node.random
        return res
    
    def copyRandomList(self, head):
        if not head: return None
        node = Node(head.val, None, None)
        d1, d2 = {}, {}
        d1[node.val]= node
        def dfs(head, node):
            if d2.get(head.val, 0)>=1:
                return 
            d1[node.val] = node
            d2[node.val] = d2.get(node.val,0) + 1 # next Node is counted whether it None or not
            if head.next:
                node.next = d1.get(head.next.val, Node(head.next.val, None, None))
                dfs(head.next, node.next)
            d2[node.val] = d2.get(node.val,0) + 1
            if head.random:
                node.random = d1.get(head.random.val, Node(head.random.val, None, None))
                dfs(head.random, node.random)
        dfs(head, node)
        return node
