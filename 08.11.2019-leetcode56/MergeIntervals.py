class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<=1:return intervals
        interv = sorted(intervals)
        res = []
        valid = [interv[0][0], interv[0][1]]
        for i in range(1, len(interv)):
            if interv[i][1]<=valid[1]:
                pass
            elif interv[i][0]<=valid[1]:
                valid[1] = interv[i][1]
            else:
                res.append(valid)
                valid = [interv[i][0], interv[i][1]]
        res.append(valid)
        return res
    #我的思路是保证一个有效的interval，然后加入列表。答案的思路是先加，然后根据
    #下一个interval来判断是否应该改变当前interval的右边界，因为左边界经过排序肯定没问题 
    def merge_answer(self, intervals):
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
