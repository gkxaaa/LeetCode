# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    思路1: 迭代
    思路2：递归
    '''
    def reverseList_iter(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        def rec(head):
            if not head.next:
                return head
            newHead = rec(head.next)
            head.next.next, head.next = head, None
            return newHead
        return rec(head)
