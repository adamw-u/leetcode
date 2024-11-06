# 题目地址
# https://leetcode-cn.com/problems/unique-binary-search-trees/

# 前置知识
# 二叉搜索树
# 分治
# 题目描述
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

# 示例:

# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

#  1         3     3      2      1
#   \       /     /      / \      \
#    3     2     1      1   3      2
#   /     /       \                 \
#  2     1         2                 3



class Solution(object):
    def numTrees(self, n):
        """
        dp[0] = 1 
        dp[1] = 1
        dp[2] = 2
        dp[3] = dp[1] * dp[1] + dp[0] * dp[2] + dp[2] * dp[0]
        https://leetcode.cn/problems/unique-binary-search-trees/solutions/1153659/96-bu-tong-de-er-cha-sou-suo-shu-python-uuysm/?source=vscode

        比如[1,2,3,4,5,6] 此时需要求出dp[6]
        首先看1和6，其左侧（右侧）无数，为dp[0]，右侧（左侧）为5个连续的数，为dp[5]，则他们各自可以排成的树个数为dp[0] * dp[5]
        2和5，可排成的树个数为dp[1] * dp[4]
        3和4则为dp[2] * dp[3]
        那么dp[6] = sum(
        1:dp[0] * dp[5]
        2:dp[1] * dp[4]
        3:dp[2] * dp[3]
        4:dp[3] * dp[2]
        5:dp[4] * dp[1]
        6:dp[5] * dp[0]
        )
        """
        dp = [0] * (n +1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j]* dp[i - j - 1]
        return dp[n]

