from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        c = Counter(s)
        h = [0] * 26
        m = ""
        n = 0
        for i in range(26):
            ch = chr(i + 97)
            h[i] = c[ch] // 2
            n += h[i]
            if c[ch] & 1:
                m = ch
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] * i
        w = f[n]
        for x in h:
            w //= f[x]
        if w < k:
            return ""
        l = []
        while n:
            for i in range(26):
                if h[i] == 0:
                    continue
                t = w * h[i] // n
                if t >= k:
                    l.append(chr(i + 97))
                    w = t
                    h[i] -= 1
                    n -= 1
                    break
                else:
                    k -= t
        l = "".join(l)
        return l + m + l[::-1]