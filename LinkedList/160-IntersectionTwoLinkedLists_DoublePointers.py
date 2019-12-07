# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    思路1:Brute Force第一遍上面遍历并记下所有点，第二遍下面遍历看是否被访问过。时间O(n)空间复杂度O(n)。
    思路2:节点从底往上返回时第一个出现不相等节点
    '''
    def traverse_rec(self, head):
        if not head:
            return 0
        return self.traverse(head.next)+1
    
    def traverse(self, head):
        node, n = head, 0
        while node:
            node = node.next
            n += 1
        return n
        
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = self.traverse(headA), self.traverse(headB)
        n = 0
        while n < abs(lenB-lenA):
            if lenA < lenB:
                headB = headB.next
            else:
                headA = headA.next
            n += 1
        while headA and headB and headA!=headB:
                headA, headB = headA.next, headB.next
        return headA
    
    def getIntersectionNode_rec(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA and not headB:
            return 
        if not headA:
            self.getIntersectionNode(headA, headB.next)
        elif not headB:
            self.getIntersectionNode(headA.next, headB)
        else:
            self.getIntersectionNode(headA.next, headB.next)
        return 
