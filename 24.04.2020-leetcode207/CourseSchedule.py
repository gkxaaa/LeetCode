class Solution:
    '''
    思路1：Brute Force， prerequisite中是否能找到一个环路从从个点在回到某个点。
           遍历每个节点，dfs深度优先搜索。每个点可能的分支可实现保存在字典中
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = dict()
        for i in range(len(prerequisites)):
            for j in range(len(prerequisites)):
                if i==j: continue
                if prerequisites[i][1] == prerequisites[j][0]:
                    d[i] = d.get(i, []) + [j]
        for i in range(len(prerequisites)):
            if i in d and self.dfs(d, prerequisites, i, [0]*len(prerequisites)):
                return False
        return True
        
    def dfs(self, d, prerequisites, start, visited):
        if start not in d:
            return False
        elif visited[start]:
            return True
        is_loop = False
        visited[start] = 1
        for next_start in d[start]:
            is_loop = is_loop or self.dfs(d, prerequisites, next_start, visited)
        visited[start] = 0
        return is_loop
