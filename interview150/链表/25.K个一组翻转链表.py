#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
#

# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

# 示例 1：


# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 示例 2：



# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
 

# 提示：
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ## 统计链表长度
        tmp = head
        n = 0
        while tmp:
            n += 1 
            tmp = tmp.next 
        
        pre = dummy = ListNode(0)
        dummy.next = head 
        
        while n - k >=0:
            n -= k 
            cur = pre.next 
            tmp = None 
            for i in range(k):
                nxt = cur.next
                cur.next = tmp 
                tmp = cur 
                cur = nxt 
            
            # 92 反转链表II的逻辑
            p0 = pre.next # 1-2-3-4-5
            pre.next.next = cur  # 1-3-4-5
            pre.next = tmp # 0-2-1-3-4-5

            pre = p0 # 1-3-4-5
        return dummy.next

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

