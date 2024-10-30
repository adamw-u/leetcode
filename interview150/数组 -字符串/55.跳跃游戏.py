#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# Tags
# array | greedy

# Companies
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

 

# 示例 1：

# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：

# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1.设置初始间隔inter=1, index = n-2 即最后一个下标的前一个值
        2.贪心的去判断倒数第二个值是否能到达最后，不能inter+=1，可以则更新index
        3.直到最后判断index==0? 
    """
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1 

        inter = 1 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= inter:
                target  = i 
                inter = 1
            else:
                inter += 1
        return target == 0
    """
    思路2:
        1.维护一个可以最远跳到的位置mx
        2.如果i > mx代表中间有断层，则无法抵达最后一个位置
        3.当mx>= len(nums) - 1代表可以到达
    """
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i, jump in enumerate(nums):
            if i > mx:  # 无法到达 i
                return False
            mx = max(mx, i + jump)  # 从 i 最右可以跳到 i + jump
            if mx >= len(nums) - 1:  # 可以跳到 n-1
                return True


   
# @lc code=end

