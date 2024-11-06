# 题目地址
# https://leetcode-cn.com/problems/implement-queue-using-stacks/

# 前置知识
# 栈
# 队列
# 题目描述
# 使用栈实现队列的下列操作：

# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 示例:

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);
# queue.peek(); // 返回 1
# queue.pop(); // 返回 1
# queue.empty(); // 返回 false
# 说明:

# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的、 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

class Queue():
    """
    思路：
        1.用List维护两个栈
        2.入栈List append
        3.出栈，将入栈中的元素倒序加入到出栈中，模拟队列pop()
    """
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        # 栈特性是LIFO(Last In First Out)
        # 如果将栈转成队列FIFO，例如queue.push(1);queue.push(2);  栈的pop->2 队列pop->1  需要维护一个出栈即先将进栈中元素转到出LIFO+LIFO->FIFO
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]


    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        return False
