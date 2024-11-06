# 题目地址
# https://leetcode-cn.com/problems/knight-probability-in-chessboard/

# 前置知识
# 动态规划
# 数组
# 题目描述
# 已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 

# 现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 

# 如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。


# 现在 “马” 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。

# 求移动结束后，“马” 仍留在棋盘上的概率。\

# 输入: n = 3, k = 2, row = 0, column = 0
# 输出: 0.0625
# 解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
# 在每一个位置上，也有两种移动可以让骑士留在棋盘上。
# 骑士留在棋盘上的总概率是0.0625。


# 动态规划
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    dp = [[0 for i in range(n)] for _ in range(n)]
    dp[row][column] = 1 # 初始概率为1

    for kk in range(k):
        cur = [[0 for i in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                for x, y in [(1, -2), (-1, 2), (-1, -2), (1, 2), (2, 1), (-2, -1), (-2, 1), (2, -1)]:
                    nx, ny = r + x, c+ y 
                    if 0 <= nx < n and 0 <= ny < n:
                        cur[nx][ny] += dp[r][c]/8  
        dp = cur 
    print(dp)
    return sum(map(sum, dp))  # map(sum, dp) 按行累加 再次sum才是总的概率值


## dfs 复杂度高，需要加记忆
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    
    def dfs(n, step, r, col, mem):
        if r >= n or r < 0 or col < 0 or col >= n:
            return 0 
        
        if step == 0:
            return 1  
        
        if (r,col,step)  in mem:
            return mem[(r,col,step)]
        
        prob = 0 
        for i, j in directions:
            prob += dfs(n, step - 1, r + i, col + j, mem) / 8
        mem[(i,j,step)] = prob
        return prob 

    directions = [(1, -2), (-1, 2), (-1, -2), (1, 2), (2, 1), (-2, -1), (-2, 1), (2, -1)]
    mem = {}
    prob = dfs(n, k, row, column, mem)

    return prob 


print(knightProbability(3, 2, 0, 0))