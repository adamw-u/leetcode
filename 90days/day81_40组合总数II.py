# 题目地址
# https://leetcode-cn.com/problems/combination-sum-ii/

# 前置知识
# 剪枝
# 数组
# 回溯
# 题目描述
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：

# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# [1, 7],
# [1, 2, 5],
# [2, 6],
# [1, 1, 6]
# ]
# 示例 2:

# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, path):
            if sum(path) == target:
                res.append(path[:])
                return res 
            elif sum(path) > target:
                return 
            for i,j in enumerate(candidates):
                # 避免重复
                if i>0 and candidates[i]==candidates[i-1]:
                    continue 
                path.append(j)
                dfs(candidates[i+1:], path)
                path.pop()
             

        res = []
        # 排序避免重复
        dfs(sorted(candidates), [])
        return res 
    
candidates = [2,5,2,1,2]
target = 5
so = Solution()
print(so.combinationSum2(candidates, target))