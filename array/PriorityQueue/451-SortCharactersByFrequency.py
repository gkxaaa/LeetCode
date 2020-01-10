import heapq
class Solution(object):
    '''
    思路1: 遍历字符用字典记下不同字符的频率，然后根据每个字符频率从大到小写字符。Time O(m*logm), Space O(m), m是不同字符的数量
    思路2：优先队列，基于思路1,在根据字典每个字符频率大小排序时，用堆排序TopK。这里K等于不同字符个数，Time O(m*logK), K从m开始递减因此更快，Space O(m)
    思路3: 桶排序, Time O(n), n=len(s), 字符最大重复频率 < len(s)
    '''
    def frequencySort_buckets(self, s):
        d, res = dict(), ''
        for si in s:
            d[si] = d.get(si, 0) + 1
        # create buckets
        nums = [None]*len(s)
        # sort buckets in order, [[bucket1], [bucket2],...]
        # The chars in the same bucket have the same frequency
        for char, count in d.items():
            if not nums[count-1]:
                nums[count-1] = [char]
            else:
                nums[count-1].append(char)
        for i, bucket in enumerate(nums):
            if bucket:
                for char in bucket:
                    res = (i+1) * char + res
        return res
        
    def frequencySort_heapq(self, s):
        d, res = dict(), ''
        for si in s:
            d[si] = d.get(si, 0) + 1
        minheap = [(v, k) for k, v in d.items()]
        heapq.heapify(minheap)
        while minheap:
            t = heapq.heappop(minheap)
            res = t[0]*t[1] + res
        return res
        
    def frequencySort_bruteForce(self, s):
        """
        :type s: str
        :rtype: str
        """
        d, res = dict(), ''
        for si in s:
            d[si] = d.get(si, 0) + 1
        for count, char in sorted(zip(d.values(), d.keys()),reverse=True):
            res += count*char
        return res
