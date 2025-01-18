#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30204
#
# [290] 单词规律
#
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。

 

# 示例1:

# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 示例 2:

# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 示例 3:

# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        思路：
            1. hash表存储首字母模式pattern对应的s
            2. 当遇到存在于hash中的pattern时判断对应的s是否与hash[pattern]一致
            3. 同理还要判断 s2pattern 
        """
        hash_pattern = {}
        hash_s = {}
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        for i, j in zip(pattern, s):
            if i in hash_pattern and hash_pattern[i] != j or \
                j in hash_s and hash_s[j] != i:
                return False
            hash_pattern[i] = j
            hash_s[j] = i
        return True
        
# @lc code=end
# pattern = "abba"
# s = "dog cat cat dog"
# so = Solution()
# print(so.wordPattern(pattern, s))

#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end

#

