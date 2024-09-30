# 题目地址
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

# 前置知识
# 链表
# 双指针
# 题目描述
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

# 图示两个链表在节点 c1 开始相交：



# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。

def getINstersectionNode(headA, headB):
    tmpA = headA 
    tmpB = headB
    while tmpA!= tmpB:
        if not tmpA:
            tmpA = headB
        else:
            tmpA = tmpA.next 
        
        if not tmpB:
            tmpB = headA
        else:
            tmpB = tmpB.next 

    return tmpA

# 1-2-4-5
# 3-4-5
# 1-2-4-5-3-4-5
# 3-4-5-1-2-4-5   在4-5交点

# 1-2-1
# 3-5
# 1-2-1-3-5
# 3-5-1-2-1  在None交点