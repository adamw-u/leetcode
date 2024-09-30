# 题目地址
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

# 前置知识
# 堆
# 排序
# 题目描述

# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:

# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

import heapq , random # 默认实现最小堆 
def findKthLargest(nums, k):
    n = len(nums)
    if n < k:
        return -1 
    heap = []
    for i,j in enumerate(nums):
        if i < k:
            heapq.heappush(heap, j)
        if i>=k and j > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, j)
        print(heap)
    return heap[0]

def findKthLargest(nums, k):
    # 递归快排
    n = len(nums)
    if n == 0:
        return 
    rnd = 0 #random.randint(0, n-1)
    # print(rnd)
    mid = [i for i in nums if i == nums[rnd]]
    left = [i for i in nums if i < nums[rnd]]
    right = [i for i in nums if i > nums[rnd]]
    if len(right) >= k:
        return findKthLargest(right, k)
    elif len(right) + len(mid) >= k :
        return nums[rnd]
    else:
        k = k - len(right) - len(mid)
        return findKthLargest(left, k)
    

nums = [3,2,1,5,6,4] #[3,2,3,1,2,4,5,5,6]
k = 2
print('res', findKthLargest(nums, k))