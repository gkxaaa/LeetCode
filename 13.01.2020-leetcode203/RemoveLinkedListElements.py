# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead, node = ListNode(None), head
        newHead.next, pre = head, newHead
        while node:
            if node.val == val:
                pre.next = node.next
            else:
                pre = node
            node = node.next
        return newHead.next
