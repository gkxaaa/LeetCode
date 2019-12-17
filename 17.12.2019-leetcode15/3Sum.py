class Solution(object):
    '''
    思路1：Brute Force，Time O(n**3)，Space O(1)
    思路2：空间换时间，Time O(n**2)，Space O(n)
    思路3：先排序，然后从左往右每次定一个数，后面分别从左右两端往中间夹
           Time O(n**2)，Space O(1)
    '''
    def threeSum2(self, nums): # Time Limit Exceeded 312/313 cases passed.
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                if -nums[i]-nums[j] in seen:
                    tmp = tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]]))
                    if tmp not in res:
                        res.add(tmp)
                else:
                    seen.add(nums[j])
        return map(list,res)
    
    def threeSum(self, nums): 
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                if -nums[i]-nums[j] in seen:
                    tmp = (nums[i], nums[j], -nums[i]-nums[j])
                    if tmp not in res:
                        res.add(tmp)
                else:
                    seen.add(nums[j])
        return map(list,res)
    
    def threeSum(self, nums): 
        res = set()
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while right > left:
                tmp = (nums[i], nums[left], nums[right]) 
                if sum(tmp)==0:
                    if tmp not in res:
                        res.add(tmp)
                    left += 1
                    right -= 1
                elif sum(tmp) < 0:
                    left += 1
                else:
                    right -= 1
        return map(list,res)
