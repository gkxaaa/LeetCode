# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, h1, h2):
        new_head = ListNode(None)
        node = new_head
        while h1 and h2:
            if h1.val < h2.val:
                node.next, h1 = h1, h1.next
            else:
                node.next, h2 = h2, h2.next
            node = node.next
        node.next = h1 or h2
        return new_head.next
        
    def sortList(self, head):
        if not head: return None
        if not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)
