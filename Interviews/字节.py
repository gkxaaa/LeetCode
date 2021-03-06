征服者
你是一名征服者。现有n个城堡编号1~n，每个城堡有一定的财富值，你希望通过征服这些城堡来获得最大的总财富值。但是你的兵力有限，
仅能帮助你征服其中的任意m座城堡。并且，对于某些城堡，必须先征服其守护城堡才能再征服该城堡（每个城堡的守护城堡至多一个，守护关系不成环）

输入描述
第一行两个整数 N,M
在接下来的N行里，每行包括2个整数，a,b. 在第 i 行，a 代表要攻克第 i 个城堡必须先攻克第 a 个城堡，如果 a = 0 则代表可以直接攻克第 i 个城堡。b 代表第 i 个城堡的宝物数量, b >= 0
输出描述
可获得的最大财富值

示例1
输入
3 2
0 1
1 3
1 4
输出
5

dMap = {1:[2,3,5], 3:[6,4]}
dValue = {1:2, 2:5}
def dfs(i):
    if i not in d or m==M:
        retrun  0, 0
    v0 = -1
    for j in dMap[i]:
        v, m = dfs(j)
        v += dValue[j]
        v0 = max(v0, v)
        m += 1
    return v0, m

MAX, tmp = -1, []
for key in dMap.keys():
    v, m = dfs(i)
    if m==M:
        MAX = max(MAX, v)
    else:
        tmp.append((v, m))
