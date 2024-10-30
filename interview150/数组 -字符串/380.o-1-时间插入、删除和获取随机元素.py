#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# Tags
# array | hash-table | design

# Companies
# 实现RandomizedSet 类：

# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

 

# 示例：

# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]

# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。


# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}  # key index
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.nums)  # 代表了数字的idx
            self.nums.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            swap_val = self.nums[-1] 

            ## 例子
            ## dict = {1:0, 3:1, 4:2}
            ## nums = [1, 3, 4]
            ## 我要删除3, 3对应的：idx=1, swap_val=4
            ## 经过下面两行代码：nums=[1, 4, 4], dict={1:0, 3:1, 4:1}
            # 最后 del 和 pop操作后nums=[1, 4], dict={1:0, 4:1}， 完成了O(1)删除元素3

            self.nums[idx] = swap_val # 把对应索引的原始值替换成 swap_val
            self.dict[swap_val] = idx # 更新swap_val的索引为idx
            del self.dict[val]
            self.nums.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

