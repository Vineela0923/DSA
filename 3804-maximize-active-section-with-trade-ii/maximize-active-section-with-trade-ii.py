from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        starts, ends, lens = [], [], []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                starts.append(i)
                ends.append(j - 1)
                lens.append(j - i)
                i = j
            else:
                i += 1
        m = len(lens)
        if m < 2:
            return [total_ones] * len(queries)
        val = [lens[i] + lens[i + 1] for i in range(m - 1)]
        st = [val]
        k = 1
        while (1 << k) <= len(val):
            prev = st[-1]
            half = 1 << (k - 1)
            st.append([
                max(prev[i], prev[i + half])
                for i in range(len(val) - (1 << k) + 1)
            ])
            k += 1
        def rmq(l, r):
            if l > r:
                return 0
            k = (r - l + 1).bit_length() - 1
            return max(
                st[k][l],
                st[k][r - (1 << k) + 1]
            )
        ans = []
        for l, r in queries:
            a = bisect_left(ends, l)
            b = bisect_right(starts, r) - 1
            if a >= m or b < 0 or a >= b:
                ans.append(total_ones)
                continue
            left = ends[a] - max(starts[a], l) + 1
            right = min(ends[b], r) - starts[b] + 1
            if b == a + 1:
                gain = left + right
            else:
                gain = max(
                    left + lens[a + 1],
                    lens[b - 1] + right,
                    rmq(a + 1, b - 2)
                )
            ans.append(total_ones + gain)
        return ans