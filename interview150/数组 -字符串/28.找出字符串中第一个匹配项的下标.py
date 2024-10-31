#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# Tags
# two-pointers | string

# Companies
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

 

# 示例 1：

# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 示例 2：

# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

# @lc code=start
class Solution:
    """
    思路：
        1. 字符串匹配，一种暴力O(mn)匹配
        2. 一种是O(M+N)的KMP匹配
    """
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if needle not in haystack or m > n:
            return -1 
        
        if haystack==needle:
            return 0
        
        for i in range(n-m+1):
            if haystack[i:m+i] == needle:
                return i 
        return -1
    
    # KMP解法
    def next(self, needle):
        nxt = []
        nxt.append(0)

        m = len(needle)
        now = 0
        x = 1
        while x < m:
            if needle[now] == needle[x]:
                now += 1
                x += 1
                nxt.append(now)
            elif now:
                now = nxt[now-1]
            else:
                nxt.append(0)
                x += 1
        return nxt 
    
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack or len(needle) > len(haystack):
            return -1 
        
        if haystack==needle:
            return 0

        tar = 0     # 主串匹配的位置
        pos = 0     # 模式串匹配的位置
        
        nxt = self.next(needle)
        while tar < len(haystack):
            if haystack[tar] == needle[pos]:
                tar += 1
                pos += 1
            elif pos: # 失配。如果pos!=0，则依据next数据移动标尺
                pos = nxt[pos - 1]
            else:        # pos[0]失配，直接把标尺向右移动一位
                tar += 1
            
            if pos == len(needle):    # 模式串匹配长度与len(p)一致，匹配成功
                # print(tar - pos) #
                # pos = nxt[pos-1] # 移动标尺
                return tar - pos
        return -1

# @lc code=end

