#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# Tags
# two-pointers | string

# Companies
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

# 字母和数字都属于字母数字字符。

# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

 

# 示例 1：

# 输入: s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。
# 示例 2：

# 输入：s = "race a car"
# 输出：false
# 解释："raceacar" 不是回文串。
# 示例 3：

# 输入：s = " "
# 输出：true
# 解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
# 由于空字符串正着反着读都一样，所以是回文串。

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum()]) # isalnum() 方法检测字符串是否由字母和数字组成。
        if len(s)==0:
            return True
        l, r = 0, len(s)-1
        # print(s, l, r)
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True  # 不能用l==r判断，例子："aa"， 最后l=1, r=0

        
# @lc code=end

