class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX=(1<<31)-1
        INT_MIN=-(1<<31)
        if dividend==INT_MIN and divisor==-1:
            return INT_MAX
        sign=-1 if (dividend<0) ^ (divisor<0) else 1
        dividend,divisor=abs(dividend),abs(divisor)
        quotient=0
        for i in range(31,-1,-1):
            if dividend>=(divisor<<i):
                dividend-=divisor<<i
                quotient+=1<<i
        return sign*quotient
        