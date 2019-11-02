class Solution(object):
    def reverse(self, x):
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
        
