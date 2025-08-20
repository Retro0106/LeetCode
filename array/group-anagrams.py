class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def calculate(word):
            vocab = [0]*26
            for char in word:
                vocab[ord(char)-ord('a')] += 1
            return vocab

        hashmap = {}
        for word in strs:
            key = tuple(calculate(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return list(hashmap.values())
            
