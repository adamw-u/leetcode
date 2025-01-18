#
# @lc app=leetcode.cn id=452 lang=python3
# @lcpr version=30204
#
# [452] 用最少数量的箭引爆气球
#

# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。

# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。

# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。

 
# 示例 1：

# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# -在x = 6处射出箭，击破气球[2,8]和[1,6]。
# -在x = 11处发射箭，击破气球[10,16]和[7,12]。
# 示例 2：

# 输入：points = [[1,2],[3,4],[5,6],[7,8]]
# 输出：4
# 解释：每个气球需要射出一支箭，总共需要4支箭。
# 示例 3：

# 输入：points = [[1,2],[2,3],[3,4],[4,5]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# - 在x = 2处发射箭，击破气球[1,2]和[2,3]。
# - 在x = 4处射出箭，击破气球[3,4]和[4,5]。


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        思路：
           1. 把区间按照右端点从小到大排序。
           2. 初始化答案 ans=0，上一个放点的位置 pre=−∞。
           3. 遍历区间，如果 start≤pre，那么这个区间已经包含点，跳过。
           4. 如果 start>pre，那么必须放一个点，把 ans 加一。根据上面的讨论，当前区间的右端点就是放点的位置，更新 pre=end。
           5. 遍历结束后，返回 ans。
        """
        points.sort(key=lambda x: x[1])
        ans = 0 
        pre = -float("inf")
        for i,j in points: 
            if i > pre:
                ans += 1
                pre = j 
            
        return ans 
        
# @lc code=end



#
# @lcpr case=start
# [[10,16],[2,8],[1,6],[7,12]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4],[5,6],[7,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,5]]\n
# @lcpr case=end

#

