class Solution(object):
    '''
    思路1：哈希表记录每个元素出先的次数，第二遍找出单独的1个, O(2*n), O(n)
    思路2：维护一个set，后面的数在set里，删除set中这个数，最后返回set里剩下的数。O(n), O(n/2)
    思路3: 为每一个遍历剩下的数字看是否能找到相同的，找不到返回结果。O(n**2),O(0)
    思路4：实现O(n), O(1)不用额外空间，那么需要在当前数组做一些标记。1.通过加一个MAX 2.或者数组内mapping 
           3.或者更新一个常数比如当前所有数字的和，差，乘积。都行不通。
           
           分析问题，当前数字怎么知道前面是否出现过呢？只能把前面信息存起来或者再遍历一遍，算法就是时间和空间的博弈。
           所以通过算法实现不可能。那么思路转换到是否用数学方法，比如所有数字加起来是奇数或者偶数，也不行。答案中二进制XOR操作眼前一亮。
    '''
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            idx = None
            for j in range(len(nums)):
                if i!=j and nums[j]==nums[i]:
                    idx = j
                    break
            if idx is None: return nums[i]
    
    def singleNumber1(self, nums):
        d = dict()
        for n in nums:
            d[n] = d.get(n,0) + 1
        for key, value in d.items():
            if value == 1: return key
    
    def singleNumber2(self, nums):         
        s = set()
        for n in nums:
            if n in s: s.remove(n)
            else: s.add(n)
        return list(s)[0]
    
    def singleNumber(self, nums): 
        a = 0
        for n in nums:
            a ^= n
        return a
