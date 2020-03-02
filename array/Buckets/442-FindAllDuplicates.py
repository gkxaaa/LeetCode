class Solution:
    '''
    思路：数组内映射，桶。当前数字作为idx映射，若映射的值大于n则说明这个数被访问
          过。一点需要注意，有可能出现死循环的情况，所以每次映射前需要判断是否循环
          是的话直接给两数加n，continue。最后知道遍历结束
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n, res = len(nums)+1, []
        for i in range(len(nums)):
            k = nums[i] if nums[i]<n else nums[i]-n
            if nums[k-1]>n:
                res.append(k)
            else:
                nums[k-1] += n
        return res
                    
