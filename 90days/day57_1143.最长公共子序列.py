# 题目地址
# https://leetcode-cn.com/problems/longest-common-subsequence

# 前置知识
# 数组
# 动态规划
# 题目描述
# 给定两个字符串  text1 和  text2，返回这两个字符串的最长公共子序列的长度。

# 一个字符串的   子序列   是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

# 若这两个字符串没有公共子序列，则返回 0。

# 示例 1:

# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 示例 2:

# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
# 示例 3:

# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。

# 提示:

# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。


def longestCommonSubsequence(text1, text2):
    l1 = len(text1)
    l2 = len(text2)

    dp = [[0] * l2 for _ in range(l1)]# [[0] * l2] * l1 
    dp[0][0] = 1 if text1[0] == text2[0] else 0
    for i in range(1, l1):
        dp[i][0] = min(1, dp[i-1][0] + 1) if text1[i] == text2[0] else dp[i-1][0] 
    for j in range(1, l2):
        dp[0][j] = min(1, dp[0][j-1] + 1) if text1[0] == text2[j] else dp[0][j-1] 

    for i  in range(1, l1):
        for j in range(1, l2):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return dp[-1][-1]

def longestCommonSubsequence(text1, text2):
    m,n = len(text1), len(text2)
    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(1, m+1):
        for j in range (1, n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]

text1 = "aaaa" #'ubmrapg'
text2 = "aaa"
print(longestCommonSubsequence(text1, text2))