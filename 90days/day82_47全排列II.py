# 题目地址
# https://leetcode-cn.com/problems/permutations-ii/

# 前置知识
# 回溯
# 数组
# 剪枝
# 题目描述
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
# [1,1,2],
# [1,2,1],
# [2,1,1]
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)
        visited = [False] * n 
        def dfs(visited, path):
            if len(path) == n:
                res.append(path[:])
                return res 
            for i, j in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1] and visited[i-1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    path.append(j)
                    dfs(visited, path)
                    path.pop()
                    visited[i] = False # 回溯
 
        
        dfs(visited, [])
        return res 
    
    def permuteUnique(self, nums):
        res = []

        def backtrack(nums, path):
            # nums里面的数全部用完
            if not nums:
                return res.append(path[:])
            
            for i in range(len(nums)):
                #剪枝，相邻两个不想等，其中第1个也就是i==0需要使用
                if i==0 or nums[i] != nums[i-1]: 
                    path.append(nums[i])
                    backtrack(nums[:i]+nums[i+1:], path)
                    path.pop()

        nums.sort()
        backtrack(nums, [])
        return res

nums = [1,1,2]
so = Solution()
print(so.permuteUnique(nums))
