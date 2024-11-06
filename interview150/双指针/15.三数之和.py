#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# Tags
# array | two-pointers

# Companies
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

# 你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。


# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：

# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
 

# 提示：

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# @lc code=start
from typing import List
class Solution:
    """
    思路:
        1. 先将nums数组由小到大排序
        2. 遍历排序数组，设target = -nums[i]， 转化成两数和问题
        3. 双指针遍历，如果存在 nums[l] + nums[r] = -nums[i]， 则三数和为0
        4. 注意: 需要避免重复
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # 跳过重复元素
                continue
            target = - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 跳过重复元素
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res 
        
# @lc code=end

