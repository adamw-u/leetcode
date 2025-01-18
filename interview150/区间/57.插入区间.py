#
# @lc app=leetcode.cn id=57 lang=python3
# @lcpr version=30204
#
# [57] 插入区间
#
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。

# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

# 返回插入之后的 intervals。

# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。

 

# 示例 1：

# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：

# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        思路：
            1. 设定左右指针分别为newInterval左区间和右区间
            2. 分三种情况考虑：
                2.1 当前值的左区间值大于right,则ans.append(newInterval)并进行列表相加并返回结果
                2.2 当前值的右区间值小于于left,ans直接添加当前值
                2.3 在以上两种情况之外,则需要更新left、right值及newInterval
            3. 注意：如果对2.3单独考虑需要处理很多边界条件,所以直接放到else里面会更容易处理
        """
        left,right = newInterval
        ans = []

        for idx,(i,j) in enumerate(intervals):
            if right<i:
                ans.append(newInterval)
                return ans+intervals[idx::]
            elif j<left:
                ans.append([i,j])
            else:
                left = min(left,i)
                right = max(right,j)
                newInterval = [left,right]
        ans.append(newInterval)
        return ans

# @lc code=end



#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#

