#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

# 示例 1：

# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：

# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

# @lc code=start
from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = max(prices), 0  # 初始化最大价格
        for i in prices:
            profit = max(profit, i - cost)  # 最小价格与当前价格的差值，找最大利润
            cost = min(i, cost) # 不断需按照最小价格
        return profit
    # & (按位与)：对二进制数的每一位执行与操作。即当两个数字的对应位都为 1 时，结果的该位才为 1，否则为 0。 j&1 == 1代表j是奇数
    def maxProfit(self, prices: List[int]) -> int:
        """
        思路：
            1. 动态规划思路，每天可以有三种选择，无动作/买入/卖出
            2. 如何表示只有一次买入卖出？ 
            3. 初始利润为[0, -p0]
                dp[i][0] = min(dp[i-1][0], -pi) # 买入无利润，卖出才能有利润，所以取最小
                dp[i][1] = max(dp[i-1][1], pi + dp[i-1][0]) # 上一步卖出利润最大，或则本次卖出利润最大 
        """
        n = len(prices)
        dp = [[-prices[0], 0] for _ in range(n)] 
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])  # 上一次买入利润dp[i-1][0]，本次买入利润-prices[i]，因为只能买一次
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        # print(dp)
        return dp[-1][1]
        
# @lc code=end

