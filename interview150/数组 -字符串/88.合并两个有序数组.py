#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# Tags
# Companies
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

 

# 示例 1：

# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

# 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？


# @lc code=start
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        双指针，逆序插入
        """
        l1, l2 = m - 1 , n - 1
        right = m + n -1 
        while l1 >= 0 or l2 >= 0:
            if l1 == -1:  # l1达到末尾后只需要插入l2即可
                nums1[right] = nums2[l2]
                l2 -= 1
            elif l2 == -1:
                nums1[right] = nums1[l1]
                l1 -= 1
            elif nums1[l1] <= nums2[l2]: 
                nums1[right] = nums2[l2]
                l2 -= 1
            else:
                nums1[right] = nums1[l1]
                l1 -= 1 
            right -= 1  # 末尾指针不断左移


# @lc code=end

