#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# Tags
# hash-table | two-pointers | string | sliding-window

# Companies
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# @lc code=start
class Solution:
    """
    思路:
        1. 设置一个set集合,记录保证set中元素不重复
        2. 双指针思路,设置l,r两个指针,当s[r]的元素已经存在于set中则不断右移l直到s[r]不存在于set中
        3. 在指针移动过程中以ans = max(ans, r -l)作为字串最大长度
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l, r = 0, 0 
        n = len(s)

        ans = 0 
        while r < n:
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            r += 1
            ans = max(ans, r - l )
        return ans 

# @lc code=end

