class Solution(object):
    '''
    思路1: 暴力O(n**4)
    思路2: 空间换时间。为了简化问题，若为2SUM问题,同时遍历listA和B，建立两个set。
             一个记录B中出现过的数，一个记录A中出现过的数。A中看新的数时，
             先看里面有没有记录过B中的数加起来和为0,有记下没有把当前数加入B set中.
             4个list一样的，前三个list等效为listA Time O(n**3), Space O(n)
    思路3: 空间换时间，也可以达到Time O(n**2), Space O(n**2)
    
    '''
    def fourSumCount(self, A, B, C, D):
        N, d, res = len(A), {}, 0
        for i in range(N):
            for j in range(N):
                d[-A[i]-B[j]] = d.get(-A[i]-B[j], 0) + 1
        for i in range(N):
            for j in range(N):
                res += d.get(C[i]+D[j], 0)
        return res
        
    def fourSumCount_Time3_Space1(self, A, B, C, D): # Time O(n**3), Space O(n)
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N, res = len(A), 0
        for i in range(N):
            for j in range(N):
                d1, d2 = {}, {}
                for k in range(N):
                    res += d1.get(A[i]+B[j]+C[k], 0)
                    d2[-A[i]-B[j]-C[k]] = d2.get(-A[i]-B[j]-C[k], 0) + 1
                    res += d2.get(D[k], 0)
                    d1[-D[k]] = d1.get(-D[k], 0) + 1
        return res
