# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n: return head
        idx, node, pre = 1, head, None
        start = ListNode(None)
        start.next = head
        while idx<=n:
            if idx>m:
                node.next, pre, node = pre, node, node.next
            else:
                if idx==m-1:
                    start = node
                pre, node = node, node.next
            idx += 1            
        start.next.next, start.next = node, pre
        return head if start.val else pre
