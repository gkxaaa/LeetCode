class Solution(object):
    '''
    思路1：只需分别检查每行，列或方块中数字是否有重复。检查的时候需要字典记下访问过得数字。时间复杂度O(3*n**2), 空间O(9)
    思路2：1 pass，需要9个字典保存列和9个字典保存方格
    '''
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        boxes = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j].isdigit():
                    if (row.get(board[i][j], 0) or cols[j].get(board[i][j], 0) or
                    boxes[i//3*3+j//3].get(board[i][j], 0)):
                        return False
                    row[board[i][j]], cols[j][board[i][j]],boxes[i//3*3+j//3][board[i][j]] = 1 ,1, 1
        return True
