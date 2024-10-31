#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# Tags
# string

# Companies
# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

# 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。

# 注意:

# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
 

# 示例 1:

# 输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 示例 2:

# 输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。       
#      第二行同样为左对齐，这是因为这行只包含一个单词。
# 示例 3:

# 输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

# @lc code=start
from typing import List 

def blank(n: int) -> str:
    return ' ' * n # 空格个数

class Solution:
    """
    思路：
    根据题干描述的贪心算法，对于每一行，我们首先确定最多可以放置多少单词，这样可以得到该行的空格个数，从而确定该行单词之间的空格个数。
    根据题目中填充空格的细节，我们分以下三种情况讨论：
        1. 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格；
        2. 当前行不是最后一行，且只有一个单词：该单词左对齐，在行末填充空格；
        3. 当前行不是最后一行，且不只一个单词：设当前行单词数为 numWords，空格数为 numSpaces，我们需要将空格均匀分配在单词之间，则单词之间应至少有
            avgSpaces=numSpaces//(numWords-1)个空格，对于多出来的
            extraSpaces=numSpacesmod(numWords-1)个空格，应填在前 extraSpaces 个单词之间。
            因此，前 extraSpaces 个单词之间填充 avgSpaces+1 个空格，其余单词之间填充 avgSpaces 个空格。
    """
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        right, n = 0, len(words)
        while True:
            left = right  # 当前行的第一个单词在 words 的位置
            sumLen = 0  # 统计这一行单词长度之和
            # 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格(right - left表示)
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1

            # 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen

            # 当前行只有一个单词：该单词左对齐，在行末填充空格
            if numWords == 1:
                ans.append(words[left] + blank(numSpaces))
                continue

            # 当前行不只一个单词
            avgSpaces = numSpaces // (numWords - 1)
            extraSpaces = numSpaces % (numWords - 1)
            s1 = blank(avgSpaces + 1).join(words[left:left + extraSpaces + 1])  # 拼接额外加一个空格的单词
            s2 = blank(avgSpaces).join(words[left + extraSpaces + 1:right])  # 拼接其余单词
            ans.append(s1 + blank(avgSpaces) + s2)

        return ans
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        对照思路重写版本：
            1. 贪心的为每一行分最多的单词，分完之后进行判定：
            2. 如果是最后一行则空格右填充
            3. 如果不是最后一行，且当前行只有一个单词，则空格右填充
            4. 如果不是最后一行，且当前行有多个单词，则根据题目规则进行空格填充(右侧空格多于左侧空空数)
        """
        ans = []
        n = len(words)
        right = 0 
        while right < n:
            left = right 
            sumLen = 0  # 只统计了单词长度
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1
            
            if right == n: # 最后一行
                s = " ".join(words[left:right])
                ans.append(s + blank(maxWidth - len(s)))
                break
            
            if right - left == 1:  # 只有一个单词
                ans.append(words[left] + blank(maxWidth - sumLen))  # 这个地方不能用words[left:right]这样返回的是一个长度为1的列表
                                                                    # 应该是words[left]或者words[left:right][0]
                continue
            
            avgSpaces = (maxWidth - sumLen)//(right - left -1) 
            extraSpaces = (maxWidth - sumLen)%(right - left -1)
            s1 = blank(avgSpaces + 1).join(words[left:left + extraSpaces + 1])
            s2 = blank(avgSpaces).join(words[left + extraSpaces + 1 : right])
            ans.append(s1 + blank(avgSpaces) + s2)
        return ans 

# @lc code=end

