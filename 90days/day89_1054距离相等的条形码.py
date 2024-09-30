# 题目地址
# https://leetcode-cn.com/problems/distant-barcodes/

# 前置知识
# 堆
# 贪心
# 题目描述
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

# 请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

 

# 示例 1：

# 输入：[1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
# 示例 2：

# 输入：[1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
 

# 提示：

# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
from typing import List
from collections import Counter
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        我们首先想到的思路就是，找到剩余数量最多的元素，尽可能优先排列它。

        然后我们每次从堆顶拿出一个剩余最多的元素，放入排列中，再更新剩余数量，重新放入最大堆中。
        如果这个元素和排列结果中的最后一个元素相同，那么我们就需要再从最大堆中取出第二多的元素，放入排列中，之后再把这两个元素放回最大堆中。
        """
        count = Counter(barcodes)
        q = []
        for x, cx in count.items():
            # 建堆
            heapq.heappush(q, (-cx, x))
        res = []
        while len(q) > 0:
            cx, x = heapq.heappop(q)
            if len(res) == 0 or res[-1] != x:
                res.append(x)
                if cx < -1:
                    heapq.heappush(q, (cx + 1, x))
            else:
                cy, y = heapq.heappop(q) # 最大堆中取出第二多的元素
                res.append(y)
                if cy < -1: # 绝对值大于1 ，代表元素还没排列完成
                    heapq.heappush(q, (cy + 1, y)) # 更新cx放入堆
                heapq.heappush(q, (cx, x))
        return res
