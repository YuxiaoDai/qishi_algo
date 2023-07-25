'''
我们可以遍历 trust，统计每个节点的入度和出度，存储在 inDegrees 和 outDegrees中。
在法官存在的情况下，法官不相信任何人，每个人（除了法官外）都信任法官，且只有一名法官。因此法官这个节点的入度是 n−1, 出度是 0。
我们可以遍历每个节点的入度和出度，如果找到一个符合条件的节点，可以直接返回结果；如果不存在符合条件的点，则返回 −1。
'''
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegrees = {i+1:0 for i in range(n)}
        outDegrees = {i+1:0 for i in range(n)}
        for x,y in trust:
            inDegrees[y] += 1
            outDegrees[x] += 1

        for i in range(1,n+1):
            if inDegrees[i] == n - 1 and outDegrees[i] == 0:
                return i
        
        return -1