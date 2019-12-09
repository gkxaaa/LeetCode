class Solution(object):
    '''
    思路1: 常规判断末尾是否为1,并右移
    思路2: 由于2进制只有1或0, 给n-1,若为奇数则消去了末尾的1,若末尾为0则把0反转并一直往前找到第一个1变它为0, 此时又有一个1被统计上。思路比较跳跃。
    '''
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        while n:
            if n & 1:
                counter += 1
            n = n >> 1
        return counter
    
    def hammingWeight(self, n):
        counter = 0
        while n:
            counter += 1
            n &= n - 1
        return counter
