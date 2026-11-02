# GA2: Customer account IDs - Linear search and Binary search

def linear_search(ids, key):
    for i in range(len(ids)):        # check every element one by one
        if ids[i] == key:
            return i
    return -1                        # Time O(n)


def binary_search(ids, key):         # list MUST be sorted
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == key:
            return mid
        elif key < ids[mid]:
            high = mid - 1           # search left half
        else:
            low = mid + 1            # search right half
    return -1                        # Time O(log n)


def binary_search_rec(ids, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if ids[mid] == key:
        return mid
    if key < ids[mid]:
        return binary_search_rec(ids, key, low, mid - 1)
    return binary_search_rec(ids, key, mid + 1, high)


ids = list(map(int, input("Enter customer IDs separated by space: ").split()))

while True:
    print("\n1.Linear Search  2.Binary Search  3.Binary Search (recursive)  4.Display  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        key = int(input("ID to search: "))
        pos = linear_search(ids, key)
        print(f"Found at index {pos}" if pos != -1 else "ID not found")
    elif ch in (2, 3):
        key = int(input("ID to search: "))
        s = sorted(ids)
        print("Sorted IDs:", s)
        if ch == 2:
            pos = binary_search(s, key)
        else:
            pos = binary_search_rec(s, key, 0, len(s) - 1)
        print(f"Found at index {pos} of sorted list" if pos != -1 else "ID not found")
    elif ch == 4:
        print("Customer IDs:", ids)
    elif ch == 5:
        break
    else:
        print("Invalid choice")
