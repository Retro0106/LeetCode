class Solution(object):
    def reportSpam(self, message, bannedWords):
        """
        :type message: List[str]
        :type bannedWords: List[str]
        :rtype: bool
        """
        # count = 0
        # a = {count += 1 in bannedWords for i in message if i in word}
        # for _ in message:
        #     if _ in bannedWords:
        #         count+=1
        # return count >= 2
        
        count = 0
        banned_set = set(bannedWords)  # Convert bannedWords to a set for O(1) lookups

        for word in message:
            if word in banned_set:  # Check case-sensitive matches
                count += 1
                
        return count >= 2

