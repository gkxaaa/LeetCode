class Solution:
    '''
    思路1: 暴力，从每个加油站开始往后走试，看是否能走一圈。Time O(n**2), Space O(1)
    思路2：one pass，当sum(gas-cost)>=0一定可以走完一圈。记下上一次gas[i]-cost[i]为正时的idx，走的时候后面碰到total_tank为负数时更新记下的idx，更新为下面再碰到的第一个正数的idx。
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nums = [gas[i]-cost[i] for i in range(len(cost))]
        if sum(nums)<0: return -1
        for start in range(len(nums)):
            tank, step, i = 0, 0, start
            while tank+nums[i]>=0:
                tank += nums[i]
                step += 1
                i += 1
                if step==len(nums):
                    return start
                if i>=len(nums):
                    i -= len(nums)
        return -1
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nums = [gas[i]-cost[i] for i in range(len(cost))]
        if sum(nums)<0: return -1
        idx, total_tank = None, 0
        for i in range(len(nums)):
            if total_tank + nums[i]<0:
                idx, total_tank = None, 0
            elif idx is None:
                idx = i
                total_tank += nums[i]
            else:
                total_tank += nums[i]
        return idx
    
