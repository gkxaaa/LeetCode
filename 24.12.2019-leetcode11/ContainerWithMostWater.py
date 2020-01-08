class Solution:
    '''
    思路：此题的关键在于，越往左越高或者越往右越高，结果越好。两边边界每次如果高
    的往內缩的话，碰到更高的没有用，碰到更低的更不顶用。所以每次低的边界往内缩一格
    '''
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = -1
        while r!=l:
            area = min(height[r],height[l])*(r-l)
            res = max(res, area)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return res
        
    def maxArea_bruteForce(self, height: List[int]) -> int:
        MAX = -1
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                MAX = max(MAX, (j-i)*min(height[i], height[j]))
        return MAX
