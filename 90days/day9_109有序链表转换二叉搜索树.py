# 题目地址
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

# 前置知识
# 递归
# 二叉搜索树的任意一个节点，当前节点的值必然大于所有左子树节点的值。同理,当前节点的值必然小于所有右子树节点的值
# 题目描述
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定的有序链表： [-10, -3, 0, 5, 9],

# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

#     0
#    / \
#  -3   9
#  /   /
# -10  5


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):

    def getLinkMid(left , right):
        slow = left 
        fast = left 
        while fast.next != right and fast.next.next!=right:
            slow = slow.next 
            fast = fast.next.next 
        return slow 
    
    def buildTree(left, right):
        if left==right:
            return None 
        mid = getLinkMid(left, right )
        root = TreeNode(mid.val)
        root.left = buildTree(left, mid)
        root.right = buildTree(mid.next, right)
        return root 

    return buildTree(head, None )
