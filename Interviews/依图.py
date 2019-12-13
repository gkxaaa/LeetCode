'''
要求完成一个函数
函数的输入是一个2维的矩阵
矩阵的每个元素都是 int
1. 每个元素可以和其上下左右4个方向的元素连接起来构成路径
2. 路径上除了第一个元素以外的每个元素都比前一个元素大的路径是 [递增路径]
函数需要返回 [矩阵中最长递增路径的长度]

123
456
789 -> 5

345
216
987 -> 9

----------------------------------------------------------------
'''

def dfs(matrix, i, j, pre=0, length=0):
    global res
    if not 0<=i<rows or not 0<=j<colss or not board[i][j] or matrix[i][j]>pre:
        res = max(res, length)
        return
    board[i][j] = Fasle
    if i+1<rows:
        dfs(matrix, i+1, j, matrix[i][j], length+1)
    if i-1>=0:
        dfs(matrix, i-1, j, matrix[i][j],length+1)
    if j+1<cols:
        dfs(matrix, i, j+1, matrix[i][j],length+1)
    if j-1>=0:
        dfs(matrix, i, j-1, matrix[i][j], length+1)
    board[i][j] = True


def maxLength(matrix):
    if not matrix: return 0
    global res
    res = -1
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            board = [[True]*cols for _ in range(rows)]
            dfs(matrix, i, j)
    return res
