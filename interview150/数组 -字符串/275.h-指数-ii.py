#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# Tags
# binary-search

# Companies
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。

# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少 有 h 篇论文分别被引用了至少 h 次。

# 请你设计并实现对数时间复杂度的算法解决此问题。

 

# 示例 1：

# 输入：citations = [0,1,3,5,6]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
#      由于研究者有3篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
# 示例 2：

# 输入：citations = [1,2,100]
# 输出：2
 

# 提示：

# n == citations.length
# 1 <= n <= 105
# 0 <= citations[i] <= 1000
# citations 按 升序排列

# @lc code=start
from typing import List 
class Solution:
    """
    思路:
        1. 有序的问题->二分查找
        2. 每次判断mid位置citations[mid] >= n - mid
            2.1 如果满足条件right移动
            2.2 否则left移动
            2.3 最后返回n - left
    """
    def hIndex(self, citations: List[int]) -> int:
        left = 0 
        right = len(citations)-1
        n = len(citations)
        while left <= right :
            mid = (left + right)//2
            if citations[mid] >= n - mid:  # 这里不能用right - mid
                right = mid -1 
            else:
                left = mid + 1
        return n - left 
        
# @lc code=end

