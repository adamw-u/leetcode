# 入选理由
# 暂无

# 题目地址
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words

# 前置知识
# 哈希表
# 双指针
# 题目描述
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

# 示例 1：
# 输入：
# s = "barfoothefoobarman",
# words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2：

# 输入：
# s = "wordgoodgoodgoodbestword",
# words = ["word","good","best","word"]
# 输出：[]
from collections import Counter
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        wordLen = len(words[0])
        wordsLen = len(words)
        r = wordLen * wordsLen
        hash_set = []
        ct = Counter(words)
        for i in range(len(s) - r + 1):
            for j in range(i, i + r, wordLen):
                hash_set.append(s[j:j+wordLen])
            if Counter(hash_set) == ct:
                res.append(i)
            hash_set.clear()
        return res
