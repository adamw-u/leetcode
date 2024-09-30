# 题目地址
# https://leetcode-cn.com/problems/coin-change/

# 前置知识
# 暂无

# 题目描述
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回  -1。

# 你可以认为每种硬币的数量是无限的。

# 示例 1：

# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：

# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：

# 输入：coins = [1], amount = 0
# 输出：0
# 示例 4：

# 输入：coins = [1], amount = 1
# 输出：1
# 示例 5：

# 输入：coins = [1], amount = 2
# 输出：2
 

# 提示：

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    n = len(coins)
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

    dp[0][0] = 0
    for i, x in enumerate(coins):
        for j in range(amount + 1):
            if j >= x:
                dp[i+1][j] = min(dp[i][j], dp[i+1][j - x] + 1) # dp[i+1][j - x] + 1 代表完全背包问题中元素可以被多次选择
            else:
                dp[i+1][j] = dp[i][j]
    return dp[n][amount] if dp[n][amount] != float('inf') else -1 

"""
以1 元和 3 元，目标是凑出总金额为 5 元
dp[1][c]=min(dp[1][c],dp[1][c-1]+1)
for cc in range(c):
    dp[1][1] = 1, dp[1][2] = 2, dp[1][3] = 3, dp[1][4] = 4, dp[1][5] = 5

但如果是 dp[1][c]=min(dp[1][c],dp[0][c-1]+1)
for cc in range(c):
    dp[1][1] = 1, dp[1][2] = min(dp[1][2],dp[0][1]+1) = inf, dp[1][3] = inf, dp[1][4] = inf, dp[1][5] = inf

所以 dp[1][c]=min(dp[1][c],dp[1][c-1]+1), 是代表硬币可以重复使用的完全背包问题
"""

coins = [2]
amount = 3

print(coinChange(coins, amount) )