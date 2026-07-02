class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * (n + 1)
        for i, c in enumerate(s):
            if c.islower():
                length[i + 1] = length[i] + 1
            elif c == '*':
                length[i + 1] = max(0, length[i] - 1)
            elif c == '#':
                length[i + 1] = length[i] * 2
            else:  # '%'
                length[i + 1] = length[i]
        if k >= length[n]:
            return '.'
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c.islower():
                if k == length[i]:
                    return c
            elif c == '#':
                k %= length[i]
            elif c == '%':
                k = length[i] - 1 - k
        return '.'