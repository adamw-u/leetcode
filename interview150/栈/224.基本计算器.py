#
# @lc app=leetcode.cn id=224 lang=python3
# @lcpr version=30204
#
# [224] 基本计算器
#

# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

 

# 示例 1：

# 输入：s = "1 + 1"
# 输出：2
# 示例 2：

# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：

# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 使用栈模拟计算顺序
        2. 通过sign记录运算符号,除了数字、()、' '之外剩余的就是运算符号：加减乘除
            2.1 +:stack.append(num)
            2.2 -:stack.append(-num)
            2.3 ×:stack[-1] = stack[-1] * num
            3.4 ÷:stack[-1] = int(stack[-1] / float(num))
        3. 如果是数字则:num = 10 * num + int(c)
    """
    def calculate(self, s: str) -> int:
        def helper(s: List) -> int:
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = num * 10 + int(c)
                # 遇到左括号开始递归计算 num
                if c == '(':
                    num = helper(s)

                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # python 除法向 0 取整的写法
                        stack[-1] = int(stack[-1] / float(num))                    
                    num = 0
                    sign = c
                # 遇到右括号返回递归结果
                if c == ')': break
            return sum(stack)

        return helper(list(s))


        
# @lc code=end



#
# @lcpr case=start
# "1 + 1"\n
# @lcpr case=end

# @lcpr case=start
# " 2-1 + 2 "\n
# @lcpr case=end

# @lcpr case=start
# "(1+(4+5+2)-3)+(6+8)"\n
# @lcpr case=end

#

