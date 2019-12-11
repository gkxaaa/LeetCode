import heapq
class Solution(object):
    '''
    思路1；字典保存每个数字频率，元组排序取前k个。Time O(n*logn) Space O(n)
    思路2：优先队列
    '''
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d, minheap = dict(), []
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for i, (key, value) in enumerate(d.items()):
            if i < k:
                heapq.heappush(minheap, (value, key))
            elif value > minheap[0][0]:
                heapq.heapreplace(minheap, (value, key))
        return [t[1] for t in minheap]
