class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        if x < 0:
            x = -x
            sign = -1
        else:
            sign = 1

        n = x

        while x > 0:
            r = x % 10
            rev = rev * 10 + r
            x //= 10

        rev = rev * sign

        if -(2**31) <= rev <= (2**31) - 1:
            return rev
        else:
            return 0