# 题目地址
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/

# 前置知识
# 暂无

# 题目描述
# 给定一个二叉树，在树的最后一行找到最左边的值。

# 示例 1:

# 输入:

#   2
#  / \
# 1   3

# 输出:
# 1
 

# 示例 2:

# 输入:

#       1
#      / \
#     2   3
#    /   / \
#   4   5   6
#      /
#     7

# 输出:
# 7

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left = node.val 
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return left