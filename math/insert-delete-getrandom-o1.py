class RandomizedSet:

    def __init__(self):
        self.my_set = set()

    def insert(self, val: int) -> bool:
        if val in self.my_set:
            return False
        self.my_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.my_set:
            self.my_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        for i in self.my_set:
            return i


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()