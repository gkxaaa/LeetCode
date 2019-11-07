class Solution(object):
    '''
    思路一：把第一行赋值给最后一列，第二行赋值给倒数第二列,......以此类推。问题：要么需要一个
    三角矩阵保存被覆盖的数;要么把最后一列和第一行交换，对下一行的赋值造成复杂的情况
    （被上一步操作覆盖掉的数字重新去第一行去取）
    思路二：从外围顺时针转圈赋值，由外向内循环。如果只要顺时针遍历的话容易，控制x和y加一减一，
    现在问题是如何顺时针赋值？
    思路三：编程实现这道题没有什么思维上的跳跃或奇思妙想，思想很简单。每次给四个角上的数字（连接起来是正方形顶点的四个数顺时针赋值）
    思路四：看了答案后还有一个思路，先转置后交换行，或先交换行后转置。
    转置：matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    交换行：matrix[:] = matrix[::-1]
    '''
    def rotate(self, matrix):
        D = len(matrix)
        step = 0
        while D-2*step > 1:
            for i in range(step, D-1-step):
                matrix[step][i], matrix[i][D-1-step], matrix[D-1-step][D-1-i], matrix[D-1-i][step] = matrix[D-1-i][step], matrix[step][i], matrix[i][D-1-step], matrix[D-1-step][D-1-i]
            step += 1
            
    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        tmp = []
        rows, cols = len(matrix), len(matrix[0])
        for j in range(cols-1, -1, -1):
            for i in range(rows):
                matrix[i][j] = matrix[cols-j][i]
                if i < rows-1:
                    matrix[cols-j][i] = matrix[i+1][j]
    
    def rotate2(self, matrix):
        D = len(matrix)
        step = 0
        while D > 1:
            tmp = []
            # right direction
            for i in range(D):
                tmp.append(nums[i][D-1-step])
                nums[i][D-1-step] = nums[step][i]
            # down direction
            tmp2 = [] ##############每个方向都需要一个数组缓存！！！
            for i in range(D):
                nums[D-1-step][i] = tmp[-i-1]
