class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while True:
            while num>0:
                d=num%10
                num=num//10
                s=s+d
            if s<=9:
                return s
                break
            else:
                num=s
                s=0
        return s