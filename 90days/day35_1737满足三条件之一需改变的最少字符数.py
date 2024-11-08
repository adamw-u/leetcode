# 题目地址
# https://leetcode-cn.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/
# 前置知识
# 	•	计数
# 	•	枚举
# 题目描述
# 给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。

# 操作的最终目标是满足下列三个条件 之一 ：

# a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
# b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
# a 和 b 都 由 同一个 字母组成。
# 返回达成目标所需的 最少 操作数。

#  

# 示例 1：

# 输入：a = "aba", b = "caa"
# 输出：2
# 解释：满足每个条件的最佳方案分别是：
# 1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
# 2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
# 3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
# 最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
# 示例 2：

# 输入：a = "dabadd", b = "cda"
# 输出：3
# 解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。
#  

# 提示：

# 1 <= a.length, b.length <= 105
# a 和 b 只由小写字母组成


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        """
        ans1:a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
        ans2:b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
        ans3:a 和 b 都 由 同一个 字母组成。

        核心思路：遍历以i为基准， 每次都变成a中的字母都比i小，b中的字母都比i大，遍历完成取最小值
        """
        count_a, count_b = [0] * 26, [0] * 26
        len_a, len_b = len(a), len(b)
        for ca in a:
            count_a[ord(ca) - ord('a')] += 1
        for cb in b:
            count_b[ord(cb) - ord('a')] += 1

        count_total = [ca + cb for ca, cb in zip(count_a, count_b)]
        ans3 = len_a + len_b - max(count_total)   ## 第3种情况的答案：统计a b中出现次数最多的字母（假设为c），把剩余字母替换成c即可
        ans1 = ans2 = len_a + len_b  ## 最多替换次数 len_a + len_b
        for i in range(1, 26): #第0个是a无法在变小了 
            ans1 = min(ans1, sum(count_a[i:]) + sum(count_b[:i]))  # a中字母严格小于b中字母
            # 依次次迭代，当字母a时，需要把stra中所有非a替换为a，把strb中a替换成非a即可完成
            ans2 = min(ans2, sum(count_a[:i]) + sum(count_b[i:]))  # b中字母严格小于a中字母
        return min(ans1, ans2, ans3)


s = Solution()
print(s.minCharacters("aba", "caa"))
print(s.minCharacters("dabadd", "cda"))
print(s.minCharacters("acac", "bd"))
print(s.minCharacters("a", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
