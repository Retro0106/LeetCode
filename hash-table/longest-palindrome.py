from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        hashmap = Counter(s)
        maximum = 0
        for word in hashmap:
            if hashmap[word] % 2 == 0:
                total += hashmap[word]
            elif hashmap[word] > maximum:
                maximum = hashmap[word]
        total += maximum
        return total