
# 题目地址
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/

# 前置知识
# 暂无

# 题目描述
# 你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。
# 其中 0 代表海洋，1 代表陆地，请你找出一个海洋单元格，
# 这个海洋单元格到离它最近的陆地单元格的距离是最大的。

# 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：
# (x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。

# 如果网格上只有陆地或者海洋，请返回 -1。

 

# 示例 1：
# image



# 输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释：
# 海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
# 示例 2：

# image


# 输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释：
# 海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
 

# 提示：

# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] 不是 0 就是 1

# 会超时

# import copy 
# def maxDistance(grid): 
#     n = len(grid)
    
#     def dfs(x, y, dist, visited):
#         # 如果当前格子越界或者已经访问过，则返回极大值（表示无法到达）
#         if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
#             return float('inf')
        
#         # 如果当前格子是陆地，则返回其到起点的曼哈顿距离
#         if grid[x][y] == 1:
#             return dist
        
#         visited.add((x, y))
        
#         # 递归搜索四个方向
#         min_dist = float('inf')
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + dx, y + dy
#             min_dist = min(min_dist, dfs(nx, ny, dist + 1, visited))
        
#         visited.remove((x, y))  # 回溯时移除已访问的点
#         return min_dist

#     max_dist = -1
#     # 遍历整个 grid
#     for i in range(n):
#         for j in range(n):
#             # 对每个水域（0），执行 DFS
#             if grid[i][j] == 0:
#                 visited = set()
#                 min_dist = dfs(i, j, 0, visited)
#                 if min_dist != float('inf'):
#                     max_dist = max(max_dist, min_dist)

#     return max_dist if max_dist != -1 else -1


## BFS
from typing import List
from collections import deque
class Solution:
    """
    思路：
        1.把所有陆地格子入队，陆地扩展到海洋
        2.处理只有陆地或者海洋的特殊情况，返回-1。
        3.遍历所有陆地节点的周围格子，若是海洋格子则入队，且距离distance + 1，bfs的每一层刚好与曼哈顿距离相对应
        4.已遍历到的海洋格子置为1，避免重复计算
        5.继续遍历已在队列中的格子的周围格子，直到没有海洋格子为止，此时队列为空，循环结束，返回distance
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        ## 队列上下左右附近距离是1 ，BFS每遍历一层距离+1
        n = len(grid)
        queue = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j]])
        if len(queue) in [0, n*n]:
            return -1

        dis = -1
        while queue:
            dis += 1
            for i in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx , y + dy
                    if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny]:
                        grid[nx][ny] = 1
                        queue.append((nx, ny)) 
        return dis 

grid = [[1,0,1],[0,0,0],[1,0,1]]
print(Solution().maxDistance(grid))
