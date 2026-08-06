class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            prod = 1
            while x:
                prod *= x % 10
                x //= 10
            return prod
        for num in range(n, 101):
            if digit_product(num) % t == 0:
                return num
        return -1