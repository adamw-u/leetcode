# 题目地址
# https://leetcode-cn.com/problems/number-of-boomerangs/

# 前置知识
# 哈希表
# 两点间距离计算方法
# 排列组合基础知识
# 题目描述
# 给定平面上  n 对不同的点，“回旋镖” 是由点表示的元组  (i, j, k) ，其中  i  和  j  之间的距离和  i  和  k  之间的距离相等（需要考虑元组的顺序）。

# 找到所有回旋镖的数量。你可以假设  n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

# 示例:


# 输入:
# [[0,0],[1,0],[2,0]]

# 输出:
# 2

# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
from collections import defaultdict
from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        def distance(x, y):
            return (x[0] - y[0])**2 + (x[1]-y[1])**2
        
        res = 0 
        for i in range(len(points)):
            # 固定一个点，选另外两个与他的距离一样(i, j, k) 
            hash_map = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dist = distance(points[i], points[j])
                    hash_map[dist] += 1  # 统计距离相等的点的个数
            for val in hash_map.values(): # m个里面选两个的排列组合 m*(m-1)
                res += val * (val - 1)
        return res 
