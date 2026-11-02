# Unit II: Searching - Linear, Sentinel, Binary, Fibonacci, Indexed Sequential

def linear_search(a, key):                  # O(n)
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


def sentinel_search(a, key):                # one comparison per step instead of two
    n = len(a)
    last = a[n - 1]
    a[n - 1] = key                          # put key at end as sentinel
    i = 0
    while a[i] != key:
        i += 1
    a[n - 1] = last                         # restore
    if i < n - 1 or last == key:
        return i
    return -1


def binary_search(a, key):                  # sorted list, O(log n)
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def fibonacci_search(a, key):               # sorted list, splits using Fibonacci numbers, O(log n)
    n = len(a)
    f2, f1 = 0, 1                           # F(k-2), F(k-1)
    f = f1 + f2                             # F(k)
    while f < n:
        f2, f1 = f1, f
        f = f1 + f2
    offset = -1
    while f > 1:
        i = min(offset + f2, n - 1)
        if a[i] < key:                      # go right: drop one Fibonacci step
            f, f1 = f1, f2
            f2 = f - f1
            offset = i
        elif a[i] > key:                    # go left: drop two Fibonacci steps
            f = f2
            f1 = f1 - f2
            f2 = f - f1
        else:
            return i
    if f1 and offset + 1 < n and a[offset + 1] == key:
        return offset + 1
    return -1


def indexed_sequential_search(a, key, block=3):   # sorted list
    index = [(a[i], i) for i in range(0, len(a), block)]   # first key of each block
    start = 0
    for k, pos in index:
        if k > key:
            break
        start = pos
    for i in range(start, min(start + block, len(a))):    # search inside that block only
        if a[i] == key:
            return i
    return -1


data = [12, 4, 56, 23, 89, 45, 7]
s = sorted(data)
print("Unsorted:", data, " Sorted:", s)
for key in (45, 100):
    print(f"key {key}: linear={linear_search(data, key)} sentinel={sentinel_search(data, key)} "
          f"binary={binary_search(s, key)} fibonacci={fibonacci_search(s, key)} "
          f"indexed={indexed_sequential_search(s, key)}")
for key in s:                                         # every element must be found
    assert fibonacci_search(s, key) == s.index(key)
    assert indexed_sequential_search(s, key) == s.index(key)
print("All searches agree on every element.")
