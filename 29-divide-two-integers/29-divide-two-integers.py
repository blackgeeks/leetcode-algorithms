class Solution:
    def check_32_bit(self, n):
	    return n < 1 << 31
    
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        if divisor == 1:
            quotient = dividend
        while dividend >= divisor != 1:
            numshift = 0
            while dividend >= (divisor << numshift):
                numshift += 1
            quotient += 1 << (numshift - 1)
            dividend -= (divisor << (numshift - 1))
        quotient = -quotient if sign == -1 else quotient
        if self.check_32_bit(quotient):
            return quotient
        else:
            return -((1 << 31) - 1) if sign == -1 else ((1 << 31) - 1)
