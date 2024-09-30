# 题目地址
# https://leetcode-cn.com/problems/linked-list-cycle-ii/

# 前置知识
# 暂无

# 题目描述
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

# 说明：不允许修改给定的链表。


def detectCycle(self, head) :
    fast = slow = head 
    while fast and  fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast==slow:
            while slow != head:
                head = head.next
                slow = slow.next 
            return slow
    
    return None

# https://leetcode.cn/problems/linked-list-cycle-ii/solutions/1999271/mei-xiang-ming-bai-yi-ge-shi-pin-jiang-t-nvsq/
# 环外长度a， slow走了 a+b 与 fast相遇 ，fast假设走了n圈，则fast总距离 = a+n(b+c)+b = 2(a+b) > (n-1)(b+c) = a-c > head走c步后与slow走c步后在环入口相遇