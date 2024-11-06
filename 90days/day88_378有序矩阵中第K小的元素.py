# 题目地址
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

# 前置知识
# 二分查找
# 堆
# 题目描述
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

# 示例：

# matrix = [
#  [ 1,  5,  9],
#  [10, 11, 13],
#  [12, 13, 15]
# ],
# k = 8,

# 返回 13。
 

# 提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

from typing import List 
import heapq
class Solution(object):
    """
    思路:https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/solutions/311472/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/?source=vscode
        1. 参考官方题解，值应该是在一个锯齿形状
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # 利用最小堆k进行操作
        # i,0分别代表行列的index值
        heap = [(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(heap) 

        # 把前k-1小的值都pop出，返回第k小
        for i in range(k-1):
            # 第一个列是0
            # 第二个列要对比 matrix[1][0] 和 matrix[0][1] 大小，pop最小值
            # 不断进行对比，所以列/行逐步增加，直到pop到k-1
            matrix_flat,row,col = heapq.heappop(heap)   
            if col != n-1:
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))  # col每次加1
        return heapq.heappop(heap)[0] # pop(第k小的值)
    
    # 二分法
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n  = len(matrix)
        def get_mid_cnt(mid):
            r, c = n - 1, 0 
            cnt = 0
            while r > 0 and c <= n-1:
                if matrix[r][c] <= mid:
                    # 从矩阵的左下角开始统计小于等于mid数量
                    cnt += r + 1 
                    c += 1
                else:
                    r -= 1
            return cnt 
        
        l, r = matrix[0][0] , matrix[n -1][n - 1] 
        while l < r:
            mid = (l + r)//2
            if get_mid_cnt(mid) >= k:
                r = mid 
            # elif get_mid_cnt(mid) == k:
            #     return mid 
            else:
                l = mid + 1
        return l 

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
so = Solution()
print(so.kthSmallest(matrix, k))
