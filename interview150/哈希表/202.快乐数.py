#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30204
#
# [202] 快乐数
#
# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」 定义为：

# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

 

# 示例 1：

# 输入：n = 19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 示例 2：

# 输入：n = 2
# 输出：false

# 1 <= n <= 2^31 - 1

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        思路: 
            1. 保留求解超时。
            2. 维护一个列表，将每次n变化后的值放入列表
            3. 放入之前进行一个判断：
                3.1 如果已经存在，说明这有一个环导致无法变成1
                3.2 如果不存在就进行往下进行
        """
        n_list = []
        while n <= 2**31 -1:
            num = [int(i)**2 for i in str(n)]
            n = sum(num)
            if n == 1:
                return True
            if n in n_list:
                return False
            n_list.append(n)
        return False
        
# @lc code=end



#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

