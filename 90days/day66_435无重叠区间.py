# 题目地址
# https://leetcode-cn.com/problems/non-overlapping-intervals/

# 前置知识
# 暂无

# 题目描述
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

# 注意:

# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 示例 1:

# 输入: [ [1,2], [2,3], [3,4], [1,3] ]

# 输出: 1

# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:

# 输入: [ [1,2], [1,2], [1,2] ]

# 输出: 2

# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:

# 输入: [ [1,2], [2,3] ]

# 输出: 0

# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        count = 0
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                count += 1
            else:
                end = intervals[i][1] # i之前的元素因满足end > intervals[i][0]，默认被移除了，所以end更新为intervals[i][1]
        return count

so = Solution()
intervals = [ [1,2], [2,3], [3,4], [1,3] ]
print(so.eraseOverlapIntervals(intervals))
