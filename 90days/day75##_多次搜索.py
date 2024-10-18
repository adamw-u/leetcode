# 题目地址
# https://leetcode-cn.com/problems/multi-search-lcci

# 前置知识
# 字符串匹配
# Trie
# 题目描述
# 给定一个较长字符串 big 和一个包含较短字符串的数组 smalls，设计一个方法，根据 smalls 中的每一个较短字符串，对 big 进行搜索。输出 smalls 中的字符串在 big 里出现的所有位置 positions，其中 positions[i]为 smalls[i]出现的所有位置。

# 示例：

# 输入：
# big = "mississippi"
# smalls = ["is","ppi","hi","sis","i","ssippi"]
# 输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
# 提示：

# 0 <= len(big) <= 1000
# 0 <= len(smalls[i]) <= 1000
# smalls 的总字符数不会超过 100000。
# 你可以认为 smalls 中没有重复字符串。
# 所有出现的字符均为英文小写字母。
import collections
from typing import List

class Trie:

    def __init__(self):
        # 初始化字典树
        self.alpha_dict = {}
        # 字符串结束标记
        self.end_of_string = -1

    def insert(self, word: str) -> None:
        # self.alpha_dict用来保存根节点内容，否则输出node是空{}
        node = self.alpha_dict  # node用于实现迭代嵌套
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w] # 字典嵌套
        node[self.end_of_string] = word  # end是以 word结尾

    def search(self, word: str):
        res = []
        node = self.alpha_dict
        for w in word:
            if w not in node:
                break 
            node = node[w]
            # 做一点改造，用来记录结束位置
            if self.end_of_string in node:
                res.append(node[self.end_of_string])
        return res
    

    def startsWith(self, prefix: str):
        res = []
        node = self.alpha_dict
        for w in prefix:
            if w not in node:
                return False 
            node = node[w]
        return True

class Solution:
    """
    思路：
        1. smalls加入到搜索树
        2. 遍历big进行搜索，如果能搜到small则记录下对应index
        3. 返回每次可以搜到对应index的列表
    """
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie()
        for s in smalls:
            trie.insert(s)
        print("trie",trie.alpha_dict)
        hit = collections.defaultdict(list)

        for i in range(len(big)):
            matchs = trie.search(big[i:])
            # hit
            for word in matchs:
                hit[word].append(i)
        print(hit)
        res = []
        for word in smalls:
            res.append(hit[word])
        return res

big = "mississippi"
# trie {'i': {'s': {-1: 'is'}, -1: 'i'}, 'p': {'p': {'i': {-1: 'ppi'}}}, 'h': {'i': {-1: 'hi'}}, 
#        's': {'i': {'s': {-1: 'sis'}}, 's': {'i': {'p': {'p': {'i': {-1: 'ssippi'}}}}}}}
smalls = ["is","ppi","hi","sis","i","ssippi"]
solution = Solution()
print(solution.multiSearch(big, smalls))