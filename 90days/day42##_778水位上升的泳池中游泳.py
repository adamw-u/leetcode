# 题目地址
# https://leetcode-cn.com/problems/swim-in-rising-water

# 前置知识
# 暂无

# 题目描述
# 在一个 N x N 的坐标方格  grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

# 现在开始下雨了。当时间为  t  时，此时雨水导致水池中任意位置的水位为  t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

# 你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台  (N-1, N-1)？

# 示例 1:

# 输入: [[0,2],[1,3]]
# 输出: 3
# 解释:
# 时间为 0 时，你位于坐标方格的位置为 (0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

# 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
# 示例 2:

# 输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# 输出: 16
# 解释:
# 0 1 2 3 4
# 24 23 22 21 5
# 12 13 14 15 16
# 11 17 18 19 20
# 10 9 8 7 6

# 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的

# 提示:

# 2 <= N <= 50.
# grid[i][j] 位于区间 [0, ..., N*N - 1] 内。

# 优先队列解法
from typing import List 
import heapq  
class Solution:
    """
    思路：
        1.使用最小堆模拟优先队列
        2.每次往[(1, 0), (-1, 0), (0, 1), (0, -1)]四个方向进行移动
        3.把有效值加入到优先队列，每次pop出grid[i][j]最小的，继续移动
        4.直到row == n-1 and col == n-1
        5.返回上述过程中优先队列经过的最大值
    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = []
        visited = set()

        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited.add((0,0))
        res = 0
        while pq:
            value, row, col = heapq.heappop(pq)
            res = max(value, res)

            if row == n-1 and col == n-1:
                return res 

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + x, col + y 

                if (new_row, new_col) not in visited and 0 <= new_row < n and 0 <= new_col < n:
                    visited.add((new_row, new_col))
                    heapq.heappush(pq, (grid[new_row][new_col], new_row, new_col))
                    
        return -1 

# grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# so = Solution()
# print(so.swimInWater(grid))


# 二分法
from typing import List 
class Solution:
    """
    思路：
        1. dfs/bfs 进行判断当grid[nx][ny] <= mid 时能不能到达终点
        2. 二分法left = max(grid[0][0], grid[-1][-1]), right = n * n - 1
        3. 不断缩小范围直到left <= right
    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(x, y, t):
            if x == n-1 and y == n-1:
                return True 
            
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = r + x # 用nx来替换x进行四个方向的尝试
                ny = c + y
                if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= t:
                    visited.add((nx, ny))
                    if dfs(nx, ny, t):
                        return True
            return False
        
        left = max(grid[0][0], grid[-1][-1])
        right = n * n - 1  # grid[i][j] 位于区间 [0, ..., N*N - 1] 内。
        while left <= right:
            mid = (left + right) // 2
            visited = set((0, 0))
            if dfs(0, 0, mid):
                right = mid - 1   # True时候，mid - 1 否则当right==mid时候无法跳出循环
            else:
                left = mid + 1
        return left
    
# 并查集解法
from typing import List
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        # if x_root != y_root:
        #     self.parent[x_root] = y_root
        # 如果两个元素属于不同的集合，则合并它们
        if x_root != y_root:
            # 按秩合并，将小树合并到大树上
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                # 如果 rank 相同，随便合并，并增加新树的 rank
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        n = len(grid)

        # 因为需要从小到大考虑时刻 t，从平台高度 t 出发判断是否能与相邻的方块连通
        # 所以这里需要存储每个平台高度对应的位置
        idx = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                idx[grid[i][j]] = (i, j)
        
        # print(idx)
        uf = UnionFind(n * n)
        for t in range(n * n):
            # 对高度为 t 的平台进行判断是否能与相邻四个方位的平台连通
            x, y = idx[t]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= t:
                    # 尝试合并相邻的平台, 因为点是按照n*n铺开的，（x,y）用x * n + y代表 
                    uf.union(x * n + y, nx * n + ny)
                    
            
            # 检查左下角与右下角是否连通，
            # 若能连通，此时的 t 即是答案
            if uf.connected(0, n * n - 1):
                return t
        
        
        return -1

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
so = Solution()
print(so.swimInWater(grid))