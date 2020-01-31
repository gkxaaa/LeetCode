# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):     
        if not head or not head.next:
            return head
        cur, new_head = head, ListNode(None)
        pre = new_head
        while cur and cur.next:
            tmp = cur.next
            cur.next, tmp.next, pre.next = cur.next.next, cur, tmp
            pre, cur = cur, cur.next
        return new_head.next
        
     
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        count, pre, pre_pair, node = 0, None, None, head
        while node:
            if count&1:
                if count==1:
                    newHead, pre_pair = node, pre
                if pre_pair:
                    pre_pair.next, pre_pair = node, pre
                pre.next, node.next, node = node.next, pre, node.next
            else:
                pre, node = node, node.next
            count += 1
        return newHead
