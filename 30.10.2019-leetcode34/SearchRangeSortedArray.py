class Solution(object):
    '''
    二分法典型题目，需要注意的有两点，第一：从中间缩短范围时用target和中间数比较。第二：注意程序断开时是l==r 还是 r-l==1
    思路一：先找到中间一个数等于target，然后在[l, m]查找左边界在[m, r]上寻找右边界，这不得写三遍二分查找
    思路二：两遍查找，第一遍寻找左边界，第二遍查找右边界
    '''
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        return [self.search_left(nums, target), self.search_right(nums, target)]
    
    def search_left(self, nums, target):
        l, r = 0, len(nums)-1
        if nums[l]==target: return l
        elif target<nums[l] or target>nums[r]: return -1
        while r-l>1:
            m = (l+r)//2
            if target <= nums[m]:
                r = m
            else:
                l = m
        return r if nums[r]==target else -1
    
    def search_right(self, nums, target):
        l, r = 0, len(nums)-1
        if nums[r]==target: return r
        elif target<nums[l] or target>nums[r]: return -1
        while r-l>1:
            m = (l+r)//2
            if target >= nums[m]:
                l = m
            else:
                r = m
        return l if nums[l]==target else -1
