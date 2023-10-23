class HashTableSymbolTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def lookup(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    self.table[index].remove(item)

    def display(self):
        for i, chain in enumerate(self.table):
            if chain:  # Check if the chain (list) is not empty
                print(f"Index {i}:")
                for k, v in chain:
                    print(f"    Key: {k}, Value: {v}")

