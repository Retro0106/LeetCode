import random
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.array.append(val)
        self.hashmap[val] = len(self.array)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        prev = self.hashmap[val]
        self.array[prev] = self.array[-1]
        self.hashmap[self.array[-1]] = prev
        del self.hashmap[val]
        self.array.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()