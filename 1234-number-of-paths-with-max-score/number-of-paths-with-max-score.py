from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n, MOD = len(board), 10**9 + 7
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue
                best, ways = -1, 0
                for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if x < n and y < n:
                        s, w = dp[x][y]
                        if s > best:
                            best, ways = s, w
                        elif s == best and s != -1:
                            ways = (ways + w) % MOD
                if best != -1:
                    if board[i][j].isdigit():
                        best += int(board[i][j])
                    dp[i][j] = (best, ways)
        return [0, 0] if dp[0][0][0] == -1 else [dp[0][0][0], dp[0][0][1]]