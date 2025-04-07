#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

# 示例 1：


# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：

# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：

# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]

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
    思路:
        1. 初始化两个链表，一个用来该表指针位置，一个用来保存结果
        2. 保证进位正确性，如果最后一位carry>0，l1 l2为空了，需要把carry放到结果中
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = curr = ListNode(0)

        addRes = 0 
        while l1 or l2 or carry >0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            addRes = v1 + v2 + carry
            carry = addRes // 10 
            curr.next = ListNode(addRes % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next 
            
        return res.next
        
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

