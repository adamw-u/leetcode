# 题目地址
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

# 前置知识
# 动态规划
# 题目描述
# 给定一个未排序的整数数组，找到最长递增子序列的个数。

# 示例 1:

# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:

# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

def LongestIncreasingSubsequence(nums):
    n = len(nums)
    dp = [1] * n
    count = [1] * n 
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]: 
                if dp[j] + 1 > dp[i]:  # dp[i] 取max ，每次从index0开始算
                    dp[i] = dp[j] + 1 
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:  # 相等的个数 代表了相同长度序列的个数
                    count[i] += count[j] 
    
    max_length = max(dp)
    res = 0
    for i, j in enumerate(dp):
        if j == max_length:
            res += count[i]
    print(dp, count)
    return res
nums = [100,90,80,70,60,50,60,70,80,90,100]
print(LongestIncreasingSubsequence(nums))
