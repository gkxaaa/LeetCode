class Solution(object):
    '''
    思路1：直觉解法，从前往后遍历遇到0时一般跳过，除非前面有1，交换；
          遇到2时从最后往回数找到第一个不为2的数，交换，交换后还要考虑此时新的数是0还是1；
          遇到1时，若前面有1，pass，若前面没出现过1，标记此时1的index
    思路2：思路1写程序时需要条例及其清楚，而且写出来代码也不是最简洁，最美观的。这里运用3个指针的概念极大的帮助代码的可懂度，见解度。
          左边界指针p0，右边界指针p1，当前curr，
          遇到0，左边界向右移动1个，curr也加一；
          遇到2，和右边界数交换，有边界p1减一缩小一格
          遇到1，curr加1，过
          控制左右边界和curr，当curr达到右边界时，结束程序
    '''
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx1, idx2 = None, len(nums)-1
        for i in range(len(nums)):
            if nums[i]==2:
                while idx2>i and nums[idx2]==2:
                    idx2 -= 1
                if idx2==i: return
                nums[i], nums[idx2] = nums[idx2], nums[i]
            if nums[i]==0 and idx1 is not None:
                nums[i], nums[idx1] = nums[idx1], nums[i]
                idx1 += 1
            elif nums[i]==1 and idx1 is None:
                idx1 = i
