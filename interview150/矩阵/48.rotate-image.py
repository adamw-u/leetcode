#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30204
#
# [48] 旋转图像
#

# Tags
# 数组 | 数学 | 矩阵

# Companies
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

 

# 示例 1：


# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
# 示例 2：


# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 首先考虑整行旋转则原来列变成行即newRow=oldCol,newCol=maxRow-oldRow(第二行变倒数第二列),原地旋转需要空间复杂度O(1)
        2. 第一次旋转假设先对矩阵四个角操作:
            2.1 A B C D分别代表矩阵的左上 右上 右下 左下四个角 
            2.2 旋转后 A->B->C->D ---> A 
            2.3 但是首次旋转后 B 的值会被A 覆盖导致 上述过程BCD都变成了A的值,所以需要先使用tmp来存储A
            2.4 先把A用D替换掉,这样只需要一个中间变量tmp,具体过程：
                tmp=matrix[i][j]
                matrix[i][j]←matrix[n-1-j][i]←matrix[n-1-i][n-1-j]←matrix[j][n-1-i]←tmp

        3. 由于一次旋转就会完成四个,所以整体转化次数 为行 n//2 列 n//2 (当列为奇数时(n+1)//2)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                # newRow=oldCol, newCol = maxRow - oldRow
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n -1 -j][i]  # 对应上面旋转准则 newRow = i 所以oldCol=i, newCol = j 所以oldCol = n -1 -j
                matrix[n -1 -j][i] = matrix[n - 1 -i][n - 1 -j] # 同理 
                matrix[n - 1 -i][n - 1 -j] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = tmp
        return matrix
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

