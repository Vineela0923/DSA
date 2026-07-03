from typing import List
from collections import deque
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        max_cost = 0
        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            max_cost = max(max_cost, c)
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        INF = 10**30
        def check(limit: int) -> bool:
            dp = [INF] * n
            dp[0] = 0
            for u in topo:
                if dp[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, c in graph[u]:
                    if c < limit:
                        continue
                    if v != 0 and v != n - 1 and not online[v]:
                        continue
                    if dp[u] + c < dp[v]:
                        dp[v] = dp[u] + c
            return dp[n - 1] <= k
        if not check(0):
            return -1
        lo, hi = 0, max_cost
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo