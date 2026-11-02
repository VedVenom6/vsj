# Unit II: Sorting - Bubble, Selection, Insertion, Quick, Merge (with pass counts)
#
# Algorithm   Best        Average     Worst       Stable  In-place
# Bubble      O(n)        O(n^2)      O(n^2)      Yes     Yes
# Selection   O(n^2)      O(n^2)      O(n^2)      No      Yes
# Insertion   O(n)        O(n^2)      O(n^2)      Yes     Yes
# Quick       O(n log n)  O(n log n)  O(n^2)      No      Yes
# Merge       O(n log n)  O(n log n)  O(n log n)  Yes     No (O(n) extra)

def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        print(f"  pass {i + 1}: {a}")
        if not swapped:
            break
    return a


def selection_sort(a):
    a = a[:]
    for i in range(len(a) - 1):
        mn = i
        for j in range(i + 1, len(a)):
            if a[j] < a[mn]:
                mn = j
        a[i], a[mn] = a[mn], a[i]
        print(f"  pass {i + 1}: {a}")
    return a


def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:        # shift bigger elements right
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"  pass {i}: {a}")
    return a


def partition(a, low, high):                # last element as pivot (Lomuto)
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)         # pivot is now in its final place
        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]


data = [29, 10, 14, 37, 13]
print("Input:", data)
print("Bubble:");    bubble_sort(data)
print("Selection:"); selection_sort(data)
print("Insertion:"); insertion_sort(data)
q = data[:]
quick_sort(q, 0, len(q) - 1)
print("Quick :", q)
print("Merge :", merge_sort(data))
# Internal sort: data fits in RAM. External sort: data on disk, sorted in chunks then merged.
