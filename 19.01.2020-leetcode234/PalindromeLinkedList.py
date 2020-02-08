# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    思路1: 不需反转链表，递归+迭代遍历。将链表分成两半，
           一半从前往后，另一半从后往前遍历，比较是否每次都相等
    思路2: 反转其中一半链表
    '''
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next            
        def rec(slow):
            if not slow:
                return (head, True)
            node, flag = rec(slow.next)
            flag = flag and (node.val==slow.val)
            return (node.next, flag)
        _, flag = rec(slow)
        return flag
    
    def isPalindrome2(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next 
        pre, tmp_slow = None, slow
        while slow:
            slow.next, pre, slow = pre, slow, slow.next
        head2 = pre
        while head and head is not tmp_slow:
            if head.val!=head2.val:
                return False
            head, head2 = head.next, head2.next
        return True
    
    
        
