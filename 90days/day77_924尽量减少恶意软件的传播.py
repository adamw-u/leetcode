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
    """
    https://leetcode.cn/problems/minimize-malware-spread/solutions/2741790/zhi-bao-han-yi-ge-bei-gan-ran-jie-dian-d-ym39/
    算法如下：
        1.遍历 initial 中的节点 x。
        2.如果 x 没有被访问过，那么从 x 开始 DFS，同时用一个 vis 数组标记访问过的节点。
        3.DFS 过程中，统计连通块的大小 size。
        4.DFS 过程中，记录访问到的在 initial 中的节点。
        5.DFS 结束后，如果发现该连通块只有一个在 initial 中的节点，并且该连通块的大小比最大的连通块更大，那么更新最大连通块的大小，以及答案节点 x。如果一样大，就更新答案节点的最小值。
        最后，如果没找到符合要求的节点，返回 min(initial)；否则返回答案节点。
    """
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        def dfs(node, visited, size):
            """
            size：代表节点可以额外感染的点的个数
            visited：感染的集合
            """
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
            """
            一个大小为 k 的连通块内，如果只有一个节点 x 被感染（x 在 initial 中），那么移除 x 后，这个连通块不会被感染，从而让 M(initial) 减少 k。
            而如果连通块内至少有两个节点被感染，无论移除哪个节点，仍然会导致连通块的所有节点被感染，M(initial) 不变。
            所以我们要找的是只包含一个被感染节点的连通块，并且这个连通块越大越好。
            """
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

