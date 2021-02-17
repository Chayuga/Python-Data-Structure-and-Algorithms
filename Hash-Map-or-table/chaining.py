"""
Handling collision in Hash Map or Hash Table. 
"""


class HashTable(object):
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    # Finding a hash value (ASCII Value)
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX

    # Setting Item (Adding Item)

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    # Getting item

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    # Deleting Item
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.ar[h][idx]


# creating an object of a class
t = HashTable()
t.get_hash('march 6')
