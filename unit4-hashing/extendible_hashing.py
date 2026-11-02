# Lab C3 (syllabus list): Extendible hashing
# Directory of 2^global_depth pointers to buckets. A bucket that overflows SPLITS;
# if its local depth == global depth, the directory DOUBLES first.
# Index = last `global_depth` bits of the key (key % 2^gd).

BUCKET_SIZE = 2


class Bucket:
    def __init__(self, depth):
        self.depth = depth          # local depth
        self.items = {}             # key -> value


class ExtendibleHash:
    def __init__(self):
        self.gd = 1                                   # global depth
        self.dir = [Bucket(1), Bucket(1)]

    def index(self, key):
        return key % (2 ** self.gd)                   # last gd bits

    def search(self, key):
        return self.dir[self.index(key)].items.get(key)

    def insert(self, key, value):
        b = self.dir[self.index(key)]
        if key in b.items or len(b.items) < BUCKET_SIZE:
            b.items[key] = value
            return
        self.split(b)                                 # bucket full -> split, then retry
        self.insert(key, value)

    def split(self, b):
        if b.depth == self.gd:                        # directory must double
            self.dir = self.dir + self.dir
            self.gd += 1
            print(f"  directory doubled -> global depth {self.gd}")
        b.depth += 1
        new = Bucket(b.depth)
        bit = 1 << (b.depth - 1)                      # the new bit that separates them
        for i in range(len(self.dir)):                # re-point half of b's entries
            if self.dir[i] is b and i & bit:
                self.dir[i] = new
        old = b.items
        b.items = {}
        for k, v in old.items():                      # redistribute keys
            self.dir[self.index(k)].items[k] = v
        print(f"  bucket split -> local depth {b.depth}")

    def delete(self, key):
        b = self.dir[self.index(key)]
        if key in b.items:
            del b.items[key]
            return True
        return False

    def display(self):
        print(f"Global depth = {self.gd}")
        for i, b in enumerate(self.dir):
            print(f"  {i:0{self.gd}b} -> (local {b.depth}) {b.items}")


eh = ExtendibleHash()
while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        k = int(input("Key: "))
        eh.insert(k, input("Value: "))
    elif ch == 2:
        v = eh.search(int(input("Key: ")))
        print(f"Value = {v}" if v is not None else "Key not found")
    elif ch == 3:
        print("Deleted" if eh.delete(int(input("Key: "))) else "Key not found")
    elif ch == 4:
        eh.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
