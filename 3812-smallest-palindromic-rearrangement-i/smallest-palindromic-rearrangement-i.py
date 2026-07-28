class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        half = []
        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + ord('a'))
            half.append(chr(i + ord('a')) * (freq[i] // 2))
        left = "".join(half)
        return left + mid + left[::-1]