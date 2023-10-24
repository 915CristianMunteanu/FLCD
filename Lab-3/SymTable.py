class HashSymTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [None] * size

    def primary_hash(self, key):
        return hash(key) % self.size

    def secondary_hash(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        index1 = self.primary_hash(key)
        index2 = self.secondary_hash(key)

        initial_index = index1

        while self.table[index1] is not None:
            if self.table[index1][0] == key:
                self.table[index1] = (key, value)
                return

            index1 = (index1 + index2) % self.size
            if index1 == initial_index:
                return

        self.table[index1] = (key, value)

    def lookup(self, key):
        index1 = self.primary_hash(key)
        index2 = self.secondary_hash(key)

        initial_index = index1

        while self.table[index1] is not None:
            if self.table[index1][0] == key:
                return self.table[index1][1]

            index1 = (index1 + index2) % self.size
            if index1 == initial_index:
                return None

        return None

    def delete(self, key):
        index1 = self.primary_hash(key)
        index2 = self.secondary_hash(key)

        initial_index = index1

        while self.table[index1] is not None:
            if self.table[index1][0] == key:
                self.table[index1] = None
                return True

            index1 = (index1 + index2) % self.size
            if index1 == initial_index:
                return False

        return False

    def display(self):
        for i, entry in enumerate(self.table):
            if entry:
                print(f"Index {i}: Key: {entry[0]}, Value: {entry[1]}")



htable = HashSymTable()
htable.insert("Danut", "Avocat")
htable.insert("Danut", 25)
htable.display()
print(htable.lookup("Danut"))
htable.delete("Danut")
print(htable.lookup("Danut"))