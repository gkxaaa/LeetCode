# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    思路1: 类似与归并排序算法中的合并，找到k个列表头.val最小的Node，然后往后走一步。可以新建ListNode，Space O(m). 也可以in place改变ListNode，Space O(1)
    思路2: 递归分治。把list分成左右两部分
    '''
    def mergeKLists(self, lists):
        if not lists: return None
        elif len(lists)==1:
            return lists[0]
        m = len(lists)//2
        return self.merge2Lists(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))       
        
    def merge2Lists(self, head1, head2):
        newHead = ListNode(None)
        node = newHead
        while head1 and head2:
            if head1.val<head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        node.next = head1 if head1 else head2
        return newHead.next
                
            
            
    def mergeKLists1(self, lists): #Space O(1), Time O(kN)
        state, newHead = True, ListNode(None)
        pre_node = newHead
        while state:
            state, MIN = False, float('inf')
            for k, head_k in enumerate(lists):
                state = state or head_k
                if head_k and head_k.val<MIN:
                    MIN, min_k = head_k.val, k
                    min_node = head_k
            if state:
                pre_node.next = min_node
                pre_node = pre_node.next
                lists[min_k] = lists[min_k].next          
        return newHead.next
    
    def mergeKLists2(self, lists): #Space O(m)
        state, newHead = True, ListNode(None)
        node = newHead
        while state:
            state, MIN = False, float('inf')
            for k, head_k in enumerate(lists):
                state = state or head_k
                if head_k and head_k.val<MIN:
                    MIN, min_k = head_k.val, k
            if state:
                node.next = ListNode(MIN)
                node = node.next
                lists[min_k] = lists[min_k].next
        return newHead.next
