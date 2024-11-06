# 入选理由
# 暂无

# 题目地址
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# 前置知识
# 哈希表
# 双指针
# 题目描述
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

def lengthOfLongestSubstring(s):
    """
    子串必须是连续的
    双指针法求解
    """
    hash_set = []
    ans = 0 
    l = r = 0
    while r < len(s):
        if s[r] not in hash_set:
            hash_set.append(s[r])
            r += 1 
        else:
            while s[r] in hash_set:
                hash_set.pop(0)
                l += 1 
        ans = max(ans, r- l)
    return ans 
