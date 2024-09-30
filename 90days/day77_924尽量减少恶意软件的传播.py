# 题目地址
# https://leetcode-cn.com/problems/minimize-malware-spread

# 前置知识
# 暂无

# 题目描述
# 在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。

# 一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。
# 这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

# 我们可以从初始列表中删除一个节点。如果移除这一节点将最小化 M(initial)， 则返回该节点。如果有多个节点满足条件，就返回索引最小的节点。

# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后可能仍然因恶意软件传播而受到感染。


# 示例 1：

# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
# 示例 2：

# 输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0
# 示例 3：

# 输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
# 输出：1


# 提示：

# 1 < graph.length = graph[0].length <= 300
# 0 <= graph[i][j] == graph[j][i] <= 1
# graph[i][i] == 1
# 1 <= initial.length < graph.length
# 0 <= initial[i] < graph.length

class Solution(object):
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        def dfs(node, visited, size):
            if node not in visited:
                visited.add(node)
                if node in initial:
                    size += 1

                for i in range(n):
                    if graph[node][i] == 1 and i not in visited:
                        visited, size = dfs(i, visited, size = size) # 整数值size是不可变对象必须随着递归输出
                        # 如果不输出size,最后return的size就是最上面的 size+=1 0+1=1 
                        # 外层的 size 始终是递归初始的值，因此最终的 size 仍然是 1，即初次递归时 dfs(0) 中的 size。
                        print('size', size)
            return visited, size
        
        # 需要统计visited内initial个数，如果全部包含两个以上则取序号最小
        # 如果有包含一个的则len(visited)最大序号最小的
        res_dict = {}
        initial.sort()
        for i,j in enumerate(initial):
            res_dict[initial[i]] = (dfs(initial[i], visited=set(), size = 0))
        
        res = initial[0]
        size = 0
        for i, (v, s) in res_dict.items():
             if s == 1:
                  if len(v) > size:
                      size = len(v)
                      res = i
        return res , res_dict

so = Solution()
# graph = [[1,0,0,0,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,1,0],[0,0,0,0,0,0,1,1,0,0,0],[0,0,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,1]]
# initial = [7,8,6,2,3]
graph = [[1,1,0], [1,1,0],[0,0,1]]
initial = [0,1,2]
print(so.minMalwareSpread(graph, initial))



# def dfs(node, visited, size):
#     if node not in visited:
#         visited.add(node)
#         if node in initial:
#             size += 1
#             print("node", node, size)

#         for i in range(n):
#             if graph[node][i] == 1 and i not in visited:
#                 dfs(i, visited, size)
#     return visited, size

# def dfs(node, visited, size):
#     if node not in visited:
#         visited.add(node)
#         if node in initial:
#             size += 1
#             print("node", node, size)

#         for i in range(n):
#             if graph[node][i] == 1 and i not in visited:
#                 visited, size = dfs(i, visited, size)  # 累加递归中的 size
#     return visited, size

# graph = [[1,1,0],[1,1,0],[0,0,1]]
# n = len(graph)
# initial = [0, 1, 2]

# visited1, size1 = dfs(initial[0], visited=set(), size = 0)
# print(visited1, size1)

