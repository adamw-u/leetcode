# 题目地址
# https://leetcode-cn.com/problems/number-of-provinces/

# 题目描述
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

# 返回矩阵中 省份 的数量。

# 示例 1：


# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 示例 2：


# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
 

# 提示：

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class UniFind:
    def __init__(self, n):
        # 初始化 n 个元素，每个元素的父节点指向自己
        self.parent = [i for i in range(n)]
        # 初始化每个集合的大小（也可以理解为秩 rank，用于按秩合并）
        self.rank = [1] * n

    def find(self, x):
        # 查找 x 所在的集合根节点，并进行路径压缩
        if self.parent[x] != x:
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


def findCircleNum(isConnected):
    """
    UniFind
    """
    n = len(isConnected)
    uf = UniFind(n)
    for i in range(n):
        for j in range(n):
            if i != j and isConnected[i][j] == 1:
                uf.union(i, j)
    provinces = sum(uf.parent[i] == i for i in range(n))  # 如果父节点是自己，说明他不跟其他节点相连，代表一个省份
    return provinces


from collections import deque
def findCircleNum(isConnected):
    """
    BFS
    """
    n = len(isConnected)
    visited = set()
    provinces = 0
    
    for c in range(n): 
        if c not in visited:
            queue = deque([c])
            provinces += 1
        while queue:
            q = queue.popleft()
            for j in range(n):
                if isConnected[q][j] == 1 and j not in visited:
                    visited.add(j)
                    queue.append(j)
        
        if len(visited) == n:
            return provinces   # 退出遍历

def findCircleNum(isConnected):
    n = len(isConnected)
    
    def dfs(c, visited):
        if c not in visited:
            visited.add(c)

            for j in range(n):
                if isConnected[c][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j, visited)
    provinces = 0
    visited=set()
    for c in range(n): 
        if c not in visited:
            dfs(c, visited)
            provinces += 1
    return provinces

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(findCircleNum(isConnected))