# 题目地址
# https://leetcode-cn.com/problems/merge-k-sorted-lists/

# 前置知识
# 链表
# 归并排序
# 题目描述

# 合并  k  个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6

from typing import List, Optional
class ListNode:
    def __init__(self, val , next = None) -> None:
        self.val = val 
        self.next = next

# def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

def mergeKLists(lists: List[Optional[List]]) -> Optional[list]:
    k = len(lists)
    if k == 0:
        return 
    if k==1:
        return lists[0]
    if k==2:
        return merge2List(lists[0], lists[1])
    
    mid = k//2 
    
    return merge2List(mergeKLists(lists[0:mid]), mergeKLists(lists[mid::]))

def merge2List(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return dummy.next

# def merge2List(l1, l2):
#     ll = []
#     idx1 = 0 
#     idx2 = 0 
#     while idx1 < len(l1) and idx2 < len(l2):
#         if l1[idx1] > l2[idx2]:
#             ll.append(l2[idx2])
#             idx2 += 1
#         else:
#             ll.append(l1[idx1])
#             idx1 += 1
    
#     if idx1 >= len(l1):
#         ll.extend(l2[idx2::])
#     if idx2 >= len(l2):
#         ll.extend(l1[idx1::])
#     return ll 

# print(merge2List([1, 2, 3], [2, 4]))

# lists = [[1,4,5],[1,3,4],[2,6]]
# print(mergeKLists(lists))