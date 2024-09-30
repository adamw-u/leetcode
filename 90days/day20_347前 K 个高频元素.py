#  题目地址
#  https://leetcode-cn.com/problems/top-k-frequent-elements/

#  前置知识
#  哈希表
#  堆排序
#  快速选择
#  题目描述
#  给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

#  示例 1:

#  输入: nums = [1,1,1,2,2,3], k = 2
#  输出: [1,2]
#  示例 2:

#  输入: nums = [1], k = 1
#  输出: [1]
 

#  提示：

#  1 <= nums.length <= 10^5
#  k 的取值范围是 [1, 数组中不相同的元素的个数]
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_res = {}
        for i, j in enumerate(nums):
            if j not in hash_res:
                hash_res[j] = 1
            else:
                hash_res[j] += 1

        hash_res = sorted(hash_res.items(), key = lambda x: x[1], reverse=True)
        # print(hash_res)
        res_k = hash_res[0:k]
        return [i[0] for i in res_k]
## 这个更快
from collections import Counter
counter = Counter(nums)
counter.most_common(k)