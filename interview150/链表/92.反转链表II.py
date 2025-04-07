#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
#

# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 

# 示例 1：


# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：

# 输入：head = [5], left = 1, right = 1
# 输出：[5]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    """
    思路:
        1. 用dummy 和 pre 复制head链表
        2. 在left-1地方对pre断开 
        3. 对pre的[1,right - left + 1)进行反转,也就是对head的[left, right]反转
        4. 最后利用pre next.next 和 .next两个指针实现对最后一个位置与倒数第二个位置的指向
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        # 0->1->2->3->4->5
        pre = dummy 
        for i in range(left - 1):
            pre = pre.next
        # pre = 1->2->3->4->5

        tmp = None 
        cur = pre.next
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = tmp # 这两句位置不能反
            tmp = cur  
            cur = nxt  
        
        # 巧妙的地方
        pre.next.next = cur #2-> 5
        pre.next = tmp # 1->4 

        return dummy.next 

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

