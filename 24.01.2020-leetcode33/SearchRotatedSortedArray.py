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
