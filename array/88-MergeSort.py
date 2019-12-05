class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, r = m-1, n-1, len(nums1)-1
        while p1 >= 0 and p2 >= 0:
            while p2 >= 0 and nums1[p1] <= nums2[p2]:
                nums1[r] = nums2[p2]
                r -= 1
                p2 -= 1
            while p1 >= 0 and p2 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[r] = nums1[p1]
                r -= 1
                p1 -= 1
        if p1 >= 0:
            nums1[r-p1:r+1] = nums1[:p1+1]
        elif p2>=0:
            nums1[r-p2:r+1] = nums2[:p2+1]
        return nums1[-m-n:]
        
