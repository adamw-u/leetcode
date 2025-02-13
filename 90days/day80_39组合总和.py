# 题目地址
# https://leetcode-cn.com/problems/combination-sum/

# 前置知识
# 剪枝
# 回溯
# 题目描述
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1：

# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
# [7],
# [2,2,3]
# ]
# 示例 2：

# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]


# 提示：

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, path):
            if sum(path) == target:
                res.append(path[:])
                return res 
            elif sum(path)>target:# path和大于target时，剪枝
                return 
            for i, j in enumerate(candidates):
                path.append(j)
                dfs(candidates[i:], path)
                path.pop()

        res = []
        dfs(candidates, path = [])
        return res 
    
candidates = [2,3,6,7] #[2, 3, 5]# [2,3,6,7]
target = 8#7
so = Solution()
print(so.combinationSum(candidates, target))
