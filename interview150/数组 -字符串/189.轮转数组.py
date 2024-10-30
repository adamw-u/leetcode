#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

# 示例 1:

# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:

# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
 

# 提示：

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# 进阶：

# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？


# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 分三步旋转，以[1,2,3,4,5,6,7]为例
        2. 整个旋转[7,6,5,4,3,2,1]
        3. 前k个元素旋转[5,6,7,4,3,2,1]
        4. k到n-1个元素旋转[5,6,7,1,2,3,4]
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等于轮转 k%n 次
        reverse(0, n - 1)  
        reverse(0, k - 1)
        reverse(k, n - 1)



# @lc code=end

