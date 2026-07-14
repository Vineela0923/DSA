class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        s = "123456789"
        res = []      
        for length in range(2, 10):
            for i in range(0, 10 - length):
                num = int(s[i:i + length])
                if num > high:
                    return res
                if num >= low:
                    res.append(num)     
        return res