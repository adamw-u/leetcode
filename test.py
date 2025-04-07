nums = [5,1,1,2,0,0]
# mid 与 r 交换位置 
# 对比 l,r区间内，所有小于r的值往前走，大于r的往后走
# 如何交换？
# 设置指针 i = l-1
import random 
def quickSort(nums, l, r):
    mid = 1 #random.randint(l, r)
    nums[r], nums[mid] = nums[mid], nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < nums[r]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i, nums

quickSort(nums, 0, 5)

# import numpy as np

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head 
#         pre = dummy 

#         ## 统计链表长度
#         tmp = head
#         n = 0
#         while tmp:
#             n += 1 
#             tmp = tmp.next 
        
#         while n - k >0:
#             n -= k 
#             cur = pre.next 
#             tmp = None 
#             for i in range(k):
#                 nxt = cur.next
#                 cur.next = tmp 
#                 tmp = cur 
#                 cur = nxt 
            
#             # 92 反转链表II的逻辑
#             p0 = pre.next
#             pre.next.next = cur 
#             pre.next = tmp 

#             pre = p0 
#         return dummy.next

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)

# a.next = b 
# b.next = c 
# c.next = d
# d.next = e    

# s = Solution()
# s.reverseKGroup(a, 2)
