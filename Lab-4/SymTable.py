

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



class SymbolTable:
    def __init__(self, size):
        self.int_hash_table = HashSymTable(size)
        self.str_hash_table = HashSymTable(size)
        self.identifier_hash_table = HashSymTable(size)

    def insert_integer(self, name, value):

        position = self.int_hash_table.insert(name, value)
        return position

    def insert_string(self, name, value):
        position = self.str_hash_table.insert(name, value)
        return position

    def insert_identifier(self, name, data):
        self.identifier_hash_table.insert(name, data)

    def get_integer(self, name):
        return self.int_hash_table.lookup(name)

    def get_string(self, name):

        return self.str_hash_table.lookup(name)

    def get_identifier(self, name):
        return self.identifier_hash_table.lookup(name)

    def delete_integer(self, name):
        return self.int_hash_table.delete(name)

    def delete_string(self, name):
        return self.str_hash_table.delete(name)

    def delete_identifier(self, name):
        return self.identifier_hash_table.delete(name)

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write("Integer Hash Table:\n")
            for i, entry in enumerate(self.int_hash_table.table):
                if entry:
                    f.write(f"Index {i}: Key: {entry[0]}, Value: {entry[1]}\n")

            f.write("\nString Hash Table:\n")
            for i, entry in enumerate(self.str_hash_table.table):
                if entry:
                    f.write(f"Index {i}: Key: {entry[0]}, Value: {entry[1]}\n")

            f.write("\nIdentifier Hash Table:\n")
            for i, entry in enumerate(self.identifier_hash_table.table):
                if entry:
                    f.write(f"Index {i}: Key: {entry[0]}, Value: {entry[1]}\n")


class Scanner:

    def __init__(self):
        self.tokens = {
            'int': 0, 'print': 1,
            'if': 2, 'else': 3
        }
        self.symtable = SymbolTable(101)

    def is_delimiter(self, ch):
        return ch in " =><;(),:\"{}"

    def is_quoted_string(self, token):
        return len(token) >= 2 and token[0] == '"' and token[-1] == '"'

    def get_tokens(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        tokens_list = []

        for line_no, line in enumerate(lines, start=1):
            i = 0
            while i < len(line):
                if line[i] == '"':
                    start = i
                    i += 1
                    while i < len(line) and line[i] != '"':
                        i += 1
                    if i < len(line) and line[i] == '"':
                        i += 1
                    tokens_list.append((line[start:i], line_no))
                elif not line[i].isspace():
                    start = i
                    while i < len(line) and not line[i].isspace() and line[i] != '"':
                        i += 1
                    tokens_list.append((line[start:i], line_no))
                else:
                    i += 1

        return tokens_list

    def scan(self, tokens):
        pif = []
        for token, line in tokens:
            if self.is_delimiter(token):
                pif.append((token,("delimiter", -1)))
            elif token in self.tokens:
                pif.append((token, ("reserved_word", -1)))
            elif token.isidentifier():
                self.symtable.insert_identifier(token, 0)
                pif.append((token, ("identifier", token)))
            elif token.isnumeric():
                self.symtable.insert_integer(token, 0)
                pif.append((token, ("integer_constant", token)))
            elif self.is_quoted_string(token):
                self.symtable.insert_string(token, 0)
                pif.append((token, ("string_constant", token)))
            else:
                print(f"There is an lexical error at line: {line}, {token}")
        return pif

    def print_symtable(self):
        self.symtable.write_to_file("symtable.txt")



def main():
    scanner = Scanner()
    tokens = scanner.get_tokens("p1.txt")
    pif = scanner.scan(tokens)
    with open("PIF.out", "w") as f:
        for token, descriptor in pif:
            f.write(f"{token} : {descriptor}\n")
    scanner.print_symtable()


if __name__ == "__main__":
    main()