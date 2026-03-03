class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1

        trusted = [0] * (n + 1)
        trusts_someone = set()

        for a, b in trust:
            trusts_someone.add(a)
            trusted[b] += 1

        for i in range(1, n + 1):
            if i not in trusts_someone and trusted[i] == n - 1:
                return i

        return -1
            