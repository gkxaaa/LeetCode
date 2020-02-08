# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class SlowNode:
    def __init__(self, slow):
        self.slow = slow
        self.res = True
        
class Solution(object):
    '''
    思路1：Brute Force，遍历记下每个点到一个列表，再循环一遍判断是否回文，Time O(2*n) Space O(n)
    思路2：未改变链表。第一遍快慢指针遍历，慢指针走到中间的位置把链表分为前后两半。
          第二遍分别递归和迭代这两半链表看是否每次节点的值都相等。
          Time O(2*n) Space O(1)
    思路3：改变了链表。对一半进行反转。Time O(2*n) Space O(1)
    '''
    def isPalindrome3(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        pre = None
        while head!=slow:
            head.next, head, pre = pre, head.next, head
        slow = slow.next if fast else slow
        while slow and pre:
            if slow.val!=pre.val:
                return False
            slow, pre = slow.next, pre.next
        return True
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        res = SlowNode(slow) if not fast else SlowNode(slow.next)
        def traverse(head):
            if head == slow:
                return
            traverse(head.next)
            res.res = res.res and (head.val==res.slow.val)
            res.slow = res.slow.next     
        traverse(head)
        return res.res
    
    
    
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
    
    
        
