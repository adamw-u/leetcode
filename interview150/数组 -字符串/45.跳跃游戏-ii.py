#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# Tags
# array | greedy

# Companies
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

# 0 <= j <= nums[i] 
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

 

# 示例 1:

# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:

# 输入: nums = [2,3,0,1,4]
# 输出: 2

# @lc code=start
from typing import List 
class Solution:
    """
    思路:
        1. 暴力解法，从左到右先找到最小能到达的下标，更新index，步数+1
        2. 如何保证最小： 正序遍历，当有第一个满足条件时候，循环break记录下下标即可
        3. 直到最小小标为0
        4. 时间复杂度高
    """
    def jump(self, nums: List[int]) -> int:
        index = len(nums) - 1
        step = 0 
        while index > 0:
            for i, j in enumerate(nums[: index + 1]):
                if  i + j >= index:
                    index = i 
                    step += 1
                    break
        return step

    """
    思路2
    """
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_right = 0  # 已建造的桥的右端点
        next_right = 0  # 下一座桥的右端点的最大值
        for i in range(len(nums) - 1): 
            # 为什么是-1？当 i=n−2 时，如果 i=curRight 成立，我们会造桥，这样可以抵达 n−1。
            # 否则 i<curRight，我们也可以到达 n−1。所以无论是何种情况，都只需要遍历到 n−2。
            next_right = max(next_right, i + nums[i])
            if i==cur_right:
                cur_right = next_right
                ans += 1
        return ans 
    
# @lc code=end

