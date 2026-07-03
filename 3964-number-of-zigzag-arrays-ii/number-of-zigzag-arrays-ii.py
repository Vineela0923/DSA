class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m
        sz = 2 * m
        T = [[0] * sz for _ in range(sz)]
        for i in range(m):
            for j in range(i):
                T[i][m + j] = 1      # up <- down
            for j in range(i + 1, m):
                T[m + i][j] = 1      # down <- up
        def matmul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if A[i][k]:
                        a = A[i][k]
                        for j in range(n):
                            C[i][j] = (C[i][j] + a * B[k][j]) % MOD
            return C
        def matpow(M, p):
            n = len(M)
            R = [[int(i == j) for j in range(n)] for i in range(n)]
            while p:
                if p & 1:
                    R = matmul(R, M)
                M = matmul(M, M)
                p >>= 1
            return R
        vec = [0] * sz
        for i in range(m):
            vec[i] = i
            vec[m + i] = m - 1 - i
        P = matpow(T, n - 2)
        ans = 0
        for i in range(sz):
            s = 0
            for j in range(sz):
                s = (s + P[i][j] * vec[j]) % MOD
            ans = (ans + s) % MOD
        return ans