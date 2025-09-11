class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        parsed = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            parsed.append([name, int(time), int(amount), city, transaction])

        invalid = set()
        for t in parsed:
            if t[2] > 1000:
                invalid.add(t[4])
        for i in range(len(parsed)):
            for j in range(i+1, len(parsed)):
                first = parsed[i]
                second = parsed[i+1]

                if first[0] == second[0] and abs(first[1]-second[1]) <= 60 and first[3] != second[3]:
                    invalid.add(first[4])
                    invalid.add(second[4])
        return list(invalid)
        

            