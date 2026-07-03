class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        up = [i for i in range(m)]
        down = [m - 1 - i for i in range(m)]
        for _ in range(n - 2):
            nu, nd = [0] * m, [0] * m
            s = 0
            for i in range(m):
                nu[i] = s
                s = (s + down[i]) % MOD
            s = 0
            for i in range(m - 1, -1, -1):
                nd[i] = s
                s = (s + up[i]) % MOD
            up, down = nu, nd
        return (sum(up) + sum(down)) % MOD