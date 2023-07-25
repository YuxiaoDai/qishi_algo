# 判断图中两个节点是否连通，一种比较简单直接的方法是使用并查集。
# 先构建并查集，然后将每条边的两个节点合并。最后查询 source 和 destination 的祖宗节点是否相同，相同则说明两个节点连通。
# 时间复杂度 O(n+m×α(m))，空间复杂度 O(n)。其中 n 和 m 分别是节点数和边数

'''
并查集总结：
https://zhuanlan.zhihu.com/p/93647900
https://leetcode.cn/problems/find-if-path-exists-in-graph/solutions/2025571/by-lcbin-96dp/
并查集是一种树形的数据结构，用于处理一些不交集的合并及查询问题。 它支持两种操作：
    查找（Find）：确定某个元素处于哪个子集，单次操作时间复杂度 O(α(n))
    合并（Union）：将两个子集合并成一个集合，单次操作时间复杂度 O(α(n))
以下是并查集的常用模板，需要熟练掌握。其中：
    n 表示节点数
    p 存储每个点的父节点，初始时每个点的父节点都是自己
    size 只有当节点是祖宗节点时才有意义，表示祖宗节点所在集合中点的数量
    find(x) 函数用于查找 x 所在集合的祖宗节点
    union(a, b) 函数用于合并 a 和 b 所在的集合

p = list(range(n))
size = [1] * n
def find(x):
    if p[x] != x:
        # 路径压缩
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        return
    p[pa] = pb
    size[pb] += size[pa]
'''


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        p = list(range(n))
        for u,v in edges:
            p[find(u)] = find(v)
        return find(source) == find(destination)