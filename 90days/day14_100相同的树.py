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
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):  # 按位异或（当且仅当两个位不同时结果才为1，否则为0） 一个为True一个False才会是True
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        res = ''
        while queue:
            root = queue.popleft()
            if not root:
                res += 'null,'
            else:
                res += str(root.val) + ','
                queue.append(root.left)
                queue.append(root.right)
        return res 
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        return str(root.val)+ ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pList = self.serialize(p)
        qList = self.serialize(q)
        # print(pList, qList)
        if pList == qList:
            return True
        return False