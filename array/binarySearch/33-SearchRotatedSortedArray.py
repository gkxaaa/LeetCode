class Solution:
    '''
    思路：直接二分法。每次取中间后分为左右两半，必有一半为有序数组
    '''
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums)-1
        while r>l:
            m = (l+r)//2
            if nums[m]==target:
                return m
            if nums[l]<=nums[m]: # left half ascending, 注意等号的边界条件
                if nums[l]<=target<nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m]<target<=nums[r]:
                    l = l + 1
                else:
                    r = m - 1
        return l if nums[l]==target else -1


'''
二分法进阶题目, 08.08.2019代码冗杂，参考29.10.2019
'''
class Solution(object):
    def search(self, nums, target):
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
