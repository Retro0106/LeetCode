class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # if given an empty string, return 0

    # initiliaze an empty set, longest variable
    #    iterate through the string
    # check if current element is in my set
    # keep track of longest at that point and update
    # inner while loop shifting the left of my window until i remove the duplicate
    # for loop keeps running until end of the string
    # update longest

        longest = 0
        i =  0

        if len(s) == 0:
            return 0
        seen = set()
        
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            longest = max(longest, len(seen))
        return longest
        
    # "pwwkew"
    #     i
    #        j      

    # set -> kew
    # longest -> 3


