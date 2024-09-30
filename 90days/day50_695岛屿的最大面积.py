# 题目地址
# https://leetcode-cn.com/problems/max-area-of-island/

# 前置知识
# 暂无

# 题目描述
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 一个 岛屿 是由一些相邻的 1 （代表土地） 构成的组合，
# 这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
# 你可以假设 grid 的四个边缘都被 0（代表水）包围着。
# 找到给定的二维数组中最大的岛屿面积。（如果没有岛屿，则返回面积为 0 。)

# 示例 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

# 示例 2:

# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵，返回 0。

 
# 注意：给定的矩阵 grid 的长度和宽度都不超过 50
from collections import deque 
def maxAreaOfIsland(grid):
    res = 0
    length = len(grid[0])
    height = len(grid)
    def bfs(x, y):
        queue = deque([(x, y)])
        area = 1
        visited = set()
        visited.add((x, y))
        while queue:
            r, c = queue.popleft()
            for i, j in [ (-1, 0), (1, 0), (0, -1), (0, 1)]: # 上下左右
                nx, ny = r + i, c + j 
                if 0 <= nx < height and 0 <= ny < length and (nx, ny) not in visited:
                    if grid[nx][ny] == 1:
                        visited.add((nx, ny))
                        area += 1
                        # print(x, y, nx, ny, area)
                        queue.append((nx, ny) )
        return area 
    
    
    
    def dfs(x, y):
        if not (0 <= x < height and 0 <= y < length) or (x, y) in visited or grid[x][y] == 0:
            return 0
        
        visited.add((x, y))
        area = 1  # 当前格子的面积
        
        # 四个方向递归累加面积
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            area += dfs(x + i, y + j)
        return area
    
    def dfs(x, y):
        area = 1
        visited.add((x, y))
        for i, j in [ (-1, 0), (1, 0), (0, -1), (0, 1)]: # 上下左右
            nx, ny = x + i, y + j 
            if 0 <= nx < height and 0 <= ny < length and (nx, ny) not in visited:
                if grid[nx][ny] == 1:
                    visited.add((nx, ny))
                    area += dfs(x, y)
            else:
                return 0 
        return area 
    
    for i in range(height):
        for j in range(length):
            if grid[i][j] == 1:
                visited = set()
                res = max(res, bfs(i, j))
    return res

grid = [[0,1,1],
        [1,1,0],
        [1,1,0],]

print(maxAreaOfIsland(grid))


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]