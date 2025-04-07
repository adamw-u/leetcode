# 24. 两两交换链表中的节点
# 入选理由
# 暂无

# 题目地址
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

# 前置知识
# 链表的基本知识
# 题目描述
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


from typing import Optional

class ListNode:
    def __init__(self, val , next = None) -> None:
        self.val = val 
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1-2-3-4
        dummyHead = ListNode(0) 
        dummyHead.next = head 
        tmp = dummyHead 
        while tmp.next and tmp.next.next:
            node1 = tmp.next       #1
            node2 = tmp.next.next  #2

            tmp.next = node2 # node0 指向原链表第二个节点 0-2

            node1.next = node2.next # 1-3
            node2.next = node1 # 2-1 完成第一步反转 0-2-1-3-4

            tmp = node1 # 更新tmp 1-3-4
        return dummyHead.next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        n = 0 
        while tmp:
            n += 1
            tmp = tmp.next
        
        p0 = dummy = ListNode(0)
        dummy.next = head 

        while n-k >= 0:
            n -= k
            pre = None #开始反转
            cur = p0.next 
            for _ in range(k):
                nxt = cur.next
                cur.next = pre 
                pre = cur 
                cur = nxt # 结束反转,记住当前反转到的位置

            tmp = p0.next   # 先把p0暂存下来后面用 1-2-3-4
            # 妙的地方 画图理解
            # p0.next 指向反转好的 pre的，即dummy节点 0-2-1
            p0.next.next = cur 
            # p0.next.next 指向反转位置的下一步即可完成反转， 由于p0.next是1，则p0.next.next 代表1-3-4
            # 例 0-1-2-3-4   0-2—1-3—4
            p0.next = pre    # 跟上面一行的位置不能换,互换之后导致p0.next.next值改变
            p0 = tmp  # p0更新继续反转   由于前面暂存时指向1，更新完成后 就变成1-3-4
        return dummy.next 