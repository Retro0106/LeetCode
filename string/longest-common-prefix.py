class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return string
            string += strs[0][i]
        return string


