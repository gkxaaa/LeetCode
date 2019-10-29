class Solution(object):
    '''
    二分法查找最典型的一道题，二分查找就是在一个有序序列里面查找是否存在特定项。
    思路一：第一遍用二分查找找到pivot拐点，第二遍再用二分法在每个有序序列里查找
    思路二：也可以只用一遍二分查找，需要指定一个复杂一点的规则，每次用target和中间数
           比较时要a结合target和左右边界数字大小关系，才能决定向哪边缩一半范围
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l, r = 0, len(nums)-1
        while r>l:
            m = (l+r)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m     
        # now l=r=upper_bound
        if nums[0]<=target<=nums[l]:
            return self.binary_search(nums, 0, l, target)
        elif l+1<len(nums) and nums[l+1]<=target<=nums[-1]:
            return self.binary_search(nums, l+1, len(nums)-1, target)
        else:
            return -1
    
    def binary_search(self, nums, l_min, r_max, target):
        l, r = l_min, r_max
        if nums[l]==target:return l
        elif nums[r]==target:return r
        elif target>nums[r] or target<nums[l]: return -1
        while r-l>1:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m
        return -1
