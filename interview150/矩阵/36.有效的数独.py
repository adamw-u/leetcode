#
# @lc app=leetcode.cn id=36 lang=python3
# @lcpr version=30204
#
# [36] 有效的数独
#

# Tags
# 数组 | 哈希表 | 矩阵

# Companies
# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）


# 注意：

# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用 '.' 表示。
 

# 示例 1：


# 输入：board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
# 示例 2：

# 输入：board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false
# 解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import Counter
class Solution:
    """
    思路：
        1. 暴力解法
        2. 对行、列、3*3分别建立一个hash表,判断hash表是否合法
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidHash(hashTable):
            for i in hashTable:
                if i != '.' and hashTable[i] > 1:
                    return False
            return True
        
        # 把矩阵展开乘9*9个索引
        board81 = []
        for i in range(9):
            for j in range(9):
                board81.append(board[i][j])
        
        # 对行进行判断
        for i in range(9):
            ct = Counter(board[i])
            if not isValidHash(ct):
                return False
        
        # 对列进行判断
        for i in range(9): # 外层固定列
            board_column = [board81[i + j*9] for j in range(9)]
            if not isValidHash(Counter(board_column)):
                return False
        
        # 对 3*3 进行判断
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                board33 = []
                for ii in range(i, i+3):
                     for jj in range(j, j+3):
                         board33.append(board81[ii + jj * 9])
                if not isValidHash(Counter(board33)):
                    return False
        
        return True
    
    """
    思路：
        1. 优化 空间复杂度及 box的取值方法
        2. 对行、列、3*3分别建立一个hash表,判断hash表是否合法
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 记录每行、每列和每个 3x3 宫中出现的数字
        row_dict = [{} for _ in range(9)]
        col_dict = [{} for _ in range(9)]
        box_dict = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    box_index = (i // 3) * 3 + j // 3 # 把3X3宫内分成
                    """
                    0 3 6
                    1 4 7
                    2 5 8
                    """
                    
                    # 检查当前数字是否已经出现过
                    if num in row_dict[i] or num in col_dict[j] or num in box_dict[box_index]:
                        return False
                    else:
                        row_dict[i][num] = 1
                        col_dict[j][num] = 1
                        box_dict[box_index][num] = 1
                        
        return True


        
# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

