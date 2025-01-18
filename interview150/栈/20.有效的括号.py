#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
 

# 示例 1：

# 输入：s = "()"

# 输出：true

# 示例 2：

# 输入：s = "()[]{}"

# 输出：true

# 示例 3：

# 输入：s = "(]"

# 输出：false

# 示例 4：

# 输入：s = "([])"

# 输出：true

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        validPair = ['()','{}','[]']
        s_stack = []
        for i in s:
            if i not in s_dict:
                s_stack.append(i)
            else:
                if len(s_stack)>=1 and s_stack.pop()+i in validPair:
                    continue
                else:
                    return False
        return not s_stack
       
        
# @lc code=end

so = Solution()
s = '()'
so.isValid(s)

#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

