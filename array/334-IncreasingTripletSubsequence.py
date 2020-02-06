class Solution:
    '''
    思路1: Brute Force, Time O(n**3), Sapce O(1)
    思路2: 遍历列表，若发现当前数大于前面一个数记下当前数为m和前面数MIN，继续遍历，
           做两件事 1.看当前数是否大于储存的数m，是直接返回True; 
                    2.看是否更新MIN和m。若当前数大于储存的MIN或者当前数大于前一个数
                      时更新m；若在当前数大于前一个数情况时，也要更新MIN
    '''
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        m, l, pre = float('inf'), float('inf'), nums[0]
        for i in range(1, len(nums)):
            if nums[i]>m:
                return True
            if nums[i]>pre or nums[i]>l:
                m = min(m, nums[i])
                l = min(l, pre)
            pre = nums[i]
        return False
