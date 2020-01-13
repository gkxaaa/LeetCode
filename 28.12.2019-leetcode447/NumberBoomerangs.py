class Solution(object):
    '''
    思路1:Brute Force，以每个点为中心遍历剩下的点，记下离当前点距离相同点。Time O(n**2), Space O(n)
    '''
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            d = dict()
            for j in range(len(points)):
                dist = (points[i][1]-points[j][1])**2 + (points[i][0]-points[j][0])**2
                res += d.get(dist, 0)      
                d[dist] = d.get(dist, 0) + 1
        return 2*res
