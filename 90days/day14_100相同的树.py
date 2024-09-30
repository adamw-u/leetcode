# 题目地址
# https://leetcode-cn.com/problems/same-tree/

# 前置知识
# 递归
# 层序遍历
# 前中序确定一棵树
# 题目描述
# 给定两个二叉树，编写一个函数来检验它们是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# 示例 1:

# 输入:       1         1
#         / \       / \
#        2   3     2   3

#       [1,2,3],   [1,2,3]

# 输出: true
# 示例 2:

# 输入:      1          1
#         /           \
#        2             2

#       [1,2],     [1,null,2]

# 输出: false
# 示例 3:

# 输入:       1         1
#         / \       / \
#        2   1     1   2

#       [1,2,1],   [1,1,2]

# 输出: false
from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True 
        if p is not None and q is None:
            return False 
        if p is None and q is not None:
            return False 
        if p.val != q.val:
            return False 
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))