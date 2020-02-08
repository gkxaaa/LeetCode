class Solution:
    '''
    思路1：Brute Force，从每个数开始作为continuous subarrays 第一个数，往后遍历看
           结果是否为k。Time O(n**2)，Ｓpace O(1)
    思考2: 若遍历一遍，不到最后一个数是不知道subarray是否和为k，为方便理解假设k为
           0。所以在遍历时应该时间换空间，储存下些信息。可以储存到当前数的前面所有
           数字累加之和，若后面的数累加求和得到的结果在储存集合中，说明当前累加和减
           掉储存的那个数之后就变为0,也就是说从储存的那个数开始到当前数，这一整個
           subarray中和为0，即找到一个subarray和为k
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_from_left_dict = {0:1}
        sum_from_left, res = 0, 0
        for i in range(len(nums)):
            sum_from_left += nums[i]
            if sum_from_left-k==0 or sum_from_left-k in sum_from_left_dict:
                res += sum_from_left_dict[sum_from_left-k]
            sum_from_left_dict[sum_from_left] = \
                      sum_from_left_dict.get(sum_from_left, 0) + 1
        return res
