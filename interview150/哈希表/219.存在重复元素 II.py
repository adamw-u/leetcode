#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#

# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

 

# 示例 1：

# 输入：nums = [1,2,3,1], k = 3
# 输出：true
# 示例 2：

# 输入：nums = [1,0,1,1], k = 1
# 输出：true
# 示例 3：

# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hash_nums = {}
        # for i, j in enumerate(nums):
        #     if j not in hash_nums:
        #         hash_nums[j] = [i]
        #     else:
        #         hash_nums[j].append(i)

        # index_v = [v for v in hash_nums.values()]
        # for index in index_v:
        #     if len(index)>=2:
        #         for i in range(1, len(index)):
        #             if abs(index[i] - index[i-1]) <= k: 
        #                 return True 
        # return False

        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

