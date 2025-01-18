#
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30204
#
# [205] 同构字符串
#
# 给定两个字符串 s 和 t ，判断它们是否是同构的。

# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

# 示例 1:

# 输入：s = "egg", t = "add"
# 输出：true
# 示例 2：

# 输入：s = "foo", t = "bar"
# 输出：false
# 示例 3：

# 输入：s = "paper", t = "title"
# 输出：true

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        思路：
            1. 对于已有映射 i -> s2t[i]，若和当前字符映射 i -> j 不匹配，
                说明有一对多的映射关系，则返回 false 
            2. 对于映射 j -> i 也同理
        """
        s2t, t2s = {}, {}
        for i, j in zip(s, t):
            if i in s2t and s2t[i] != j or \
            j  in t2s and t2s[j] != i:
                return False
            s2t[i], t2s[j] = j, i
        return True
# @lc code=end



#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "foo"\n"bar"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#

