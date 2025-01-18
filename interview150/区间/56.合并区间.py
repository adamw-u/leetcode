#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

# 示例 1：

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：

# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        思路:
            1. 先对intervals按照首个数字大小进行排序
            2. 依次判断, i+1值的左区间值 < i值的右区间值 则合并 同时更新右侧区间的大小
            3. 如果不满足上述条件则之间加入到new_intervals，直至结束
        """
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)
        i = 0 
        new_intervals = []
        while i < n:
            l = intervals[i][0]
            r = intervals[i][1]
            while i < n-1 and intervals[i+1][0] <= r:
                r = max(intervals[i+1][1], r)
                i += 1 

            new_intervals.append([l, r])
            i += 1
        return new_intervals
            

# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#

