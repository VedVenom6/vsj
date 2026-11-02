# Unit IV case study: Dictionary (word -> meaning) using a hash table with chaining
# String keys are turned into a number first, then the division method is applied.
# Load factor = n / size. When it passes 0.75 the table is REHASHED into double the size.

class Dictionary:
    def __init__(self, size=5):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    def h(self, word):
        total = 0
        for ch in word.lower():
            total = total * 31 + ord(ch)          # polynomial rolling hash
        return total % self.size                  # division method

    def insert(self, word, meaning):
        chain = self.table[self.h(word)]
        for pair in chain:
            if pair[0] == word:
                pair[1] = meaning                 # update existing word
                return
        chain.append([word, meaning])
        self.count += 1
        if self.count / self.size > 0.75:
            self.rehash()

    def search(self, word):
        for w, m in self.table[self.h(word)]:
            if w == word:
                return m
        return None

    def delete(self, word):
        chain = self.table[self.h(word)]
        for i, (w, m) in enumerate(chain):
            if w == word:
                chain.pop(i)
                self.count -= 1
                return True
        return False

    def rehash(self):
        old = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for chain in old:
            for w, m in chain:
                self.insert(w, m)
        print(f"  (rehashed to size {self.size})")

    def display(self):
        print(f"size={self.size} words={self.count} load factor={self.count / self.size:.2f}")
        for i, chain in enumerate(self.table):
            if chain:
                print(f"  {i}: " + " -> ".join(w for w, m in chain))


d = Dictionary()
words = {
    "array": "fixed-size collection of elements",
    "stack": "LIFO list",
    "queue": "FIFO list",
    "graph": "nodes connected by edges",
    "tree": "hierarchical structure with a root",
    "hash": "maps a key to a table index",
}
for w, m in words.items():
    d.insert(w, m)
d.display()
print("queue ->", d.search("queue"))
d.delete("stack")
print("stack ->", d.search("stack"))
d.display()

# Collision-handling terms:
#   Open hashing / separate chaining / closed addressing: colliding keys stored in a chain.
#   Closed hashing / open addressing: colliding key probes other slots (linear, quadratic, double hashing).
#   Synonyms = keys with the same hash value. Perfect hash function = no collisions.
