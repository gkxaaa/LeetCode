# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    思路：pre1为需要插入位置的前一个节点，pre2为每次cur节点的前一个点.
          1. 若cur大于等于x，pre1不变，pre2和cur往前走一步
          2. 若cur小于x，若pre1下一个点也小于x，pre1和pre2以及cur都向前一步
          3. 若cur小于x，若pre1下一个点不小于x，此时插入cur到pre1之后，调整链表
    '''
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return None
        newHead = ListNode(None)
        newHead.next = head
        pre1, cur = newHead, head
        while cur:
            if cur.val<x and pre1.next.val>=x:
                pre1.next, cur.next, pre2.next = cur, pre1.next, cur.next
                pre1, cur = cur, pre2.next
            elif cur.val<x:
                pre1, pre2, cur = cur, cur, cur.next
            else:
                pre2, cur = cur, cur.next
        return newHead.next
