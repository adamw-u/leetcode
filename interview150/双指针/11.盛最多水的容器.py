#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# Tags
# array | two-pointers

# Companies
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。

# 说明：你不能倾斜容器。

# 示例 1：

# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例 2：

# 输入：height = [1,1]
# 输出：1

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 设置双指针 l, r
        2. 面积是由 (r-l)*min(h[l], h[r])得到， 短板决定面积
        3. 双指针移动策略：
            往面积变大的方向移动
            移动短板
    """
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1

        res = (r - l) * min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * (r - l)) # 向右移动短板，面积变大/变小
                l += 1                              # 因为如果这时候，向左移动长板，短板可能会变小x轴一定变小，所以面积一定变小
            else:
                res = max(res, height[r] * (r - l)) # 移动短板 r
                r -= 1

        return res 

# @lc code=end

