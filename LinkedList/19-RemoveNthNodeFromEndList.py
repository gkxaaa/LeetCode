# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd_DoublePointers(self, head, n):
        '''
        Double pointers
        '''
        node = head
        gap, second = 0, head
        while node:
            if gap > n:
                second = second.next
            node = node.next
            gap += 1
        if gap == n:
            return head.next
        else:
            second.next = second.next.next
            return head    
        
    def removeNthFromEnd_rec(self, head, n):
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
        
    def removeNthFromEnd_others(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        fast = fast.next 
        
        for i in range(n):
            fast = fast.next
        
        while(fast is not None): 
            fast = fast.next 
            slow = slow.next    
        slow.next = slow.next.next
        
        return dummy.next
