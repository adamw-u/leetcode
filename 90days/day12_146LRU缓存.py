# 题目描述
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 实现 LRUCache 类：

# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？



# 示例：

# 输入

# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 解释

# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4


# OrderedDict 思路
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if key not in  self.cache:
            return -1 
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value 
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 双链表加hashmap
class Node:
    def __init__(self,key,val,pre=None,next=None):
        self.key = key
        self.val = val
        self.pre = None 
        self.next = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur = 0
        self.hashmap = {}
        self.dummy = Node(0,0)
        self.tail = Node(0,0)
        
        self.dummy.next = self.tail
        self.tail.pre = self.dummy
    
    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            
            node.pre.next = node.next
            node.next.pre = node.pre 
            
            temp = self.dummy.next
            self.dummy.next = node
            node.next = temp
            
            temp.pre = node
            node.pre = self.dummy
            return self.hashmap[key].val
        else:
            return -1
    def put(self, key, value):
        if key in self.hashmap:
            self.hashmap[key].val = value
            
            node = self.hashmap[key]
            node.pre.next = node.next
            node.next.pre = node.pre
            
        else:
            new = Node(key,value)
            self.hashmap[key] = new
            if self.cur>=self.capacity:
                self.tail = self.tail.pre
                self.tail.next = None
                
                del self.hashmap[self.tail.key]
                self.cur -=1 
            self.cur+=1
        node = self.hashmap[key]
        
        temp = self.dummy.next
        self.dummy.next = node
        node.next = temp
        
        temp.pre = node
        node.pre = self.dummy
