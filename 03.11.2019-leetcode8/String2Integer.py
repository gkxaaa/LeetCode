class Solution(object):
    '''
    思路：解题思路很容易，难点在于边界条件（正负）和是否溢出。因为正数最大可以到2**31-1, 负
    数-2**31, 所以不能把所有负数直接转换为正数来做，除非考虑到-2**31时的边界条件。所以算
    法思路就是先判断正负，然后迭代
    '''
    def myAtoi(self, char):
        INT_MAX, INT_MIN = 2**31-1, -2**31
        char = char.strip()
        if not char: return 0
        char = char.split()[0]
        if char[0] in '+':
            positive = True
        elif char[0] =='-':
            positive = False
        elif char[0] in '0123456789':
            positive = True
            char = '+' + char
        else:
            return 0
        res = 0
        for s in char[1:]:
            if s not in '0123456789':
                return res
            if positive:
                if res>INT_MAX/10 or (res==INT_MAX/10 and int(s)>7):
                    return INT_MAX
                else:
                    res = res * 10 + int(s)
            else:
                if res<INT_MIN/10+1 or (res==INT_MIN/10+1 and int(s)>8):
                    return INT_MIN
                else:
                    res = res * 10 - int(s)
        return res
            
