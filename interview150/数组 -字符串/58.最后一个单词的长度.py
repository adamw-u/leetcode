#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        s_len = len(s)
        for i in range(s_len-1, -1, -1):
            if len(s[i]) > 0:
                return len(s[i])
        return 0
        
# @lc code=end

