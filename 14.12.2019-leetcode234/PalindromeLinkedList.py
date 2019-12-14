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
    def isPalindrome(self, head):
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
    
    def isPalindrome2(self, head):
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
