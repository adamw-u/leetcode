# 题目地址
# https://leetcode-cn.com/problems/n-queens-ii/

# 前置知识
# 回溯
# 深度优先遍历
# 题目描述
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。


# 示例 1：


# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：

# 输入：n = 1
# 输出：1
 

# 提示：

# 1 <= n <= 9
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

def totalNQueens(n):
    """
    思路：
        1. 按行回溯遍历  backtrack(r)
        2. 除行外，还需要判断列，对角线：
            2.1. 列进行for循环遍历
            2.2. 主对角线判断条件：row1 - col1 == row2 - col2, 所以在集合里面添加一个r-i即可
            2.3. 副对角线判断条件：row1 + col1 == row2 + col2
        3. 终止条件：r==n代表有一个解
    """
    col = set()
    dia1 = set()
    dia2 = set() 

    
    def backtrack(r):
        if r == n :
            nonlocal res 
            res += 1
            return res
        for c in range(n):
            if c not in col and r - c not in dia1 and r + c not in dia2:
                col.add(c)
                dia1.add(r - c)
                dia2.add(r + c)
                backtrack(r + 1)
                col.remove(c)
                dia1.remove(r - c)
                dia2.remove(r + c)
            else:
                continue 
    res = 0 
    backtrack(0)
    return  res 

print(totalNQueens(6))
