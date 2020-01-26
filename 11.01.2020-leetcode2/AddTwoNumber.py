# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    思路1：新建一个链表每次保存链表数字之和，Space O(n)
    思路2：in place改变当前链表，Space O(1)
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num, pre = 0, None
        head = l1
        while l1:
            if l2:
                num += l2.val
                l2 = l2.next
            num += l1.val
            l1.val, num = num%10, num//10
            pre, l1 = l1, l1.next
        while l2:
            num += l2.val
            l2.val, num = num%10, num//10
            pre.next, pre, l2 = l2, l2, l2.next
        if num:
            pre.next = ListNode(num)
        return head

        
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode(None)
        node = newHead
        flag = 0
        while l1 or l2 or flag:
            node.next = ListNode(0)
            if l1:
                node.next.val += l1.val
                l1 = l1.next
            if l2:
                node.next.val += l2.val
                l2 = l2.next
            node.next.val += flag
            flag, node.next.val = node.next.val//10,node.next.val%10
            node = node.next
        return newHead.next
