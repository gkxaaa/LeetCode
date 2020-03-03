class Solution:
    '''
    思路1: 全排列A，每次计算对于B的优势。Time O(2**n*m) Space O(1)
    思路2: dp，Time O(n**2) Space O(n) 看错问题，以为是求最大优势的个数
           1.状态：dp[i]第一个到第i个数字，A最大领先个数。
           2.递推：两种情况A[i]保留位置，或者和前面每个位置交换位置
           3.初始状态：dp[0]=0
    思路3: 参考答案，贪心算法. Time O(NlogN) Space O(1)
           A中最差的那张牌应该打B中最差的那张，如果大不了就输给B中最大的数。
           需要对A，B排序,并记下本来B中最大牌的位置，输了后滑动窗口
    '''
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [0]*len(A)
        mapB = sorted(zip(B, range(len(B))))
        A, B = sorted(A), sorted(B)
        l, r = 0, len(B)-1
        for i in range(len(A)):
            if A[i]>B[l]:
                res[mapB[l][-1]] = A[i]
                l += 1
            else:
                res[mapB[r][-1]] = A[i]
                r -= 1
        return res
        
    def advantageCount_wrong(self, A: List[int], B: List[int]) -> List[int]:
        dp = [0]*(len(A))
        dp[0] = 1 if A[0]>B[0] else 0
        for i in range(len(A)):
            for j in range(i):
                dv1 = A[j]>B[j] + A[i]>B[i] # not change
                dv2 = A[i]>B[j] + A[j]>B[i] # change pos
                if dv2>dv1:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1]
        print(dp)
        return dp[-1]
