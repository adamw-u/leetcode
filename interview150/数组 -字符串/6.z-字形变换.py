#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#


# Tags
# string

# Companies
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);
 

# 示例 1：

# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 示例 3：

# 输入：s = "A", numRows = 1
# 输出："A"

# @lc code=start
class Solution:
    """
    思路：
        1. 借助一个flag字段,让字符c先按flag增加当falg达到最大numRows时,反向变化直到0
        2. 按照上述方法即可得到s中每个字符c对应的行号
        3. 同时借助res = ["" for _ in range(numRows)],记录每一行对应的字符串，最后拼接
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c # 将对应行的字符串记录在一起
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        print(res)
        return "".join(res)

# s = "PAYPALISHIRING"
# numRows = 3
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
# res = ['PAHN', 'APLSIIG', 'YIR']
# @lc code=end

