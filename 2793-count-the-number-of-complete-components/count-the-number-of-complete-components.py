from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i]:
                continue
            stack = [i]
            visited[i] = True
            vertices = 0
            degree_sum = 0
            while stack:
                node = stack.pop()
                vertices += 1
                degree_sum += len(graph[node])
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
            if degree_sum // 2 == vertices * (vertices - 1) // 2:
                ans += 1
        return ans