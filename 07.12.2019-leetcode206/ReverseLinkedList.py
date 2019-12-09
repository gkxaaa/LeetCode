# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList_iter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre
    
    def reverseList_rec(self, head):
        if not head: return None
        def rec(head):
            if not head.next:
                return head
            res = rec(head.next)
            head.next.next = head
            head.next = None
            return res
        return rec(head)
