# 前置知识
# DFS
# BFS
# 前序遍历
# 题目描述
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

# 例如，从根到叶子节点路径 1->2->3 代表数字 123。

# 计算从根到叶子节点生成的所有数字之和。

# 说明: 叶子节点是指没有子节点的节点。

# 示例 1:

# 输入: [1,2,3]
#   1
#  / \
# 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
# 示例 2:

# 输入: [4,9,0,5,1]
#   4
#  / \
# 9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 构建测试二叉树: 
root = TreeNode(9)
root.left = TreeNode(2)
root.right = TreeNode(1)


from typing import Optional
def sumNumbers(root: Optional[TreeNode]) -> int:
    
    def dfs(root, res):
        if not root:
            return res 
        res += root.val
        if root.left and not root.right:
            return dfs(root.left, res * 10)
        if root.right and not root.left:
            return dfs(root.right, 10* res)
        if not root.left and not root.right:
            return res
        else:
            return dfs(root.left, 10 * res) + dfs(root.right, 10* res)

    return dfs(root, 0)