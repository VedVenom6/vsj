# GC8: Fixed-size hash table, division method, collisions by linear probing
# EMPTY = never used, DELETED = was used then deleted (so search keeps probing past it)

EMPTY = None
DELETED = "DEL"

size = int(input("Table size: "))
table = [EMPTY] * size


def h(key):
    return key % size


def insert(key):
    if search(key) != -1:
        print("Key already present")
        return
    i = h(key)
    for step in range(size):
        j = (i + step) % size                  # (h(k) + i) % size
        if table[j] is EMPTY or table[j] == DELETED:
            table[j] = key
            print(f"Inserted {key} at index {j}" + (f" (after {step} probes)" if step else ""))
            return
    print("Table full, cannot insert")


def search(key):
    i = h(key)
    for step in range(size):
        j = (i + step) % size
        if table[j] is EMPTY:                  # empty slot -> key can't be further
            return -1
        if table[j] == key:
            return j
    return -1


def delete(key):
    j = search(key)
    if j == -1:
        return False
    table[j] = DELETED                         # mark, don't empty
    return True


def display():
    for i in range(size):
        print(i, ":", "-" if table[i] is EMPTY else table[i])


while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        insert(int(input("Key: ")))
    elif ch == 2:
        j = search(int(input("Key: ")))
        print(f"Found at index {j}" if j != -1 else "Key not found")
    elif ch == 3:
        print("Deleted" if delete(int(input("Key: "))) else "Key not found")
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
