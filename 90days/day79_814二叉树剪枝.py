# 题目地址
# https://leetcode-cn.com/problems/binary-tree-pruning

# 前置知识
# 二叉树
# 递归
# 题目描述
# 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

# 返回移除了所有不包含 1 的子树的原二叉树。

# ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

# 示例1:
# 输入: [1,null,0,0,1]
# 输出: [1,null,0,null,1]

# 示例2:
# 输入: [1,0,1,0,0,0,1]
# 输出: [1,null,1,null,1]

# 示例3:
# 输入: [1,1,0,1,1,0,1,0]
# 输出: [1,1,0,1,1,null,1]

# 说明:

# 给定的二叉树最多有 100 个节点。
# 每个节点的值只会为 0 或 1

# roo.left = None and root.right = None root.val = 0 return = None 
def pruneTree(root):
    if not root:
        return None 
    pruneTree(root.left)
    pruneTree(root.right)
    if root.left is None and root.right is None and root.val == 0 :
        return None 
    return root 

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root
