# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def rec(head):
            if not head:
                return -1
            n_node = rec(head.next) + 1
            if n_node == n:
                head.next = head.next.next
            return n_node
        
        if rec(head) == n-1:
            return head.next
        else:
            return head
