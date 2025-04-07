#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = res = ListNode(0)
        while list1 and list2:
            if list1.val >= list2.val:
                tmp.next = list2 #ListNode(list2.val) 
                list2 = list2.next 
            else:
                tmp.next = list1 #ListNode(list1.val)
                list1 = list1.next
            tmp = tmp.next 

        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2 
        return res.next 
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

