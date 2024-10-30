#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# Tags
# greedy

# Companies
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

# 你需要按照以下要求，给这些孩子分发糖果：

# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

 

# 示例 1：

# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 示例 2：

# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。

# @lc code=start
from typing import List
class Solution:
    """
    思路：  与238题思路相似
        1. https://leetcode.cn/problems/candy/solutions/17847/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/?source=vscode
        2. 左规则： 当 ratingsB>ratingsA时,B 的糖比 A 的糖数量多。右规则： 当 ratingsA>ratingsB时,A 的糖比 B 的糖数量多。
        3. 先从左至右遍历学生成绩 ratings,按照以下规则给糖，并记录在 left 中：
            3.1 先给所有学生 1 颗糖；
            3.2 若 ratings i>ratings i-1,则第 i 名学生糖比第 i-1 名学生多 1 个。
            3.2 若 ratings i<=ratings i-1,则第 i 名学生糖数量不变。（交由从右向左遍历时处理。）
            经过此规则分配后，可以保证所有学生糖数量 满足左规则 。
        4. 同理，在此规则下从右至左遍历学生成绩并记录在 right 中，可以保证所有学生糖数量 满足右规则 。
        5. 最终，取以上 2 轮遍历 left 和 right 对应学生糖果数的 最大值 ，这样则 同时满足左规则和右规则 ，即得到每个同学的最少糖果数量。
    """
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        left, right = [1] * n , [1] * n 
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        
        res = sum([max(right[i], left[i]) for i in range(n)])
        return res 
        
# @lc code=end
