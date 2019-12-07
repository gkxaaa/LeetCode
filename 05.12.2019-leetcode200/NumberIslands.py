class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        board = [[0]*cols for _ in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and not board[i][j]:
                    res += self.bfs(grid, board, i, j)
        return res
                    
    def bfs(self, grid, board, i, j):
        queue = []
        queue.append((i,j))
        while queue:
            i, j = queue.pop(0)
            if 0<=i<len(grid) and 0<=j<len(grid[0]) \
                and not board[i][j] and grid[i][j] == '1':
                board[i][j] = 1
                queue.append((i+1,j))
                queue.append((i-1,j))
                queue.append((i,j+1))
                queue.append((i,j-1))
        return 1
    
    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        board = [[0]*cols for _ in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and not board[i][j]:
                    res += self.dfs(grid, board, i, j)   
        return res
    
    def dfs(self, grid, board, i, j):
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]) \
            or board[i][j] or grid[i][j]=='0':
            return 0
        board[i][j] = 1
        self.dfs(grid, board, i+1, j)
        self.dfs(grid, board, i-1, j)
        self.dfs(grid, board, i, j+1)
        self.dfs(grid, board, i, j-1)
        return 1
