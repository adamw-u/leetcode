#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#


# Tags
# greedy

# Companies
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

 

# 示例 1:

# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
# 示例 2:

# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。

# @lc code=start
from typing import List
class Solution:
    """
    思路：
        1. 对每一个满足gas[i] >= cost[i]点进行环遍历，如果满足条件就输出i
        2. 超时复杂度O(n2)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) - sum(gas) > 0:
            return -1 
        
        def getCycle(n, i):
            listn = list(range(n))
            return listn[i::] + listn[0:i]
        
        
        for i in range(n):
            if gas[i] >= cost[i]:
                res = True
                cycle_list = getCycle(n, i)
                for j in range(n):
                    if sum([gas[i] for i in cycle_list[0:j]]) - sum([cost[i] for i in cycle_list[0:j]]) < 0:
                        res =  False
                if res:
                    return i
        return -1
    
    """
    思路2:
        1. 如果x到达不了y+1，那么x-y之间的点也不可能到达y+1，因为中间任何一点的油都是拥有前面的余量的，所以下次遍历直接从y+1开始
        2. https://leetcode.cn/problems/gas-station/solutions/488357/jia-you-zhan-by-leetcode-solution/?source=vscode
        3. 对于超过n的索引用j = (i + cnt) % n   表示
        4. 时间复杂度O(n),空间复杂度O(1)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_cost > sum_of_gas:
                    break
                cnt += 1  # sum_of_gas>sum_of_cost个数
            if cnt == n: # 当cnt==n代表可以环路走完
                return i
            else:
                i += cnt + 1  # 否则i 从 cnt+1开始继续往下找  **关键点***
        return -1


        
# @lc code=end

