
# 题目地址
# https://leetcode-cn.com/problems/sqrtx

# 前置知识
# 二分法
# 题目描述
# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:

# 输入: 4
# 输出: 2
# 示例 2:

# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x 
        while l <= r:
            mid = (l + r)//2
            # print(l, r, mid )
            if mid ** 2 == x:
                return int(mid) 
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1
        return l-1 # r

# 进阶
def sqrt_binary_search(x, precision=1e-7):
    if x < 0:
        raise ValueError("不能计算负数的平方根")
    
    # 处理特殊情况
    if x == 0 or x == 1:
        return x
    
    # 定义左右边界
    low, high = 0, x
    if x < 1:  # 如果 x 是小数，则 high = 1
        high = 1
    
    # 二分法逼近平方根
    while high - low > precision:
        mid = (low + high) / 2
        if mid * mid > x:
            high = mid
        else:
            low = mid
    
    return low

# 示例
x = 15
result = sqrt_binary_search(x)
print(f"{x} 的平方根是 {result:.7f}")