# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
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
