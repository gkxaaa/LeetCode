class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set()
        for n in nums:
            if n in d:
                return True
            d.add(n)
        return False
