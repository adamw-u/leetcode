# 题目地址
# https://leetcode-cn.com/problems/partition-equal-subset-sum/

# 前置知识
# 暂无

# 题目描述
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# 注意:

# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 示例 1:

# 输入: [1, 5, 11, 5]

# 输出: true

# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

# 示例 2:

# 输入: [1, 2, 3, 5]

# 输出: false

# 解释: 数组不能分割成两个元素和相等的子集.



def canPartition(nums):
    """
    背包容量 s/2
    状态方程：f[i][j] = f[i-1][j - nums[i-1]] or f[i-1][j]
    """
    sums = sum(nums)
    if sums % 2 != 0:
        return False 
    s = int(sums/2)
    n = len(nums)

    dp = [[False for i in range(s + 1)] for _ in range(n+1)]
    dp[0][0] = True
    for i, x in enumerate(nums):
        for j in range(1, s + 1):
            if j >= x:
                dp[i + 1][j] = dp[i][j - nums[i]] or dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    
    return dp[n][s]


nums = [1, 11, 5, 5]
print(canPartition(nums))