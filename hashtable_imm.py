class HashTable:

    class Node:

        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, n=1000):
        self.table = [None] * n
        self.keys = []

    def __len__(self):
        return len(self.keys)

    def __setitem__(self, key, value):
        index = hash(key) % len(self.table)
        n = self.table[index]
        while n is not None:
            if n.key == key:
                n.value = value
                return
            n = n.next
        self.table[index] = HashTable.Node(key, value, self.table[index])
        self.keys.append(key)

    def __getitem__(self, key):
        index = hash(key) % len(self.table)
        n = self.table[index]
        while n is not None:
            if n.key == key:
                return n.value
            n = n.next
        else:
            raise KeyError(key)

    def __contains__(self, key):
        try:
            x = self[key]
            return True
        except:
            return False

    def __iter__(self):
        for key in self.keys:
            yield key

    def __repr__(self):
        return "{" + ', '.join(repr(key) + ':' + repr(self[key]) for key in self) + "}"
