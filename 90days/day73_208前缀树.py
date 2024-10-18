# 题目地址
# https://leetcode-cn.com/problems/implement-trie-prefix-tree

# 前置知识
# 树
# Trie
# 题目描述
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

# 示例:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple"); // 返回 true
# trie.search("app"); // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app"); // 返回 true
# 说明:

# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。

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
        node[self.end_of_string] = True

    def search(self, word: str) -> bool:
        node = self.alpha_dict
        for w in word:
            if w not in node:
                return False 
            node = node[w]
        return self.end_of_string in node 
       

    def startsWith(self, prefix: str) -> bool:
        node = self.alpha_dict
        for w in prefix:
            if w not in node:
                return False 
            node = node[w]
        return True


trie = Trie()
trie.insert('apple')
print(trie.alpha_dict, trie.end_of_string)
# {'a': {'p': {'p': {'l': {'e': {-1: True}}}}}} -1