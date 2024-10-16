# 题目地址
# https://leetcode-cn.com/problems/coin-change-2/

# 前置知识
# 暂无

# 题目描述
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

# 示例 1:

# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2:

# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 示例 3:

# 输入: amount = 10, coins = [10]
# 输出: 1
 

# 注意:

# 你可以假设：

# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
from typing import List
def change(amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # dp[i][0] = 1，因为凑出金额 0 不需要使用任何硬币，只有一种方式

    for i, x in enumerate(coins):
        for j in range(amount + 1):
            if j >= x:
                # 用前i种硬币组成j的组合个数，加上新增i+1种硬币，组成j的组合个数
                dp[i + 1][j] = dp[i][j] + dp[i + 1][j - x]
            else:
                dp[i + 1][j] = dp[i][j] 
    print(dp)
    return dp[n][amount]

# 状态转移方程
# 如果不选择第 i 种硬币，凑 j 元的方式等于前 i-1 种硬币凑 j 元的方式：dp[i][j] = dp[i-1][j]。
# 如果选择第 i 种硬币，凑 j 元的方式等于前 i 种硬币凑 j - coins[i-1] 元的方式：dp[i][j] += dp[i][j - coins[i-1]]。
# 递推方程为： dp[i][j]=dp[i−1][j]+dp[i][j−coins[i−1]]

dp = [[1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 0]]

amount = 5 # 2
coins = [1, 2, 5]
print(change(amount, coins))