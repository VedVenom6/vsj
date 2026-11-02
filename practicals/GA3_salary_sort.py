# GA3: Sort employee salaries (float) with Selection sort and Bubble sort, show top 5

def selection_sort(a):
    a = a[:]                                  # work on a copy
    n = len(a)
    for i in range(n - 1):
        mn = i
        for j in range(i + 1, n):             # find smallest in unsorted part
            if a[j] < a[mn]:
                mn = j
        a[i], a[mn] = a[mn], a[i]             # put it at position i
    return a                                  # Time O(n^2), Space O(1)


def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):            # largest bubbles to the end
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                       # already sorted -> stop early
            break
    return a                                  # Time O(n^2), best O(n)


def top_five(sorted_list):
    top = []
    for i in range(len(sorted_list) - 1, -1, -1):   # walk from the end
        top.append(sorted_list[i])
        if len(top) == 5:
            break
    return top


salaries = list(map(float, input("Enter salaries separated by space: ").split()))

while True:
    print("\n1.Selection Sort  2.Bubble Sort  3.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        s = selection_sort(salaries)
    elif ch == 2:
        s = bubble_sort(salaries)
    elif ch == 3:
        break
    else:
        print("Invalid choice")
        continue
    print("Sorted (ascending):", s)
    print("Top 5 salaries    :", top_five(s))
