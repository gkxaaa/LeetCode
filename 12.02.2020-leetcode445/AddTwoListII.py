# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def lenListNode(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n
   
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        len1, len2 = self.lenListNode(node1), self.lenListNode(node2)
        (l1, l2) = (l2, l1) if len2<len1 else (l1, l2)
        if abs(len1-len2):
            for i in range(abs(len2-len1)):
                new_l1 = ListNode(0)
                new_l1.next, l1 = l1, new_l1
        else:
            new_l1 = l1
            
        head, num = self.rec(new_l1, l2)
        if num:
            newHead, newHead.next = ListNode(num), head
            return newHead
        else:
            return head
            
    def rec(self,l1, l2):
        if not l1 and not l2:
            return (None, 0)
        pre_node, num = self.rec(l1.next, l2.next)
        num += l1.val + l2.val
        node, node.next = ListNode(num%10), pre_node
        num = num//10
        return (node, num)
