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
    """
    初始化两个状态转移方程一个是序列中的最长递增子序列长度，一个是最长递增子序列的个数
    """
    n = len(nums)
    dp = [1] * n
    count = [1] * n 
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]: 
                if dp[j] + 1 > dp[i]:  # 对j属于0-i的索引，进行遍历：更新dp[i]的值，因为nums[i] > nums[j]，所以dp[i]应取max dp[j] + 1，对应代码就是这里
                    dp[i] = dp[j] + 1 
                    count[i] = count[j]  # 因为出现了最大值，所以count不更新
                elif dp[j] + 1 == dp[i]: # 代表 (0, l)且l<i直接出现了一次与当前dp[j]相同长度的值
                    # 最长递增子序列个数进行累加
                    count[i] += count[j]  # 固定i，累计所有j<i中dp[j] + 1 == dp[i]的count[j]的个数
    
    max_length = max(dp)
    res = 0
    for i, j in enumerate(dp):
        if j == max_length:
            res += count[i]
    print(dp, count)
    return res
# nums = [90,100,80,90,60,50,60,70,80,90,100]
nums = [90,100,80,90,60,50, 60, 55, 52 ,80]
print(LongestIncreasingSubsequence(nums))
