#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#

# Tags
# 哈希表 | 字符串 | 滑动窗口

# Companies
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。


# 注意：

# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

# 示例 1：

# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 示例 2：

# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 示例 3:

# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
class Solution:
    """
    思路1:
        1. 滑动窗口 + Counter比较
        2. 双指针newLeft,r=0,len(s):
            2.1 右移r直到s[l:r]包含t, 比较并判断是否更新指针
            2.2 在左移newLeft直到s[newLeft:r]不包含t
            2.3 这个过程用ans记录最小长度的s
        3. 这里设置一个哨兵节点left=-1,如果left没有更新过则输出结果为空
    """
    def compareCounter(self, c1, c2):
        """如果c1包含c2返回True"""
        for i, j in c2.items():
            if i not in c1  or  c1[i] < j:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        cs = Counter()

        newLeft = 0
        # 绝了
        left = -1 # -1 代表左指针没有移动过，即t在s中找不到返回""
        right = len(s)

        for i, j in enumerate(s):
           cs[j] += 1
           while self.compareCounter(cs, ct):
            # 当ct中所有字符都存在于cs中，缩小newRight ，newLeft范围
              if right -  left >= i - newLeft:
                 left, right = newLeft, i  # 因为我们保证它是唯一的答案。所以可以不断缩小范围

              cs[s[newLeft]] -= 1
              newLeft += 1     

        return "" if left <0 else s[left:right+1]
        
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

