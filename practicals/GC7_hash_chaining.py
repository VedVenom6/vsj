# GC7: Hash table of size 10, division method h(k) = k % 10, collisions by chaining

SIZE = 10
table = [[] for _ in range(SIZE)]     # each slot is a chain (list of [key, value])


def h(key):
    return key % SIZE                 # division method


def insert(key, value):
    chain = table[h(key)]
    for pair in chain:
        if pair[0] == key:            # key already there -> update value
            pair[1] = value
            return
    chain.append([key, value])        # collision just grows the chain


def search(key):
    for k, v in table[h(key)]:
        if k == key:
            return v
    return None


def delete(key):
    chain = table[h(key)]
    for i in range(len(chain)):
        if chain[i][0] == key:
            chain.pop(i)
            return True
    return False


def display():
    for i in range(SIZE):
        print(i, "->", " -> ".join(f"({k},{v})" for k, v in table[i]) or "None")


while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        k = int(input("Key: "))
        v = input("Value: ")
        insert(k, v)
        print(f"Inserted at index {h(k)}")
    elif ch == 2:
        k = int(input("Key: "))
        v = search(k)
        print(f"Value = {v}" if v is not None else "Key not found")
    elif ch == 3:
        k = int(input("Key: "))
        print("Deleted" if delete(k) else "Key not found")
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
