# 题目地址
# https://leetcode-cn.com/problems/can-i-win/

# 前置知识
# 暂无

# 题目描述
# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。
# 如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
# 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
# 给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
# 你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

# 示例：
# 输入：
# maxChoosableInteger = 10
# desiredTotal = 11

# 输出：
# false

# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        特判：
            1.如果最大能选择的数字maxChoosableInteger比期望的总数desiredTotal要大，先手稳赢，返回True
            2.如果能选择的所有数字总和比期望的总数desiredTotal要小，一定到达不了desiredTotal，先手稳输，返回False
        """
        seen = {}
        def dfs(remain, choices):
            if sum(choices) < remain:
                return False
            if choices[- 1] >= remain:
                return True
            if choices in seen:
                return seen[choices]
            
            for i, e in enumerate(choices):
                if not dfs(remain - e, choices[:i] + choices[i + 1:]):   # 排除其中一个元素后True，代表对手赢
                    seen[choices] = True                                 # 排除其中一个元素后False，代表对手输，对手输所以seen[choices] = True   
                    return True
            seen[choices] = False  # 遍历choices都没有赢，所以seen[choices] = False
            print(seen)
            return False
        
        return dfs(desiredTotal, tuple([i + 1 for i in range(maxChoosableInteger)]))

so = Solution()
print(so.canIWin(4, 8))
# {(3, 4): False, (2, 3, 4): True, (1, 3, 4): True, (1, 2, 4): False}
# (1, 2, 4): False，所以seen[(1,2,3,4)] = True ，返回True结束遍历