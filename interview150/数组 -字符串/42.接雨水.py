#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# Tags
# array | two-pointers | stack

# Companies
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

# 示例 1：



# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 示例 2：

# 输入：height = [4,2,0,3,2,5]
# 输出：9

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 首先明确每个柱子所在位置能接到的雨水是由其:左边柱子最大高度和右边柱子最大高度,与自身高度差决定的
        2. 左边柱子最大高度 l_max = max(l_max, h[i])
        3. 右边柱子最大高度 r_max = max(r_max, h[i])
        4. 时空复杂度都是0(n)
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max, r_max = [0] * n, [0] * n 

        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i-1], height[i])
        
        r_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])
        
        res = 0 
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        
        return res 
    """
    思路：
        1. 双指针法，降低空间复杂度0(n)->0(1)
        2. 用双指针来移动来表示每个指针当下对应的l_max, r_max
        3. 理解难点，当处于left时候l_max 代表[0-left]最大点,r_max代表[r, n]的最大点，跟上面思路有不同，没有覆盖整个区间
            3.1 我们只要找到min(l_max， r_max) - h[i]即可
            3.2 考虑双指针的移动顺序，当l_max < r_max时候我们用l_max- h[i]求得面积，移动左指针
            3.3 当l_max > r_max时候我们用r_max- h[i]求得面积，移动右指针    
    """
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0

        res = 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            # res += min(l_max, r_max) - height[i]
            if l_max < r_max:
                res += l_max - height[left]
                left += 1  # 左指针移动
            else:
                res += r_max - height[right]
                right -= 1
        return res
        
# @lc code=end

