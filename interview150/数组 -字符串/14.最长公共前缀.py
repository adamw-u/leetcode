#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

 

# 示例 1：

# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：

# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 设置初始前缀为strs[0], 依次使用第一个单词与后续每一个单词进行公共前缀匹配直到最后一个单词
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def twoStrCommonPrefix(s1, s2):
            index = 0  
            length = min(len(s1), len(s2))
            while index < length and s1[index]==s2[index]:
                index += 1
            return s1[0:index]
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = twoStrCommonPrefix(prefix, strs[i])
            if not prefix:
                break
        
        return prefix
            
        
# @lc code=end

