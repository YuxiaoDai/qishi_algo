class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        # 并查集模板
        fa = list(range(n))
        # size[x] 表示节点值等于 vals[x] 的节点个数，
        # 如果按照节点值从小到大合并，size[x] 也是连通块内的等于最大节点值的节点个数
        size = [1] * n
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = n  # 单个节点的好路径
        for vx, x in sorted(zip(vals, range(n))):
            fx = find(x)
            for y in g[x]:
                y = find(y)
                if y == fx or vals[y] > vx:
                    continue  # 只考虑最大节点值不超过 vx 的连通块
                if vals[y] == vx:  # 可以构成好路径
                    ans += size[fx] * size[y]  # 乘法原理
                    size[fx] += size[y]  # 统计连通块内节点值等于 vx 的节点个数
                fa[y] = fx  # 把小的节点值合并到大的节点值上
        return ans
