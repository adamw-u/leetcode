# 题目地址
# https://leetcode-cn.com/problems/beautiful-array/

# 前置知识
# 分治
# 题目描述
# 对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

# 对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

# 那么数组 A 是漂亮数组。

 

# 给定 N，返回任意漂亮数组 A（保证存在一个）。

 

# 示例 1：

# 输入：4
# 输出：[2,1,4,3]


# 示例 2：

# 输入：5
# 输出：[3,1,2,5,4]

 

# 提示：

# 1 <= N <= 1000

# 有点难懂
class Solution:
    def beautifulArray(self, N):
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                odds = f((N+1)/2)
                evens = f(N/2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)
    
