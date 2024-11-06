# https://leetcode-cn.com/problems/shortest-distance-to-a-character
# 前置知识
# 数组的遍历(正向遍历和反向遍历)
# 题目描述
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

# 示例 1:

# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 说明:

# - 字符串 S 的长度范围为 [1, 10000]。
# - C 是一个单字符，且保证是字符串 S 里的字符。
# - S 和 C 中的所有字母均为小写字母。

def get_distance(S, C):
    """
    思路：
        1.设初始的最短距离为一个大的值
        2.从左到右遍历一遍，当遇到C时候，更新初始距离idx为abs(i-idx)
        3.从右到左遍历一遍，取min(ans[i], idx-i)
    """
    n = len(S)
    ans = [0]*n

    idx = 2*n
    for i, j in enumerate(S):
        if j == C:
            idx = i
        ans[i] = abs(i - idx)
    
    idx = 2*n 
    for i in range(n-1, -1, -1): # 最大取n-1
        if S[i] == C:
            idx = i
        ans[i] = min(ans[i], idx-i)
    return ans

S = 'loveleetcode'
C = 'e'
get_distance(S, C)

from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0]*n

        idx = 2*n
        for i, j in enumerate(s):
            if j == c:
                idx = i
            ans[i] = abs(i - idx)
        
        idx = 2*n 
        for i in range(n-1, -1, -1): # 最大取n-1
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx-i)
        return ans