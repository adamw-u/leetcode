#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#

# Tags
# 数组 | 矩阵 | 模拟

# Companies
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

# 示例 1：


# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：


# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import  List
class Solution:
    """
    思路：
        1. 空值处理： 当 matrix 为空时，直接返回空列表 [] 即可。
        2. 初始化： 矩阵 左、右、上、下 四个边界 l , r , t , d ，用于打印的结果列表 res 。
        3. 循环打印： “从左向右、从上向下、从右向左、从下向上” 四个方向循环打印。
            3.1 根据边界打印，即将元素按顺序添加至列表 res 尾部。
            3.2 边界向内收缩 1 （代表已被打印）。
            3.3 判断边界是否相遇（是否打印完毕），若打印完毕则跳出。
        4. 返回值： 返回 res 即可。
            打印方向	1. 根据边界打印	2. 边界向内收缩	3. 是否打印完毕
            从左向右	左边界l ,右边界 r	上边界 t 加 1	是否 t > d
            从上向下	上边界 t ,下边界d	右边界 r 减 1	是否 l > r
            从右向左	右边界 r ,左边界l	下边界 d 减 1	是否 t > d
            从下向上	下边界 d ,上边界t	左边界 l 加 1	是否 l > r

    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, d = 0, n-1, 0, m-1
        res = []
        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > d : break

            for i in range(t, d+1):
                res.append(matrix[i][r])
            r -= 1
            if l > r : break

            for i in range(r, l-1, -1):
                res.append(matrix[d][i])
            d -= 1
            if t > d : break

            for i in range(d, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r : break
        
        return res 

        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

