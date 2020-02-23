# -*- coding:utf-8 -*-
class Solution:
    '''
    思路1: Brute Force，从1开头一直到tsum//2开头连续的数字求和，Time O(NlogN), Space O(1)
    思路2: 空间换时间sliding window，保持win内连续整数和加起来不超过N。若超过N，左边界右移，不超过右边界右移。
          需要额外Space O(logN)记录访问过的数字和，Time优化到O(N)
    '''
    def FindContinuousSequence(self, tsum):
        SUM, l, n = 0, 0, 1
        sum_list, res = [0], []
        while l+2!=len(sum_list):
            while SUM-sum_list[l]<tsum: #SUM代表从1开始到当前数的和，右边界减去左边界为窗内数字和
                SUM += n
                sum_list.append(SUM)
                n += 1
            while l+2<len(sum_list) and SUM-sum_list[l]>=tsum: #保证窗不能太短，l不能到倒数第二个位置
                if SUM-sum_list[l]==tsum: res.append(range(l+1, n))
                l += 1
        return res
