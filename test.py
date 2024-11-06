nums = [5,1,1,2,0,0]
# mid 与 r 交换位置 
# 对比 l,r区间内，所有小于r的值往前走，大于r的往后走
# 如何交换？
# 设置指针 i = l-1
import random 
def quickSort(nums, l, r):
    mid = 1 #random.randint(l, r)
    nums[r], nums[mid] = nums[mid], nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < nums[r]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i, nums

quickSort(nums, 0, 5)