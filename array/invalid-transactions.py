class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # parse
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append([name, int(time), int(amount), city, t])

        n = len(parsed)
        invalid_flags = [False] * n  # track invalids by index

        # Rule 1: amount > 1000
        for i, (name, time, amount, city, orig) in enumerate(parsed):
            if amount > 1000:
                invalid_flags[i] = True

        # Rule 2: same name, different city within 60 mins
        for i in range(n):
            for j in range(i+1, n):
                n1, t1, a1, c1, o1 = parsed[i]
                n2, t2, a2, c2, o2 = parsed[j]
                if n1 == n2 and abs(t1 - t2) <= 60 and c1 != c2:
                    invalid_flags[i] = True
                    invalid_flags[j] = True

        # collect results preserving duplicates
        return [parsed[i][4] for i in range(n) if invalid_flags[i]]


        
        # parsed = []

        # for transaction in transactions:
        #     name, time, amount, city = transaction.split(',')
        #     parsed.append([name, int(time), int(amount), city, transaction])

        # invalid = set()
        # for t in parsed:
        #     if t[2] > 1000:
        #         invalid.add(t[4])
        # for i in range(len(parsed)):
        #     for j in range(i+1, len(parsed)):
        #         first = parsed[i]
        #         second = parsed[j]

        #         if first[0] == second[0] and abs(first[1]-second[1]) <= 60 and first[3] != second[3]:
        #             invalid.add(first[4])
        #             invalid.add(second[4])
        # return list(invalid)
        

            