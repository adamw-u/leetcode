# 题目地址
# https://leetcode-cn.com/problems/rotate-list/

# 前置知识
# 求单链表的倒数第 N 个节点
# 题目描述
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:

# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    tmp1 = head 
    len = 1
    # 把链表处理成环 
    while tmp1.next:
        len += 1
        tmp1 = tmp1.next
    tmp1.next = head

    """
     1-2-3
     |   |
     6-5-4 
    """
    if k >= len:
        k = k%len
    # 在 len-k 处断开
    # 6-1-2-3-4-5
    tmp2 = tmp1
    count = 0
    while tmp2:
        count += 1
        tmp2 = tmp2.next
        if count == len-k:
            break 
    head = tmp2.next
    tmp2.next = None
    return  head

        
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(6)
 
# a.next = b
# b.next = c
# # c.next = d
# # d.next = e
# # e.next = f
# # f.next = None

# head = rotateRight(a, 4)

# while head:
#     print(head.val)
#     head = head.next