class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        for i in range(len(A)):
            if not A[i]&1:
                A[i], A[l] = A[l], A[i]
                l += 1
        return A
