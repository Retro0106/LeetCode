class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        j = len(s)-1
        lis = s.split()
        return " ".join(lis[::-1])
