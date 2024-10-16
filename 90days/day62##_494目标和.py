# 题目地址
# https://leetcode-cn.com/problems/target-sum/

# 前置知识
# 背包
# 数学
# 题目描述
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，target。现在你有两个符号  +  和  -。对于数组中的任意一个整数，你都可以从  +  或  -中选择一个符号添加在前面。

# 返回可以使最终数组和为目标数 target 的所有添加符号的方法数。

# 示例：

# 输入：nums: [1, 1, 1, 1, 1], target: 3
# 输出：5
# 解释：

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 一共有5种方法让最终目标和为3。
from typing import List
def findTargetSumWays(nums: List[int], target: int):
    """
    思路：
        1.首先排除target > sum(nums) 和 (sum(nums) - target) % 2 != 0 情况，(sum(nums) - target)剩余数值必须得通过+  或  -组合成0，即偶数
        2.s = (sum(nums) - target) //2作为背包容量
        参考：https://leetcode.cn/problems/target-sum/solutions/2119041/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-s1cx/?source=vscode
    """
    if target > sum(nums) or (sum(nums) - target) % 2 != 0: 
        return 0 
    n = len(nums)
    s = (sum(nums) - target) //2

    dp = [[0] * (s+1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i, x in enumerate(nums):
        for j in range(s + 1):
            if j >= x:
                dp[i+1][j] = dp[i][j] + dp[i][j - x]
            else:
                dp[i+1][j] = dp[i][j]

    return dp[n][s]


from typing import List
def findTargetSumWays(nums: List[int], target: int):
    if target > sum(nums) or (sum(nums) - target) % 2 != 0:
        return 0 
    
    n = len(nums)
    count = 0 
    def dfs(nums, target, index, sums):
        nonlocal count
        if index == n:
            if sums == target:
                count += 1
            return  
        dfs(nums, target, index + 1, sums + nums[index])
        dfs(nums, target, index + 1, sums - nums[index])
    dfs(nums, target, 0, 0)
    return count

from collections import defaultdict
def findTargetSumWays(nums: List[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    
    for num in nums:
        newdp = defaultdict(int)
        for key in dp:
            newdp[key+num] += dp[key]
            newdp[key-num] += dp[key]
        dp = newdp
    return dp[target]
    # {0:1} -> {1:1, -1:1} -> {2: 1, 0: 2, -2: 1}) -> 

nums = [1, 1, 1, 1, 1]
target = 3
print(findTargetSumWays(nums, target))