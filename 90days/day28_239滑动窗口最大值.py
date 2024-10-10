# 题目地址
# https://leetcode-cn.com/problems/sliding-window-maximum/

# 前置知识
# 队列
# 滑动窗口
# 题目描述
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。

 

# 进阶：

# 你能在线性时间复杂度内解决此题吗？



# 示例:

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:

# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7



# 输入: nums = [1,3,-1,-3,2,3,6,7], 和 k = 3
# 输出: [3,3,2,3,6,7]


# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  2  3  6  7       3
# 1 [3  -1  -3] 2  3  6  7       3
# 1  3 [-1  -3  2] 3  6  7       2
# 1  3  -1 [-3  2  3] 6  7       3
# 1  3  -1  -3 [2  3  6] 7       6
# 1  3  -1  -3  2 [3  6  7]      7

# 提示：

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

from collections import deque
def maxSlidingWindow(nums, k):
    """
    思路：
        1.利用单调递减队列
        2.
    """
    queue = deque()
    for i in range(k):
        while queue and queue[-1] < nums[i]: 
            # 队尾元素小于当前值，删除队尾值，直到队尾元素大于当前值
            queue.pop()
        queue.append(nums[i])
    # [3, -1]
    
    res = [queue[0]]
    for i in range(k, len(nums)):
        # print(queue)
        if queue[0] == nums[i - k]: # 如果队首元素是需要删除的i-k值，则出队列，保证窗口覆盖大小为k
            queue.popleft()    # 队首元素在[queue[0]]已经加入，需要删除
                               # 为什么不直接popleft，因为队首元素不一定是nums[i - k]所以加了这个判断
        while queue and queue[-1] < nums[i]:  # 维护单调队列，保证最大值在队首
            queue.pop()
        queue.append(nums[i])
        res.append(queue[0])
    return res 

