# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    思路：快慢指针。Time O(n), Space O(1)
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head 
        slow, fast, count = self.find_fast_slow(head, k)
        if k>=count: # 若k大于链表长度
            slow, fast, count = self.find_fast_slow(head, k%count)
        if fast is slow: # 说明快慢指针相同，k==0
            return head
        fast.next, new_head = head, slow.next
        slow.next = None
        return new_head
    
    def find_fast_slow(self, head, k): #找到链表最末端和slow节点
        count = 0
        fast, slow = head, head
        while fast.next:
            fast = fast.next
            count += 1
            if count>k:
                slow = slow.next
        return (slow, fast, count+1)
