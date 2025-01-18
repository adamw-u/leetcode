#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
#
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：

# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

# 示例 1：

# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 示例 2：

# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    思路：
        1. 找到链表的中位数节点，断开
        2. 对找中位数后面的链表内容反转
        3. 合并两个链表
    """
    def getMidList(self, head: Optional[ListNode]) -> None:
        low = head
        fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next 
        return low 
    
    def reversedList(self, head: Optional[ListNode]):
        tmp = None
        while head:
            nxt = head.next
            head.next  = tmp
            tmp =  head 
            head = nxt 
        return tmp

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.getMidList(head)
        head2 = self.reversedList(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

