#
# @lc app=leetcode.cn id=228 lang=python3
# @lcpr version=30204
#
# [228] 汇总区间
#
# 给定一个  无重复元素 的 有序 整数数组 nums 。

# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

# 列表中的每个区间范围 [a,b] 应该按如下格式输出：

# "a->b" ，如果 a != b
# "a" ，如果 a == b

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        思路： 
            1. 设计边界条件处理 最好通过while循环解决
            注：虽然代码写的是一个二重循环，但 i += 1 这句话至多执行 n 次，所以总的时间复杂度仍然是 O(n) 的。
        """
        res = []
        i = 0 
        while i < len(nums):
            start = i 
            while i < len(nums) - 1 and nums[i + 1] - nums[i] == 1:
                i += 1
            strs = str(nums[start])
            if start != i:
                strs += '->' + str(nums[i])
            res.append(strs)
            i += 1
        return res 
        
# @lc code=end



#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#

