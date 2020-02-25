class Solution:
    '''
    思路：只要在prerequistes中找闭环，那么就不能选够.其次依次向stack中添加访问过的节点
          涉及到局部的flag控制和全局flag控制
    '''
    def findOrder(self, n, prerequisites):
        d = {k:[] for k in range(n)}
        for adv, basic in prerequisites:
            d[basic].append(adv)
        self.res, self.is_possible = [], True
        visited_one_path, visited = [0]*n, set()
        def dfs(basic):
            if not self.is_possible: # 不加有环时程序停不下来！
                return
            if visited_one_path[basic]:
                self.is_possible = False
                return
            visited_one_path[basic] = 1
            for adv in d[basic]:
                dfs(adv)
            visited_one_path[basic] = 0
            #不能放在前面。若先碰到到尽头的节点，会被误以为起始节点导致顺序出错
            if basic not in visited:#当前这条path中有之前path或单个节点被遍历过，跳过不影响结果顺序
                self.res.append(basic)
            visited.add(basic)
        for basic in d.keys():
            if basic not in visited: #图中节点遍历过的话后面不需再遍历
                dfs(basic)
        return self.res[::-1] if self.is_possible else []
        
        
        
        
    def findOrder_tree_idea(self, n, prerequisites):# 存放数据的结构不好，可以判断是够有环但五环
        if not prerequisites: return range(n)
        d = [[] for _ in range(n)]
        for adv, basic in prerequisites:
            d[basic].append(adv)
        self.res, self.is_possible = [], True
        def dfs(basic, visited): #找到是否有环并返回上课顺序
            if visited[basic]==1:
                self.is_possible = False
                return
            elif not d[basic]:
                return 
            self.res.append(basic)
            visited[basic] = 1
            for adv in d[basic]:
                dfs(adv, visited)
            visited[basic] = 0
        for basic in range(len(d)):
            if d[basic]:
                dfs(basic, [0]*n)
        if self.is_possible and len(self.res) < n:
            for i in range(n):
                if len(self.res)==n:
                    return self.res
                if i not in set(self.res):
                    self.res.append(i)
        return self.res if self.is_possible else []
