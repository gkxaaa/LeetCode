class Solution(object):
    '''
    思路1：遍历。一般的遍历有 bfs/dfs/loop 这三种。这里时bfs遍历最典型的例子，还有一道平方数的题也是。这里超时
    思路2：DP。这里dp可以是一维也可以用二维。
    '''
    def coinChange(self, coins, amount): # Time Limit Exceeded
        if amount==0: return 0
        queue = []
        queue.append((amount,1))
        coins.sort(reverse=True)
        while queue:
            node, layer = queue.pop(0)
            for coin in coins:
                if node - coin == 0: return layer
                elif node - coin > 0:
                    queue.append((node-coin, layer+1))
        return -1
                
    def coinChange_1d(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for v in range(1, amount+1):
            for coin in coins:
                if v-coin>=0:
                    dp[v] = min(dp[v], dp[v-coin]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
