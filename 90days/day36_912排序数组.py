# 题目地址
# https://leetcode-cn.com/problems/sort-an-array/

# 前置知识
# 数组
# 排序
# 题目描述
# 给你一个整数数组 nums，请你将该数组升序排列。

 

# 示例 1：

# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：

# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
 

# 提示：

# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000

## quick sort 
from typing import List
import random
class Solution:
    # 空间复杂度高
    def sortArray(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len<=1:
            return nums
        mid = random.randint(0, nums_len-1)
        left = [i for i in nums if i < nums[mid]]
        right = [i for i in nums if i > nums[mid]]
        return self.sortArray(left) + [i for i in nums if i==nums[mid]] + self.sortArray(right)
    
## 只能通过17/21案例
from typing import List
import random
class Solution:
    """
    nums = [5,1,1,2,0,0]
    思路：
        1.原地排序：
            1.1 mid 与 r 交换位置 ，固定选取的mid值在最右侧，方便对比
            1.2 对比 l,r区间内，所有小于r的值往前走，大于r的往后走
            1.2 设置指针 i = l-1，统计了小于nums[mid]值的个数
        2.在l < r，范围递归第1步
    """
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1  # 用左指针，来指定小于nums[pivot]的值的位置
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i] # 最后把r值放回到左边都是小于他的地方
        return i

    def randomized_quicksort(self, nums, l, r):
        if l < r:
            mid = self.randomized_partition(nums, l, r)
            self.randomized_quicksort(nums, l, mid - 1)
            self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums
    
