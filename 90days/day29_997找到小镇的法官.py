# 题目地址
# https://leetcode-cn.com/problems/find-the-town-judge/

# 前置知识
# 图
# 题目描述
# 在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。

# 如果小镇的法官真的存在，那么：

# 小镇的法官不相信任何人。
# 每个人（除了小镇法官外）都信任小镇的法官。
# 只有一个人同时满足条件 1 和条件 2 。

# 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。

# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。
 

# 示例 1：

# 输入：n = 2, trust = [[1,2]]
# 输出：2


# 示例 2：

# 输入：n = 3, trust = [[1,3],[2,3]]
# 输出：3


# 示例 3：

# 输入：n = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1


# 示例 4：

# 输入：n = 3, trust = [[1,2],[2,3]]
# 输出：-1


# 示例 5：

# 输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3

 

# 提示：

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# trust[i] 互不相同
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= n
from typing import List
class Solution:
    """
    思路：
        1.构造图的入度出度值，如果某个节点的入度为n-1，出度为0，则返回节点值
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graphIN = {i: [] for i in range(1, n + 1)}
        for a, b in trust:
            graphIN[b].append(a)

        graphOut = {i: [] for i in range(1, n + 1)}
        for a, b in trust:
            graphOut[a].append(b)
        
        for i in graphIN:
            if len(graphIN[i]) == n-1 and len(graphOut[i])==0:
                return i
        return -1 