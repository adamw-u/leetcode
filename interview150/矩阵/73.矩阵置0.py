# @lcpr-before-debug-begin
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

 

# 示例 1：


# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 示例 2：


# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        思路:
            1. 首次遍历取出0所在的行和列
            2. 再次遍历对有0的行和列所有元素置0
        """
        row = len(matrix)
        col = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0

        # row = len(matrix)
        # col = len(matrix[0])
        # row0_flag = False
        # col0_flag = False
        # # 找第一行是否有0
        # for j in range(col):
        #     if matrix[0][j] == 0:
        #         row0_flag = True
        #         break
        # # 第一列是否有0
        # for i in range(row):
        #     if matrix[i][0] == 0:
        #         col0_flag = True
        #         break

        # # 把第一行或者第一列作为 标志位
        # for i in range(1, row):
        #     for j in range(1, col):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = matrix[0][j] = 0
        # #print(matrix)
        # # 置0
        # for i in range(1, row):
        #     for j in range(1, col):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0

        # if row0_flag:
        #     for j in range(col):
        #         matrix[0][j] = 0
        # if col0_flag:
        #     for i in range(row):
        #         matrix[i][0] = 0
        
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# so = Solution()
# print(so.setZeroes(matrix))
# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

