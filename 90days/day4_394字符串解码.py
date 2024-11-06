# 题目地址
# https://leetcode-cn.com/problems/decode-string/

# 前置知识
# 栈
# 括号匹配
# 题目描述
# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 示例 1：

# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：

# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：

# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：

# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"

class Solution(object):
    """
    思路：
        1.初始化一个空栈
        2.字符串依次入栈，直到遇到]
            2.1 开始出栈，直到遇到[，把[前的元素记录到words中
            2.2 把数字记录到nums中，直到stack为空或者stack[-1]不是数值
            2.3 words*nums
        3.words*nums添加到栈中，继续重复第2步
    """
    def decodeString(self, s):
        stack = []

        for i in list(s):
            if i != ']':
                stack.append(i)
            else:
                w = stack.pop()
                words = ''
                while w != '[':
                    words = w + words
                    w = stack.pop()
                n = stack.pop()
                nums = ''
                while n.isnumeric():
                    nums = n + nums 
                    if stack and stack[-1].isnumeric():
                        n = stack.pop()
                    else:
                        break
                stack.append(words*int(nums))
                print(words, int(nums))
        return ''.join(stack)

s = "2[abc]3[cd]ef"
so = Solution()
so.decodeString(s)   