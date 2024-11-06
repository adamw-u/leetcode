# 题目地址
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

# 前置知识
# 链表
# 双指针
# 题目描述
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

# 图示两个链表在节点 c1 开始相交：

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'


# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。

def getINstersectionNode(headA, headB):
    """
    https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/12624/intersection-of-two-linked-lists-shuang-zhi-zhen-l/?source=vscode
    思路：
        1.假设交点为node，公共部分长度c，则在交点之前A需要走a-c步，b需要走b-c步
        2.走完a后继续走b-c的长度，或者走完b继续走a-c的长度，直到相交或者A=B=NONE，可用公式进行如下表示：
        3.a + b-c = b + a-c,如果有交点，则一定在走过a+b-c后相交
    """
    tmpA = headA 
    tmpB = headB
    while tmpA!= tmpB:
        tmpA = tmpA.next if tmpA else headB
        
        tmpB = tmpB.next if tmpB else headA

    return tmpA

# 1-2-4-5
# 3-4-5
# 1-2-4-5-3-4-5
# 3-4-5-1-2-4-5   在4-5交点

# 1-2-1
# 3-5
# 1-2-1-3-5
# 3-5-1-2-1  在None交点