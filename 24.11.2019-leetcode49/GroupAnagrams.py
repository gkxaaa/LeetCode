class Solution(object):
    '''
    思路1:Brute Force. 给每个词排序，往后遍历碰到相同的append进res，并标记已选。复杂度O(K*logK*n**2)
    思路2:哈希,一个排序后的元组mapping一个列表，结果是字典的values
    思路3:character count哈希
    '''
    def groupAnagrams_hash(self, strs):
        d = collections.defaultdict(list)
        for _str in strs:
            d[tuple(sorted(_str))].append(_str)
        return d.values()
    
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for _str in strs:
            count = [0]*26
            for c in _str:
                count[ord(c)-ord('a')] += 1
            d[tuple(count)].append(_str)
        return d.values()
    
    def groupAnagrams_BruteForce(self, strs): #100/101 cases passed, Time Limit Exceeded
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        for i in range(len(strs)):
            if strs[i]!='#':
                anagram = [strs[i]]
                si = ''.join(sorted(strs[i]))
                for j in range(i+1,len(strs)):
                     if strs[j]!='#':
                        sj = ''.join(sorted(strs[j]))
                        if si==sj: 
                            anagram.append(strs[j])
                            strs[j]='#'
                res.append(anagram)                        
        return res
