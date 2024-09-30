# 24. 两两交换链表中的节点
# 入选理由
# 暂无

# 题目地址
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

# 前置知识
# 链表的基本知识
# 题目描述
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


from typing import Optional

class ListNode:
    def __init__(self, val , next = None) -> None:
        self.val = val 
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0) 
        dummyHead.next = head 
        tmp = dummyHead 
        while tmp.next and tmp.next.next:
            node1 = tmp.next 
            node2 = tmp.next.next 

            tmp.next = node2 

            node1.next = node2.next 
            node2.next = node1

            tmp = node1 
        return dummyHead.next

