#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
# 返回 k 。
# 判题标准:

# 系统会用下面的代码来测试你的题解:

# int[] nums = [...]; // 输入数组
# int[] expectedNums = [...]; // 长度正确的期望答案

# int k = removeDuplicates(nums); // 调用

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# 如果所有断言都通过，那么您的题解将被 通过。

 

# 示例 1：

# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 示例 2：

# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        n = len(nums)
        while l < n - 1:
            if nums[l] == nums[l+1]:
                nums.pop(l)  # list.pop(i) 时间复杂度为O（n），所以不建议用
                n -= 1
            else:        # 要加else条件
                l += 1
        return  l + 1
    
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            ## 将快指针 fast 依次遍历从 1 到 n−1 的每个位置，对于每个位置，如果 nums[fast]！=nums[fast−1]  /  nums[slow-1]
            # 说明 nums[fast] 和之前的元素都不同，因此将 nums[fast] 的值复制到 nums[slow]，然后将 slow 的值加 1，即指向下一个位置。

            # 遍历结束之后，从 nums[0] 到 nums[slow−1] 的每个元素都不相同且包含原数组中的每个不同的元素，因此新的长度即为 slow，返回 slow 即可。
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow


# @lc code=end

