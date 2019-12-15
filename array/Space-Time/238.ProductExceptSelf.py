class Solution(object):
    '''
    思路1：Brute Force 每个output[i]直接通过连乘计算得到。Time O(n**2), Space O(1)
    思路2：先求出nums的乘积，再用依次除以nums[i]赋值给output[i]. Time O(n) Space O(1)
    思路3：空间换时间，左边右边连乘记下来。Time O(n) Space O(n)
    思路4：思路3的改进，在output列表上操作，第一遍遍历把左边连乘乘上，第二遍乘右边
    '''
    def productExceptSelf3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L, R = [1]*len(nums), [1]*len(nums)
        i, j = 1, len(nums)-2
        while i<len(nums) and j>=0:
            L[i] = L[i-1] * nums[i-1]
            R[j] = R[j+1] * nums[j+1] 
            i += 1
            j -= 1
        output = [0]*len(nums)
        for i in range(len(output)):
            output[i] = L[i]*R[i]
        return output
        
    def productExceptSelf(self, nums):
        output = [1]*(len(nums)+1)
        for i in range(1,len(nums)):
            output[i] = output[i-1] * nums[i-1]#
        for j in range(len(nums)-1, -1, -1):
            output[j] *= output[-1]
            output[-1] *= nums[j]     
        return output[:-1]
