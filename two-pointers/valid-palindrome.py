class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
            else:
                return True
            
            left += 1
            right -= 1
        return True