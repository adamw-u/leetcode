#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# Tags
# array | two-pointers | binary-search

# Companies
# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

# 示例 1：

# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：

# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：

# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
 

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 利用滑动窗口不断缩短窗口大小
        2. 具体过程,设置l,r=0,0
            2.1 r不断右移,直到sum(l,r)>target
            2.2 固定r在右移l,直到sum(l,r)<target
            2.3 重复上述两步,以ans=min(ans, r-l)记录作为最后结果
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0 , 0
        ans = float('inf')

        sumRes = 0 
        while r < len(nums):
            sumRes += nums[r]
            while sumRes >= target:
                sumRes -= nums[l] 
                ans = min(ans, r + 1 -l)  # r 是index，如果要返回长度，需要+1
                l +=1 
            r += 1
        return 0 if ans==float('inf') else ans 
        
# @lc code=end

