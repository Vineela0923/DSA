#3286
from heapq import heappush, heappop
class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        dist = [[10**9] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        while pq:
            d, x, y = heappop(pq)
            if (x, y) == (m - 1, n - 1):
                return d < health
            if d > dist[x][y]:
                continue
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = d + grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(pq, (nd, nx, ny))
        return False