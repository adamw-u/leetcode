#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# Tags
# array

# Companies
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

# 示例 1:

# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:

# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
 

# 提示：

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
 

# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）


# @lc code=start
from typing import List
class Solution:
    """
    思路:
        1. 需要O(n)且不能使用除法
        2. nums = [2, 3, 4, 5]
            2.1 其前缀乘p=[1, 2, 6, 24], 除p[0]=1,其他位置p[i] = nums[i-1] * p[i-1]
            2.2 其后缀乘l=[60, 20, 5, 1],除p[-1]=1,其他位置逆序遍历，p[i] = nums[i+1] * p[i-1]
        3. 最终结果，p[i]*l[i]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p, l, res = [0] * n, [0] * n, [0] * n

        p[0] = 1
        for i in range(1, n):
            p[i] = nums[i-1] * p[i-1]
        
        l[-1] = 1
        for i in range(n-2, -1, -1):
            l[i] = nums[i+1] * l[i+1]

        for i in range(n):
            res[i] = p[i] * l[i]
        
        return res 

        
# @lc code=end

