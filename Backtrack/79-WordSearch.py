class Ans:
    def __init__(self):
        self.has = False
class Solution(object):
    '''
    思路1：一道搜索遍历题(回溯)。找到第一个字母开始上下左右遍历。找到第一个字母for循环，上下左右遍历dfs深度优先遍历.
    花了两个小时100%做完，主要卡在两个问题：
    1. dfs遍历时看过的字母后面不能再看，只能每次前向递归时开辟一块新的空间记录当前看过的字母，类似于全排列中函数自变量
    中的数组。！！！不能直接改变board[i][j]的值，因为哈希可以理解为全局变量，不管在哪一层递归改变它的值都会影响后面的搜索。
    每次开辟一块数组不是最优解，答案中在递归前向时标记board[i][j]并且保存到tmp，递归反向在把tmp重新赋值给board，眼前一亮。
    2. Tip：对于or或者and逻辑运算，or中只要有一个True后面不看了直接返回True，and只要有False直接返回False，减少时间复杂度。
    '''
    def exist_rec(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    seen = [(i,j)]
                    if self.rec(board, word[1:], i, j,seen):
                        return True
        return False
    
    def exist(self, board, word):
        if not board: return False
        rows, cols = len(board), len(board[0])
        for i in xrange(rows):
            for j in xrange(cols):
                if self.dfs(board, word, i, j):
                    return True
        return False
    
    #Time Limit Exceeded, 85/87 cases passed.
    # 超时的原因在于：若直接得到res=dfs(up) or dfs(down) or dfs(left) or dfs(right),只要这四里面有一个是True，后面就不用看了。
    # 但若像下面那样分开计算，不管上一行是否是True，下面都得计算，浪费了时间所以超时。
    def dfs_or(self, board, word, i, j):
        if not word:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False
        board[i][j], tmp = '#', board[i][j]
        down = self.dfs(board, word[1:], i+1, j)
        up = self.dfs(board, word[1:], i-1, j)
        right = self.dfs(board, word[1:], i, j+1)
        left = self.dfs(board, word[1:], i, j-1)
        board[i][j] = tmp
        return (up or down or right or left)
    
    def dfs(self, board, word, i, j):
        if not word:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False
        board[i][j], tmp = '#', board[i][j]
        res = self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i-1, j) \
            or self.dfs(board, word[1:], i, j+1) or self.dfs(board, word[1:], i, j-1)
        board[i][j] = tmp
        return res
    
    #Time Limit Exceeded, 85/87 cases passed.
    def rec(self, board, word, i, j, seen): 
        if not word:
            return True
        #print(word, i, j, seen)
        up=down=right=left=False
        if i+1<len(board) and board[i+1][j]==word[0] and (i+1,j) not in seen:#down
            down = self.rec(board, word[1:],i+1,j,seen+[(i+1,j)])
        if i>0 and board[i-1][j]==word[0] and (i-1,j) not in seen:#up
            up = self.rec(board, word[1:],i-1,j,seen+[(i-1,j)])
        if j+1<len(board[0]) and board[i][j+1]==word[0] and (i,j+1) not in seen:#right
            right = self.rec(board, word[1:],i,j+1,seen+[(i,j+1)])
        if j>0 and board[i][j-1]==word[0] and (i,j-1) not in seen:#left
            left = self.rec(board, word[1:],i,j-1,seen+[(i,j-1)])
        return (up or down or right or left)
  
