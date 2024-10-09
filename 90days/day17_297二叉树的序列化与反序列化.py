# 题目地址
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

# 前置知识
# 暂无

# 题目描述
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

# 示例: 

# 你可以将以下二叉树：

#   1
#  / \
# 2   3
#    / \
#   4   5

# 序列化为 "[1,2,3,null,null,4,5]"
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        return str(root.val)+ ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs (data, index):
            if data[index] == 'null':
                return None, index 
            root = TreeNode(data[index])
            root.left, index = dfs(data, index + 1)   # 通过新增一个index值，不断循环data 
            root.right, index = dfs(data, index + 1)  # 一定要返回index，实现index自增
            return root, index
        
        return dfs(data.split(','), 0)[0]
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs (data):
            val = data.pop(0)   # 利用列表pop
            if val=='null':
                return None 
            root = TreeNode(int(val))
            root.left = dfs(data)
            root.right = dfs(data) 
            return root
            
        data = data.split(',')
        return dfs(data)
    

from collections import deque
class Codec:

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
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if data == 'null,': return None
        data = data.split(',')
        
        n = len(data)
        root = TreeNode(int(data.pop(0)))
        queue = deque([root])
        i = 1
        while i < n - 1:
            node = queue.popleft()  # 借助队列实现树的构造
            
            q1 = TreeNode(data.pop(0))
            i += 1
            if q1 != 'null':
                node.left = q1 
                queue.append(node.left)
            
            q2 = TreeNode(data.pop(0))
            i += 1
            if q2 != 'null':
                node.right = q2
                queue.append(node.right)
        return root