class Solution:
    # 滑动窗口
    def containsNearbyAlmostDuplicate_window(self, nums, k, t): # Time Limit Exceeded, 40/41 cases passed.
        if len(nums)<=1 or k==0: return False
        for i in range(len(nums)):
            for j in range(max(i-k, 0), i):
                if abs(nums[i]-nums[j])<=t:
                    return True
        return False
    # 桶思想
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums)<=1 or k==0 or t<0: return False
        bucket = {}
        for i in range(len(nums)):
            bucket_idx = nums[i]//(t+1)
            if bucket_idx in bucket:
                return True
            elif bucket_idx-1 in bucket and abs(nums[i]-bucket[bucket_idx-1])<=t:
                return True
            elif bucket_idx+1 in bucket and abs(nums[i]-bucket[bucket_idx+1])<=t:
                return True
            else:
                bucket[bucket_idx] = nums[i]
            if i >= k: # Guarantee k numebrs in bucket everytime
                removed_idx = nums[i-k]//(t+1)
                bucket.pop(removed_idx)
        return False
