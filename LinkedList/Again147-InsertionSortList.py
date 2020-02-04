# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        new_head, cur = ListNode(0), head
        while cur:
            pre = new_head
            next_tmp = cur.next
            while pre.next and cur.val > pre.next.val:
                pre = pre.next
            pre.next, cur.next = cur, pre.next
            cur = next_tmp
        return new_head.next
            
        
        
        
        
    def insertionSortList2(self, head): #Time Limit Exceeded,18 / 22 test cases passed.
        if not head: return None
        cur = head
        while cur.next:
            pre, node = None, head
            while cur.next!=node and cur.next.val>=node.val:#find the right position
                pre, node = node, node.next
            tmp = cur.next
            if not(cur.next is node):
                cur.next.next, cur.next = node, cur.next.next
                if not pre: #插入表头，需更新head
                    head = tmp
                else:
                    pre.next = tmp
            cur = tmp
        return head
