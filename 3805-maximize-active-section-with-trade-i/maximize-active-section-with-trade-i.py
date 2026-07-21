class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        t = '1' + s + '1'
        zeros = []
        i = 0
        while i < len(t):
            if t[i] == '0':
                j = i
                while j < len(t) and t[j] == '0':
                    j += 1
                zeros.append(j - i)
                i = j
            else:
                i += 1
        if len(zeros) < 2:
            return ones
        gain = max(zeros[i] + zeros[i + 1]
                   for i in range(len(zeros) - 1))      
        return ones + gain