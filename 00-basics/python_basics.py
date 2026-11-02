# Python basics you need for every DS practical
# Run it: python3 python_basics.py   (no input needed - the input() lines are shown in comments)

# ---------- 1. Input patterns (the ones practicals use) ----------
# n = int(input("Enter n: "))                              # one integer
# x = float(input("Enter salary: "))                       # one float
# name = input("Name: ")                                   # one string
# a = list(map(int, input("Numbers: ").split()))           # many ints on one line -> list
# s = list(map(float, input("Salaries: ").split()))        # many floats on one line
# u, v = input("Edge (A B): ").split()                     # two strings on one line
# a = [int(input(f"Element {i+1}: ")) for i in range(n)]   # n ints, one per line

# ---------- 2. Variables and types ----------
year = 2
cgpa = 8.6
name = "Riya"
passed = True
print(type(year), type(cgpa), type(name), type(passed))
print(f"{name}, year {year}, CGPA {cgpa}")                 # f-string formatting
print(7 // 2, 7 % 2, 7 / 2, 2 ** 5)                        # floor div, mod, true div, power

# ---------- 3. Conditions ----------
marks = 72
if marks >= 75:
    grade = "Distinction"
elif marks >= 60:
    grade = "First class"
else:
    grade = "Pass"
print("Grade:", grade)

# ---------- 4. Loops ----------
for i in range(5):                 # 0 1 2 3 4
    print(i, end=" ")
print()
for i in range(10, 0, -3):         # 10 7 4 1 (start, stop, step)
    print(i, end=" ")
print()
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue                   # skip rest of this iteration
    print("while", i)

# ---------- 5. Lists (Python's array) ----------
a = [40, 10, 30, 20]
a.append(50)                       # add at end            O(1)
a.insert(0, 5)                     # add at index          O(n)
a.remove(30)                       # remove by value       O(n)
last = a.pop()                     # remove last           O(1)
first = a.pop(0)                   # remove first          O(n)
print(a, last, first, len(a))
print(a[0], a[-1], a[1:3], a[::-1])   # index, last, slice, reversed
b = a[:]                           # COPY (b = a would share the same list)
b.sort()                           # in-place sort
print("sorted copy:", b, "original:", a, "sorted():", sorted(a, reverse=True))
a[0], a[1] = a[1], a[0]            # swap - used in every sorting program
print("after swap:", a)

# 2D list (matrix) - ALWAYS build it like this, not [[0]*n]*n
rows, cols = 2, 3
m = [[0] * cols for _ in range(rows)]
m[0][1] = 5
print(m)

# list comprehension
squares = [x * x for x in range(6)]
evens = [x for x in squares if x % 2 == 0]
print(squares, evens)

# ---------- 6. Dictionary (key -> value), used in hashing / graphs / counting ----------
freq = {}
for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1   # count occurrences
print(freq)
graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
for node in graph:
    print(node, "->", graph[node])
print("B" in graph, graph.keys(), graph.values())

# ---------- 7. Functions ----------
def find_max(arr):
    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x
    return mx


def stats(arr):                    # returning more than one value
    return min(arr), max(arr), sum(arr) / len(arr)


print("max:", find_max([3, 9, 2]))
lo, hi, avg = stats([3, 9, 2])
print(lo, hi, avg)


# ---------- 8. Recursion (needed for trees, DFS, quick/merge sort) ----------
def factorial(n):
    if n <= 1:                     # base case
        return 1
    return n * factorial(n - 1)    # recursive case


def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(factorial(5), [fib(i) for i in range(8)])


# ---------- 9. Classes (needed for Node, Stack, Queue, LinkedList, BST) ----------
class Student:
    def __init__(self, roll, name, marks):   # constructor
        self.roll = roll
        self.name = name
        self.marks = marks

    def show(self):
        print(f"{self.roll} {self.name} {self.marks}")


class Node:                        # the building block of linked lists and trees
    def __init__(self, data):
        self.data = data
        self.next = None


s1 = Student(1, "Riya", 88)
s1.show()
n1, n2 = Node(10), Node(20)
n1.next = n2                       # link two nodes
print(n1.data, "->", n1.next.data)

# ---------- 10. Menu-driven program skeleton (every practical uses this) ----------
# while True:
#     print("\n1.Insert  2.Delete  3.Display  4.Exit")
#     ch = int(input("Choice: "))
#     if ch == 1:
#         ...
#     elif ch == 4:
#         break
#     else:
#         print("Invalid choice")
