class Solution(object):
    '''
    思路1：全排列找第k个
    思路2：直接从坐往右查字典一样
    '''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        nums = [i+1 for i in range(n)]
        pers = 1
        for i in range(1,n+1):
            pers *= i
        while n>0:
            pers /= n
            for i in range(1,n+1):
                if k <= i*pers:
                    res += str(nums.pop(i-1))
                    break
            k -= (i-1)*pers
            n -= 1
        return res
