class Solution(object):
    '''
    思路1：字典map，时间2*O(n)空间O(n)
    思路2：Brute Force，双层循环时间O(n**2)空间O(1)
    思路3：快排n*log(n)桶排序O(n)，最后从头开始找出第一个不顺眼的数字，但是会该改变数组
    思路4：数组内映射，当前元素访问过后加一个大数，后面遇到重复的会映射过来再次访问这个大数。O(n), O(1)
    思路5：二分法
    '''
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set()
        for num in nums:
            if num in d:
                return num
            else:
                d.add(num)
                
    def findDuplicate2(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return nums[i]
    
    def findDuplicate4(self, nums):
        MAX = len(nums)
        for n in nums:
            if n >= MAX:
                n -= MAX
            if nums[n-1] >= MAX:
                return n
            else:
                nums[n-1] += MAX
        
    def findDuplicate(self, nums):
        left, right = min(nums), max(nums)
        while right > left:
            counter = 0
            mid = (right + left)//2
            for num in nums:
                if num <= mid:
                    counter += 1
            if counter > mid:
                right = mid
            else:
                left = mid + 1
        return right   
                
