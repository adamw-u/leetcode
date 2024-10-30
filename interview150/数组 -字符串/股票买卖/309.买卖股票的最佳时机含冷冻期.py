#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#


# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

# 示例 1:

# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 示例 2:

# 输入: prices = [1]
# 输出: 0
 

# 提示：

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1.相比122题，新增了冷冻期，即卖出后第二天才能再买入
        2.因为买卖次数无限制，所以省略第二个维度(交易次数k)，用dp[i][j]来表示
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, -prices[0]] for _ in range(n)]
        for i in range(1, n):
            if i <= 2:  # i-2边界处理
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                # 当 i = 1 时，dp[i-2] 不合法，所以只能从 dp[i-1][1] 转移过来
                dp[i][1] = max(dp[i-1][1], -prices[i])

            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]) # dp[i-2][0] - prices[0] 代表前两天卖出后今天才能卖出

        return dp[-1][0]
        
# @lc code=end

