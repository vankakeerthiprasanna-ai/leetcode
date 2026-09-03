class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x//=10
        if rev==n:
            return True
        else:
            return False
        