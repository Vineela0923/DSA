from typing import List
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suffix = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suffix[i] = (m - 1 - j)
        res = []
        j = 0
        usedMismatch = False
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            else:
                if not usedMismatch:
                    remaining = m - (j + 1)
                    if suffix[i + 1] >= remaining:
                        usedMismatch = True
                        res.append(i)
                        j += 1
        return res if j == m else []