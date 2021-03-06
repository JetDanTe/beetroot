from functools import reduce


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.re_hash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        counter = 0
        for i in self.slots:
            if not i is None:
                counter += 1
        return sum([1 for i in self.slots if not i is None])
        #return reduce(lambda a, x: a + 1 if x is not None else a, self.slots, 0)

    def __contains__(self, item):
        slot = self.hash_function(item, len(self.slots))
        if self.slots[slot] == item:
            return True
        re_slot = slot
        while self.slots[re_slot] != item:
            re_slot = self.re_hash(re_slot, len(self.slots))
            if slot == re_slot:
                return False
        return True

    def __delitem__(self, key):
        slot = self.hash_function(key, len(self.slots))
        if self.slots[slot] == key:
            self.slots[slot] = None
            self.data[slot] = None
            return
        re_slot = slot
        while self.slots[re_slot] != key:
            re_slot = self.re_hash(re_slot, len(self.slots))
            if slot == re_slot:
                raise IndexError("Circle!")
        self.slots[re_slot] = None
        self.data[re_slot] = None






if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)

    print(H[20])

    print(H[17])
    H[20] = "duck"
    print(H[20])
    print(H[99])
    print(f"Was {len(H)}")
    del H[44]
    H.__contains__(26)
    print(f"Will {len(H)}")
