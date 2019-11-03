import math
class Solution(object):
    def reverse(self, x):
        if not x: return 0
        MIN, MAX = -2**31, 2**31-1
        res, positive = 0, x>0
        x = abs(x)
        while x:
            remainder = x % 10
            x = x / 10
            if positive and (res>MAX/10 or (res==MAX/10 and remainder>7)):
                return 0
            if (not positive) and (res>abs(MIN)/10 or (res==abs(MIN)/10 and remainder>8)):
                return 0
            res = res * 10 + remainder
        return res if positive else -res
    
    def reverse_ugly(self, x):
        if not x: return 0
        MIN, MAX = -2**31, 2**31-1
        res, positive = 0, x>0
        while x:
            if positive:
                remainder = x % 10
                x = x / 10
            else:
                remainder = int(x - math.ceil(x/10.0)*10)
                x = int(math.ceil(x/10.0))
            if res>MAX/10 or (res==MAX/10 and remainder>7):
                return 0
            elif res<MIN/10 or (res==MAX/10 and remainder<-8):
                return 0
            res = res * 10 + remainder
        return res
        
    def reverse_false(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return 0
        lower, upper = -2**31, 2**31-1
        queue = []
        positive, x = x>0, abs(x)
        while x:
            queue.append(x%10)
            x = x/10
        res = 0
        while queue:
            res += queue.pop(0)*(10**len(queue))
            
        if res<lower or res>upper:
            return 0
        elif positive:
            return res
        else:
            return -res
