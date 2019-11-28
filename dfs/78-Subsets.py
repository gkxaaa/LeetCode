class Solution(object):
    '''
    思路：全排列和组合的区别是：比如[1,2,3]，
    全排列是第一层1时下面只能选2和3,第一层2时下面可以选1和3,第一层是3时下面可以选1和2.
    组合是第一层1时下面只能选2和3一样的,第一层2时（1上步选过了）下面只能选3,第一层是3时下面不可选. 就是下面选的数大于当前的数
    '''
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        def dfs(nums, MAX_len, i=0, comb=[]):
            if i==MAX_len:
                res.append(comb)
            for i in range(len(nums)):
                dfs(nums[i+1:], MAX_len, i+1, comb+[nums[i]])        
        for j in range(1,len(nums)+1):
            dfs(nums, j)
        return res
