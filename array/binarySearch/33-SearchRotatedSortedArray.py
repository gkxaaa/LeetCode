class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        pivot = self.find_rotate_point(nums)
        if pivot is None:
            l, r = 0, len(nums)-1
        else:
            if target>=nums[0]:
                l, r = 0, pivot
            else:
                l, r = pivot+1, len(nums)-1
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        if target < nums[l] or target > nums[r]:
            return -1
        
        while r-l>1:            
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid
            else:
                r = mid
        return -1
    
    def find_rotate_point(self, nums):
        l, r = 0, len(nums)-1
        if nums[r] >= nums[l]:
            return None
        while r-l>1:
            mid = (l+r)//2
            if nums[mid]>=nums[l]:
                l = mid
            elif nums[mid]<nums[r]:
                r = mid
        return l
