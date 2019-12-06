class Solution(object):
    def mergeTwoLists(self,l1, l2):
        new_head = ListNode(None)
        node = new_head
        while l1 and l2:
            if l1.val > l2.val:
                node.next, l2 = l2, l2.next
            else:
                node.next, l1 = l1, l1.next
            node = node.next
        node.next = l1 or l2
        return new_head.next
    
    def mergeTwoLists_old(self,l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l2.val < l1.val:
            l1, l2 = l2, l1
        l = l1
        while l1 and l2:
            if l1.next and l1.next.val <= l2.val:
                l1 = l1.next
            else:
                l1.next, l2, l1 = l2, l1.next, l2
        return l
