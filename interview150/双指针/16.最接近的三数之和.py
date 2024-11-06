#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# Tags
# array | two-pointers

# Companies
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

# 返回这三个数的和。

# 假定每组输入只存在恰好一个解。

 

# 示例 1：

# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：

# 输入：nums = [0,0,0], target = 1
# 输出：0

# @lc code=start
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_res = float('inf')
        sum_res = None
        for i in range(len(nums)):
            left , right = i+1, len(nums)-1
            while left < right:
                # diff = abs(target - (nums[i] + nums[left] + nums[right]))
                sum_res = nums[i] + nums[left] + nums[right]
                sum_diff = sum_res - target
                if sum_res == target:
                    return sum_res
                elif sum_res > target:
                    right -= 1
                else:
                    left += 1

                if abs(sum_diff) < min_res:
                    min_res = abs(sum_diff)
                    new_res = sum_res
                    # print(new_res)
        return new_res
# @lc code=end

