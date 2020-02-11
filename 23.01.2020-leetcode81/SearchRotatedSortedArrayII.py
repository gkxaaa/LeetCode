class Solution:
    '''
    思路1: 先二分法找到转折点，然后再用一次二分法找target。
           问题或难点：有重复的数字，当nums[m]==nums[l]==nums[r]时
           不一定是左边或者右边，需要递归继续往里看后才能判断取哪边
           Time O(logN)**2, Space O(1), 274/275 cases pass
    思路2: 直接用二分法查找。在之前的二分法算法中，总是直接用target和中间或者两边
           的数比大小，然后观察具体数组corner cases看怎么缩小范围，这道题的一个难
           点就在于罗列所有可能情况（总共有6种）虽然也可以解决但没有抓到问题的本质
           
           总结二分法算法关键：从理解上，必须基于有序数组，问题比较复杂时则考虑怎
           么化解成若干个有序数组来理解。在这道题中，每次取中间后，数组分为左右两
           半，必有一半是有序数组（拐点不在其中）
    '''
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        l, r = 0, len(nums)-1
        while r>l:
            m = (r+l)//2
            if nums[m]==target:
                return True
            while m>l and nums[m]==nums[l]:
                l += 1
            if nums[l]<=nums[m]:#1. half is ascending or 1. half are same numbers
                if nums[l]<=target<nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # 2. half is ascending
                if nums[m]<target<=nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return nums[l]==target
            
    def search3(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        l, r = 0, len(nums)-1
        while r>l:  # 出现nums[m]==nums[l]==nums[r]时有歧义
            m = (r+l)//2
            if nums[m]==target:
                return True
            if target > nums[m] or target<=nums[r]<nums[m]:
                l = m + 1
            elif target > nums[r] or target<nums[m]<=nums[r]:
                r = m - 1
        return target==nums[l]
    def find_rotate(self, nums): #
        l, r = 0, len(nums)-1
        while r-l>1:
            m = (r+l)//2
            if nums[m]>nums[r] or nums[m]<nums[l]:
                return True
            l = m
        return False
    
    def binary_search(self, nums, target):
        l, r = 0, len(nums)-1
        while r>l:
            m = (r+l)//2
            if nums[m]==target:
                return True
            elif target>nums[m]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]==target
                
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        l, r = 0, len(nums)-1
        if nums[l]>=nums[r]:
            while r-l>1:
                m = (r+l)//2
                if nums[m]>nums[r]:
                    l = m
                elif nums[m]<nums[l]:
                    r = m
                else: # nums[m]==nums[l]==nums[r]
                    if self.find_rotate(nums[l:m+1]):
                        r = m
                    else:
                        l = m
        if nums[r]<=target<=nums[-1]:
            return self.binary_search(nums[r:], target)
        elif nums[0]<=target<=nums[r-1]:
            return self.binary_search(nums[:r], target)
        else:
            return False
        
        
