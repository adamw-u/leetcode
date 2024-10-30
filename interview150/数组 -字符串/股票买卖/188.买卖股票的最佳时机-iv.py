#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

# 示例 1：

# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2：

# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 

# @lc code=start
from typing import List
class Solution:
    """
    思路:
        1. dp[i][k][j] 作为递推方程表示,其中i代表股票在不同天的价格,k代表最大交易次数,j代表股票持有状态
        2. 其中 第k次交易可获得的利润依赖与第k-1次交易利润，所以k需要倒序遍历
    """
    def maxProfit(self, k:int, prices: List[int]) -> int:
        n = len(prices)
        
        k = min(k, n//2)
        dp = [[[0, -prices[0]] for _ in range(k + 1)] for _ in range(n)]  # 长度是交易次数
        ## 这里注意点,直接扩展成最多k次交易，k<=n//2，如果k>=n//2也最多能完成n//2次买卖

        for i in range(1, n):
            for j in range(k, 0, -1):   # 代表第i次交易，只要买入交易次数+1，卖出不+1
                dp[i][j][1] =  max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])  # 有
                dp[i][j][0] =  max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])  # 没有
        # print(dp)
        return dp[-1][k][0]
        
# @lc code=end

