# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        evenHead, cur = head.next, head
        n = 1
        while cur.next:
            cur.next, cur, pre = cur.next.next, cur.next, cur
            n += 1
        if n&1: cur.next = evenHead
        else: pre.next = evenHead
        return head
