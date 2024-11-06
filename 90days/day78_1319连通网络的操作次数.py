# 题目地址
# https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/


# 题目描述
# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。



# 示例 1：



# 输入：n = 4, connections = [[0,1],[0,2],[1,2]]
# 输出：1
# 解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
# 示例 2：



# 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# 输出：2
# 示例 3：

# 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# 输出：-1
# 解释：线缆数量不足。
# 示例 4：

# 输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
# 输出：0


# 提示：

# 1 <= n <= 10^5
# 1 <= connections.length <= min(n*(n-1)/2, 10^5)
# connections[i].length == 2
# 0 <= connections[i][0], connections[i][1] < n
# connections[i][0] != connections[i][1]
# 没有重复的连接。
# 两台计算机不会通过多条线缆连接。

from typing import List
## 并查集
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # 找到 x 和 y 的根节点
        rootX = self.find(x)
        rootY = self.find(y)
        
        # 如果两个元素属于不同的集合，则合并它们
        if rootX != rootY:
            # 按秩合并，将小树合并到大树上
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                # 如果 rank 相同，随便合并，并增加新树的 rank
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        # 判断 x 和 y 是否属于同一个集合
        return self.find(x) == self.find(y)


def makeConnected(n: int, connections: List[List[int]]):
    
    if len(connections) < n -1:
        return -1 
    
    uf = UnionFind(n)
    for i, j in connections:
        uf.union(i, j)

    # 找到父节点是自己的个数， 即联通分量的个数
    return sum(uf.find(x) == x for x in range(n)) - 1

import collections
## 会超时
def makeConnected(n: int, connections: List[List[int]]):
    if len(connections) < n -1:
        return -1 
    
    edges = collections.defaultdict(list)
    for i,j in connections:
        edges[i].append(j) 
        edges[j].append(i) 
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for i in range(n):
                if i in edges[node]:
                    dfs(i)
    
    res = 0 
    visited = set()
    for i in range(n):
        if i not in visited:
            dfs(i)
            res += 1
    return res - 1



n = 5
connections = [[0,1],[0,2],[3,4],[2,3]]
print(makeConnected(n, connections))
