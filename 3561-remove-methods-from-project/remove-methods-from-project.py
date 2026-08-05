from typing import List
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
        vis = [False] * n
        stack = [k]
        vis[k] = True
        while stack:
            u = stack.pop()
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    stack.append(v)
        for u, v in invocations:
            if vis[v] and not vis[u]:
                return list(range(n))
        return [i for i in range(n) if not vis[i]]