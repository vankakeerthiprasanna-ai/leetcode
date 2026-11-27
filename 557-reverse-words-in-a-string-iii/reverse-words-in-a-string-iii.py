class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        r_w=[word[::-1]for word in w]
        return " ".join(r_w)