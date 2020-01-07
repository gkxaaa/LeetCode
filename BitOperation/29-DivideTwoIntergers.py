class Solution(object):
    def divide(self, dividend, divisor):
        if dividend==0: return 0
        positive = (dividend>0) is (divisor>0)
        dividend, divisor = abs(dividend), abs(divisor)
        res, i = 0, 1
        while dividend>=divisor:
            i, base = 1, divisor
            while dividend >= base:
                dividend -= base
                res += i
                i <<= 1
                base <<= 1
        return min(res, 2**31-1) if positive else max(-res, -2**31)         
        
    def divide1(self, dividend, divisor): # Time Limit Exceed, 10 / 989 test cases passed.
        if dividend==0: return 0
        positive = (dividend>0) is (divisor>0)
        m, n = abs(dividend), abs(divisor)
        res = -1
        while m >= 0:
            m -= n
            res += 1
        return min(res, 2**32-1) if positive else max(-res, -2**31)
    
    def divide2(self, dividend, divisor): # Time Limit Exceed, 19 / 989 test cases passed.
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0: return 0
        positive = dividend*divisor>0
        m, n = abs(dividend), abs(divisor)
        left, right = 1, m
        while right>=left:
            middle, SUM = (left+right)//2, 0
            for _ in xrange(n):
                SUM += middle
            if SUM == m:
                return min(middle, 2**31-1) if positive else max(-middle, -2**31)
            if SUM > m:
                right = middle - 1
            else:
                left = middle + 1
        return min(right, 2**32-1) if dividend*divisor>0 else max(-right, -2**31)
