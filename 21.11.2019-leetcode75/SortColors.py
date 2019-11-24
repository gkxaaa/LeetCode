class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx1, idx2 = None, len(nums)-1
        for i in range(len(nums)):
            if nums[i]==2:
                while idx2>i and nums[idx2]==2:
                    idx2 -= 1
                if idx2==i: return
                nums[i], nums[idx2] = nums[idx2], nums[i]
            if nums[i]==0 and idx1 is not None:
                nums[i], nums[idx1] = nums[idx1], nums[i]
                idx1 += 1
            elif nums[i]==1 and idx1 is None:
                idx1 = i
