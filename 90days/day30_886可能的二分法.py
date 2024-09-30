# 题目地址
# https://leetcode-cn.com/problems/possible-bipartition/

# 前置知识
# 图的遍历
# DFS
# 题目描述
# 给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

# 每个人都可能不喜欢其他人，那么他们不应该属于同一组。

# 形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

# 当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。

 

# 示例 1：

# 输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
# 示例 2：

# 输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
# 示例 3：

# 输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
 

# 提示：

# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# 对于dislikes[i] == dislikes[j] 不存在 i != j

from typing import List
from collections import deque
def possibleBipartition(n: int, dislikes: List[List[int]]):
    # 构建邻接表
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    
    # 用于存储每个节点的颜色，0表示未染色，1和-1表示两种不同的颜色
    color = {}
    
    # def dfs(node, c=1):  # 对所有与node关联节点染色，并进行判断
    #     color[node] = c
    #     for neighbor in graph[node]:
    #         if neighbor not in color:
    #             if not dfs(neighbor, -c):  # 对邻居节点染色-c
    #                 return False
    #         elif color[neighbor] == color[node]:  # 如果与邻居节点颜色一样返回false
    #             return False
    #     return True

    def bfs(node, c = 1):
        queue = deque([node])
        color[node] = c 
        
        while queue:
            q = queue.popleft()

            for neighbor in graph[q]:
                if neighbor not in color:
                    color[neighbor] = -color[q] 
                    queue.append(neighbor)
                elif color[neighbor] == color[q]:
                    return False
        return True

    def dfs(node, c = 1):
        if node in color:
            return color[node]==c
        color[node] = c 
        
        for neighbor in graph[node]:
            if not dfs(neighbor, -c):
                return False
        return True
    
    for node in range(1, N + 1):
        if node not in color:
            if not dfs(node):
                return False
    
    return True, color
N = 4
dislikes = [[1,2],[1,3],[2,4]]
possibleBipartition(N, dislikes)