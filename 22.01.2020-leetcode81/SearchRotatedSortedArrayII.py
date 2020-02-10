class Solution:
    '''
    思路1: 先二分法找到转折点，然后再用一次二分法找target。
           问题或难点：有重复的数字，当nums[m]==nums[l]==nums[r]时
           不一定是左边或者右边，需要递归继续往里看后才能判断取哪边
           Time O(logN)**2, Space O(1), 274/275 cases pass
    思路2:
    '''
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
