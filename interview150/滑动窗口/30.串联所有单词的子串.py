#
# @lc app=leetcode.cn id=30 lang=python3
# @lcpr version=30204
#
# [30] 串联所有单词的子串
#

# Tags
# 哈希表 | 字符串 | 滑动窗口

# Companies
# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。

 

# 示例 1：

# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
# 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
# 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
# 输出顺序无关紧要。返回 [9,0] 也是可以的。
# 示例 2：

# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
# s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
# 所以我们返回一个空数组。
# 示例 3：

# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
# 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
# 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
# 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
# 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List 
from collections import Counter
class Solution:
    """
    思路：
        1. 首先明确题目要求:words中单词长度一致,我们以Counter记录及其频次
        2. 在s中以 words.length*words[i].length 大的窗口进行滑动,如果滑动窗口内Counter==words的Counter则返回结果
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ctWords = Counter(words)
        wordsLen = len(words[0])
        slidLen = len(words) * wordsLen

        res = []
        for i in range(len(s) - slidLen + 1): # 必须+1 代表要取到末尾
            swords = [s[i:i+wordsLen] for i in range(i, i+slidLen, wordsLen)]
            if Counter(swords) == ctWords:
                res.append(i)
        return res 
        
# @lc code=end



#
# @lcpr case=start
# "barfoothefoobarman"\n["foo","bar"]\n
# @lcpr case=end

# @lcpr case=start
# "wordgoodgoodgoodbestword"\n["word","good","best","word"]\n
# @lcpr case=end

# @lcpr case=start
# "barfoofoobarthefoobarman"\n["bar","foo","the"]\n
# @lcpr case=end

#

