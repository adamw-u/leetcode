# @lcpr-before-debug-begin
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#
# 给你一个满足下述两条属性的 m x n 整数矩阵：

# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

# 示例 1：


# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 示例 2：


# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        思路：
            1. 有序的矩阵所以考虑二分法
            2. m代表矩阵行 n代表列
            3. 假设left = 0, right = m*n-1,  mid = (left+right)//2
            则mid所在矩阵的位置为matrix[mid//n][mid%n]
            4. 根据所在位置的值收缩范围
        """
        m = len(matrix)
        n = len(matrix[0])
        left = 0 
        right = m * n -1
        while left <= right: # 当left==right时候如果matrix[mid//n][mid%n] == target 返回True，否则就是不存在
            mid = (left + right)//2
            if matrix[mid//n][mid%n] > target:
                right = mid - 1
            elif matrix[mid//n][mid%n] < target:
                left = mid + 1
            else:
                return True
        return False
        
# @lc code=end

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t = 3
so = Solution()
print(so.searchMatrix(matrix, t))

#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

