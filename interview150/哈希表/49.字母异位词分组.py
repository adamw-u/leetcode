#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

 

# 示例 1:

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:

# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:

# 输入: strs = ["a"]
# 输出: [["a"]]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        思路:
            1. 对每个s进行字母排序
            2. 构建hash表，观察排序后s是否存在于hash表中，如果存在则对应列表添加元素，不存在则新构造一个list
            3. 最后返回dict[str:List[str]]中的value值
        """
        res = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i not in res:
                res[sorted_i]=[i]
            else:
                res[sorted_i].append(i)
        return [v for v in res.values()]
        
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

