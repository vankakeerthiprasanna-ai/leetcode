class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        sign = 1

        if x < 0:
            sign = -1
            x = -x

        while x > 0:
            d = x % 10
            r = r * 10 + d
            x //= 10

        r = r * sign

        if r < -2**31 or r > 2**31 - 1:
            return 0

        return r