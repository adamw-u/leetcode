# 题目地址
# https://leetcode-cn.com/problems/subsets/

# 前置知识
# 位运算
# 回溯
# 题目描述
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：

# 输入：nums = [0]
# 输出：[[],[0]]
 

# 提示：

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同

from typing import List
class Solution(object):
    """
    思路：
        1. 初始化空列表path
        2. n==数组长度时候，终止递归
        3. 用一个index变量记录每次递归使用到数组哪个index
    """
    def subsets(self,  nums: List[int]) -> List[List[int]]:

        def dfs(nums, n, path = []): 
            res.append(path[:])
            if n == len(nums):
                return res 
            for i in range(n, len(nums)): 
                path.append(nums[i])
                dfs(nums, i+1, path)
                path.pop()
            return res 

        res = []
        # 递归变量为index
        return dfs(nums, 0,  path=[])

nums = [1,2]
so = Solution()
print(so.subsets(nums))