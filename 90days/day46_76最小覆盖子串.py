# 题目地址
# https://leetcode-cn.com/problems/minimum-window-substring

# 前置知识
# Sliding Window
# 哈希表
# 题目描述
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。



# 示例：

# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"


# 提示：

# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
from collections import Counter
class Solution:
   def minWindow(self, s: str, t: str) -> str:
      ct = Counter(t)
      cs = Counter()

      left = 0
      # 绝了
      newLeft = -1 # -1 代表左指针没有移动过，即t在s中找不到返回""
      newRight = len(s)

      for i, j in enumerate(s):
         cs[j] += 1
         while cs >= ct:
            if newRight -  newLeft >= i - left:
               newLeft, newRight = left, i

            cs[s[left]] -= 1
            left += 1

      return "" if newLeft <0 else s[newLeft:newRight+1]


so = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(so.minWindow(S, T))