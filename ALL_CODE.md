# All DS Python code in one file

Practicals first, then basics and each syllabus unit. Copy a block into a `.py` file and run `python3 file.py`.

## Index

**Practical exam programs**

- [GA1 – Library borrowing records](#ga1--library-borrowing-records)
- [GA2 – Customer ID linear and binary search](#ga2--customer-id-linear-and-binary-search)
- [GA3 – Salary selection and bubble sort, top 5](#ga3--salary-selection-and-bubble-sort-top-5)
- [GB4 – Undo/redo with stacks](#gb4--undoredo-with-stacks)
- [GB5 – Event processing queue](#gb5--event-processing-queue)
- [GB6 – Student records with a linked list](#gb6--student-records-with-a-linked-list)
- [GC7 – Hash table with chaining](#gc7--hash-table-with-chaining)
- [GC8 – Hash table with linear probing](#gc8--hash-table-with-linear-probing)
- [GD9 – City graph BFS and DFS](#gd9--city-graph-bfs-and-dfs)
- [GD10 – Binary search tree](#gd10--binary-search-tree)

**Python basics**

- [Python basics for DS](#python-basics-for-ds)

**Unit I – Complexity, divide and conquer, greedy**

- [Step count method](#step-count-method)
- [Divide and conquer – product sorting](#divide-and-conquer--product-sorting)
- [Greedy – calendar scheduling](#greedy--calendar-scheduling)

**Unit II – Arrays, searching, sorting**

- [Arrays and matrices](#arrays-and-matrices)
- [Searching](#searching)
- [Sorting](#sorting)

**Unit III – Stacks, queues, linked lists**

- [Stack and expressions](#stack-and-expressions)
- [Queues](#queues)
- [Call center queue (lab B3)](#call-center-queue-lab-b3)
- [Linked lists (singly, doubly, circular)](#linked-lists-singly-doubly-circular)
- [Stack and queue using a linked list](#stack-and-queue-using-a-linked-list)

**Unit IV – Hashing**

- [Extendible hashing (lab C3)](#extendible-hashing-lab-c3)
- [Dictionary with hashing and rehashing](#dictionary-with-hashing-and-rehashing)

**Unit V – Graphs and trees**

- [Prim, Kruskal, Dijkstra (lab D2)](#prim-kruskal-dijkstra-lab-d2)
- [Binary tree traversals](#binary-tree-traversals)
- [Expression tree from prefix (lab D4)](#expression-tree-from-prefix-lab-d4)
- [City population BST (lab D5)](#city-population-bst-lab-d5)
- [Propositional formula tree (lab D6)](#propositional-formula-tree-lab-d6)
- [Huffman coding](#huffman-coding)

---

# Practical exam programs

## GA1 – Library borrowing records
File: `practicals/GA1_library_borrowing.py`

```python
# GA1: Library borrowing records
# Average, highest/lowest, members with 0 borrows, mode (most frequent borrow count)
# Every operation is written with plain loops (no max/min/sum) so you can explain it.

def average(counts):
    total = 0
    for c in counts:                 # one pass over n members
        total += c
    return total / len(counts)       # Time O(n), Space O(1)


def highest_lowest(names, counts):
    hi = lo = 0                      # index of highest and lowest so far
    for i in range(1, len(counts)):
        if counts[i] > counts[hi]:
            hi = i
        if counts[i] < counts[lo]:
            lo = i
    return names[hi], counts[hi], names[lo], counts[lo]   # Time O(n), Space O(1)


def count_zero(counts):
    zero = 0
    for c in counts:
        if c == 0:
            zero += 1
    return zero                      # Time O(n), Space O(1)


def mode(counts):
    freq = {}                        # borrow count -> how many times it appears
    for c in counts:
        freq[c] = freq.get(c, 0) + 1
    best = counts[0]
    for c in freq:
        if freq[c] > freq[best]:
            best = c
    return best, freq[best]          # Time O(n), Space O(k), k = distinct counts


n = int(input("Number of members: "))
names = []
counts = []
for i in range(n):
    name = input(f"Member {i + 1} name: ")
    c = int(input(f"Books borrowed by {name}: "))
    names.append(name)
    counts.append(c)

while True:
    print("\n1.Average  2.Highest & Lowest  3.Members with 0 books  4.Mode  5.Complexity  6.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        print("Average books borrowed =", round(average(counts), 2))
    elif ch == 2:
        hn, hc, ln, lc = highest_lowest(names, counts)
        print(f"Highest: {hn} ({hc} books)   Lowest: {ln} ({lc} books)")
    elif ch == 3:
        print("Members who borrowed 0 books =", count_zero(counts))
    elif ch == 4:
        m, f = mode(counts)
        print(f"Most frequent borrow count = {m} (appears {f} times)")
    elif ch == 5:
        print("Average        : Time O(n)  Space O(1)")
        print("Highest/Lowest : Time O(n)  Space O(1)")
        print("Count zero     : Time O(n)  Space O(1)")
        print("Mode           : Time O(n)  Space O(k)  (dictionary of k distinct counts)")
    elif ch == 6:
        break
    else:
        print("Invalid choice")
```

## GA2 – Customer ID linear and binary search
File: `practicals/GA2_customer_search.py`

```python
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
```

## GA3 – Salary selection and bubble sort, top 5
File: `practicals/GA3_salary_sort.py`

```python
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
```

## GB4 – Undo/redo with stacks
File: `practicals/GB4_undo_redo_stack.py`

```python
# GB4: Undo / Redo for a text editor using two stacks

undo_stack = []      # every change made, latest on top
redo_stack = []      # changes that were undone, latest on top


def make_change(text):
    undo_stack.append(text)          # push
    redo_stack.clear()               # a new change kills the redo history
    print("Change added:", text)


def undo():
    if not undo_stack:
        print("Nothing to undo")
        return
    change = undo_stack.pop()        # pop latest change
    redo_stack.append(change)        # keep it for redo
    print("Undone:", change)


def redo():
    if not redo_stack:
        print("Nothing to redo")
        return
    change = redo_stack.pop()
    undo_stack.append(change)
    print("Redone:", change)


def display():
    print("Document:", " ".join(undo_stack) if undo_stack else "(empty)")
    print("Undo stack:", undo_stack)
    print("Redo stack:", redo_stack)


while True:
    print("\n1.Make Change  2.Undo  3.Redo  4.Display Document  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        make_change(input("Enter text: "))
    elif ch == 2:
        undo()
        display()
    elif ch == 3:
        redo()
        display()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
```

## GB5 – Event processing queue
File: `practicals/GB5_event_queue.py`

```python
# GB5: Real-time event processing using a Queue (FIFO)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, x):            # add at rear
        self.items.append(x)

    def dequeue(self):               # remove from front (oldest)
        return self.items.pop(0)

    def remove(self, x):             # cancel an unprocessed event
        if x in self.items:
            self.items.remove(x)
            return True
        return False


q = Queue()

while True:
    print("\n1.Add Event  2.Process Next Event  3.Display Pending  4.Cancel Event  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        e = input("Event name: ")
        q.enqueue(e)
        print("Added:", e)
    elif ch == 2:
        if q.is_empty():
            print("No events to process")
        else:
            print("Processed:", q.dequeue())
    elif ch == 3:
        print("Pending events (front -> rear):", q.items if not q.is_empty() else "none")
    elif ch == 4:
        e = input("Event to cancel: ")
        print("Cancelled:", e if q.remove(e) else "event not found / already processed")
    elif ch == 5:
        break
    else:
        print("Invalid choice")
```

## GB6 – Student records with a linked list
File: `practicals/GB6_student_linked_list.py`

```python
# GB6: Student Record Management System using a Singly Linked List
# Node stores Roll No, Name, Marks. Add, Delete, Update, Search, Sort, Display asc/desc.

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                return temp
            temp = temp.next
        return None

    def add(self, roll, name, marks):           # insert at end
        if self.search(roll):
            print("Roll number already exists")
            return
        new = Node(roll, name, marks)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, roll):
        if self.head is None:
            return False
        if self.head.roll == roll:              # deleting the first node
            self.head = self.head.next
            return True
        prev = self.head
        while prev.next and prev.next.roll != roll:
            prev = prev.next
        if prev.next is None:
            return False
        prev.next = prev.next.next              # unlink the node
        return True

    def update(self, roll, name, marks):
        node = self.search(roll)
        if node:
            node.name = name
            node.marks = marks
            return True
        return False

    def sort(self, key, descending=False):     # bubble sort by swapping node data
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                a = getattr(temp, key)
                b = getattr(temp.next, key)
                if (a > b and not descending) or (a < b and descending):
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next

    def display(self):
        if self.head is None:
            print("No records")
            return
        print(f"{'Roll':<6}{'Name':<15}{'Marks':<6}")
        temp = self.head
        while temp:
            print(f"{temp.roll:<6}{temp.name:<15}{temp.marks:<6}")
            temp = temp.next


s = StudentList()

while True:
    print("\n1.Add  2.Delete  3.Update  4.Search  5.Sort & Display  6.Display  7.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        r = int(input("Roll No: "))
        n = input("Name: ")
        m = float(input("Marks: "))
        s.add(r, n, m)
    elif ch == 2:
        r = int(input("Roll No to delete: "))
        print("Deleted" if s.delete(r) else "Not found")
    elif ch == 3:
        r = int(input("Roll No to update: "))
        n = input("New name: ")
        m = float(input("New marks: "))
        print("Updated" if s.update(r, n, m) else "Not found")
    elif ch == 4:
        node = s.search(int(input("Roll No to search: ")))
        print(f"Found: {node.roll} {node.name} {node.marks}" if node else "Not found")
    elif ch == 5:
        k = input("Sort by (roll/marks): ").strip()
        if k not in ("roll", "marks"):
            print("Type roll or marks")
            continue
        order = input("Order (asc/desc): ").strip()
        s.sort(k, order == "desc")
        s.display()
    elif ch == 6:
        s.display()
    elif ch == 7:
        break
    else:
        print("Invalid choice")
```

## GC7 – Hash table with chaining
File: `practicals/GC7_hash_chaining.py`

```python
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
```

## GC8 – Hash table with linear probing
File: `practicals/GC8_hash_linear_probing.py`

```python
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
```

## GD9 – City graph BFS and DFS
File: `practicals/GD9_graph_bfs_dfs.py`

```python
# GD9: City locations as a graph
# DFS using an ADJACENCY MATRIX, BFS using an ADJACENCY LIST (as the question asks)

n = int(input("Number of locations: "))
names = input("Location names separated by space (e.g. A B C D): ").split()
index = {names[i]: i for i in range(n)}

matrix = [[0] * n for _ in range(n)]       # for DFS
adj = {name: [] for name in names}        # for BFS

e = int(input("Number of routes: "))
for _ in range(e):
    u, v = input("Route (e.g. A B): ").split()
    matrix[index[u]][index[v]] = matrix[index[v]][index[u]] = 1   # undirected
    adj[u].append(v)
    adj[v].append(u)


def dfs(i, visited, order):                # recursive DFS on the matrix
    visited[i] = True
    order.append(names[i])
    for j in range(n):
        if matrix[i][j] == 1 and not visited[j]:
            dfs(j, visited, order)


def bfs(start):                            # BFS with a queue on the list
    visited = [start]
    queue = [start]
    order = []
    while queue:
        node = queue.pop(0)                # dequeue
        order.append(node)
        for nb in adj[node]:
            if nb not in visited:
                visited.append(nb)
                queue.append(nb)           # enqueue
    return order


while True:
    print("\n1.Show Matrix  2.Show List  3.DFS  4.BFS  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        print("   " + "  ".join(names))
        for i in range(n):
            print(names[i], " ", "  ".join(map(str, matrix[i])))
    elif ch == 2:
        for k in adj:
            print(k, "->", adj[k])
    elif ch == 3:
        s = input("Start location: ")
        order = []
        dfs(index[s], [False] * n, order)
        print("DFS:", " -> ".join(order))
    elif ch == 4:
        s = input("Start location: ")
        print("BFS:", " -> ".join(bfs(s)))
    elif ch == 5:
        break
    else:
        print("Invalid choice")
```

## GD10 – Binary search tree
File: `practicals/GD10_bst.py`

```python
# GD10: Binary Search Tree - insert, delete, search, display (inorder/preorder/postorder)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    else:
        print("Duplicate key ignored")
    return root


def search(root, key):
    while root:
        if key == root.data:
            return True
        root = root.left if key < root.data else root.right
    return False


def min_node(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        print("Key not found")
        return None
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:              # case 1 & 2: no child / only right child
            return root.right
        if root.right is None:             # case 2: only left child
            return root.left
        succ = min_node(root.right)        # case 3: two children -> inorder successor
        root.data = succ.data
        root.right = delete(root.right, succ.data)
    return root


def inorder(root):                         # gives sorted order
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

while True:
    print("\n1.Insert  2.Delete  3.Search  4.Display  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        for k in map(int, input("Keys separated by space: ").split()):
            root = insert(root, k)
    elif ch == 2:
        root = delete(root, int(input("Key to delete: ")))
    elif ch == 3:
        print("Found" if search(root, int(input("Key to search: "))) else "Not found")
    elif ch == 4:
        if root is None:
            print("Tree is empty")
            continue
        print("Inorder  : ", end=""); inorder(root); print()
        print("Preorder : ", end=""); preorder(root); print()
        print("Postorder: ", end=""); postorder(root); print()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
```

# Python basics

## Python basics for DS
File: `00-basics/python_basics.py`

```python
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
```

# Unit I – Complexity, divide and conquer, greedy

## Step count method
File: `unit1-complexity/complexity_step_count.py`

```python
# Unit I: Step count method - count how many times the basic operation runs
# Linear O(n), Quadratic O(n^2), Cubic O(n^3), Logarithmic O(log n)

def linear(n):
    steps = 0
    for i in range(n):
        steps += 1
    return steps


def quadratic(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps


def cubic(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                steps += 1
    return steps


def logarithmic(n):
    steps = 0
    i = n
    while i > 1:            # i halves each time -> log2(n) iterations
        i //= 2
        steps += 1
    return steps


print(f"{'n':>5}{'log n':>8}{'n':>8}{'n^2':>10}{'n^3':>12}")
for n in (8, 16, 32, 64):
    print(f"{n:>5}{logarithmic(n):>8}{linear(n):>8}{quadratic(n):>10}{cubic(n):>12}")

# Step count for sum of array:
#   total = 0                1
#   for x in arr:            n + 1
#       total += x           n
#   return total             1
#   ---------------------------------
#   T(n) = 2n + 3  ->  O(n)
#
# Big-O = upper bound (worst case), Omega = lower bound (best case),
# Theta = tight bound (upper and lower are the same order).
```

## Divide and conquer – product sorting
File: `unit1-complexity/divide_conquer_product_sort.py`

```python
# Unit I case study: E-commerce product sorting using Divide and Conquer (Merge sort)
# Divide the list in half, sort each half recursively, then merge.  T(n) = 2T(n/2) + n = O(n log n)

def merge_sort(products, key):
    if len(products) <= 1:                       # base case
        return products
    mid = len(products) // 2
    left = merge_sort(products[:mid], key)       # divide + conquer
    right = merge_sort(products[mid:], key)
    return merge(left, right, key)               # combine


def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:        # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


products = [
    {"name": "Laptop", "price": 55000, "rating": 4.4},
    {"name": "Mouse", "price": 700, "rating": 4.1},
    {"name": "Phone", "price": 18000, "rating": 4.6},
    {"name": "Earbuds", "price": 1500, "rating": 3.9},
    {"name": "Monitor", "price": 12000, "rating": 4.3},
]

print("By price (low to high):")
for p in merge_sort(products, "price"):
    print(f"  {p['name']:<8} Rs {p['price']}")

print("By rating (high to low):")
for p in reversed(merge_sort(products, "rating")):
    print(f"  {p['name']:<8} {p['rating']}")
```

## Greedy – calendar scheduling
File: `unit1-complexity/greedy_calendar.py`

```python
# Unit I case study: Google Calendar style scheduling using the Greedy strategy
# Activity selection: fit the MAXIMUM number of non-overlapping meetings.
# Greedy choice: always pick the meeting that ENDS earliest.  Time O(n log n) for the sort.

meetings = [
    ("Standup", 9, 10),
    ("Design review", 9, 12),
    ("Lunch", 12, 13),
    ("Client call", 10, 11),
    ("Lab", 11, 14),
    ("Code review", 13, 15),
    ("1:1", 15, 16),
]

meetings.sort(key=lambda m: m[2])        # sort by end time

chosen = []
last_end = 0
for name, start, end in meetings:
    if start >= last_end:                # doesn't overlap the last chosen meeting
        chosen.append((name, start, end))
        last_end = end

print("Selected meetings:")
for name, s, e in chosen:
    print(f"  {s:>2}:00 - {e:>2}:00  {name}")
print("Total:", len(chosen))
```

# Unit II – Arrays, searching, sorting

## Arrays and matrices
File: `unit2-arrays-search-sort/arrays_matrices.py`

```python
# Unit II: Array as an ADT, 2D matrices, sparse matrix, adjacency matrix case study

# ---------- Array ADT operations ----------
def traverse(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()


def insert_at(a, pos, x):        # shift right, O(n)
    a.append(None)
    for i in range(len(a) - 1, pos, -1):
        a[i] = a[i - 1]
    a[pos] = x


def delete_at(a, pos):           # shift left, O(n)
    x = a[pos]
    for i in range(pos, len(a) - 1):
        a[i] = a[i + 1]
    a.pop()
    return x


arr = [10, 20, 30, 40]
insert_at(arr, 1, 15)
print("After insert 15 at 1:", arr)
print("Deleted:", delete_at(arr, 3), "->", arr)
traverse(arr)

# Storage representation (row-major), base address B, element size w, n columns:
#   address(A[i][j]) = B + (i * n + j) * w
# Column-major, m rows:  address(A[i][j]) = B + (j * m + i) * w
B, w, m, n = 1000, 4, 3, 4
print("Row-major A[2][1]    =", B + (2 * n + 1) * w)
print("Column-major A[2][1] =", B + (1 * m + 2) * w)


# ---------- 2D matrix operations ----------
def add(A, Bm):
    return [[A[i][j] + Bm[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def multiply(A, Bm):             # O(n^3)
    r, c, k = len(A), len(Bm[0]), len(Bm)
    C = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for x in range(k):
                C[i][j] += A[i][x] * Bm[x][j]
    return C


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


A = [[1, 2], [3, 4]]
Bm = [[5, 6], [7, 8]]
print("A+B =", add(A, Bm), " AxB =", multiply(A, Bm), " A^T =", transpose(A))


# ---------- Sparse matrix (triplet form: row, col, value) ----------
def to_triplet(M):
    t = [(len(M), len(M[0]), 0)]             # header: rows, cols, count of non-zeros
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 0:
                t.append((i, j, M[i][j]))
    t[0] = (len(M), len(M[0]), len(t) - 1)
    return t


def sparse_transpose(t):                     # simple transpose: swap row and col, then sort
    rows, cols, cnt = t[0]
    body = sorted((c, r, v) for r, c, v in t[1:])
    return [(cols, rows, cnt)] + body


S = [[0, 0, 3, 0],
     [0, 0, 0, 0],
     [5, 0, 0, 7],
     [0, 2, 0, 0]]
trip = to_triplet(S)
print("Triplet  :", trip)
print("Transpose:", sparse_transpose(trip))

# ---------- Case study: social network as an adjacency matrix ----------
users = ["Asha", "Ben", "Chen", "Dev"]
friends = [("Asha", "Ben"), ("Asha", "Chen"), ("Chen", "Dev")]
idx = {u: i for i, u in enumerate(users)}
adj = [[0] * len(users) for _ in users]
for a, b in friends:
    adj[idx[a]][idx[b]] = adj[idx[b]][idx[a]] = 1
for i, u in enumerate(users):
    print(f"{u:<5}", adj[i], "friends:", sum(adj[i]))
# For millions of users a matrix needs n^2 cells and is mostly zeros -> use adjacency lists.
```

## Searching
File: `unit2-arrays-search-sort/searching.py`

```python
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
```

## Sorting
File: `unit2-arrays-search-sort/sorting.py`

```python
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
```

# Unit III – Stacks, queues, linked lists

## Stack and expressions
File: `unit3-stack-queue-linkedlist/stack_expressions.py`

```python
# Unit III: Stack, multiple stacks, infix -> postfix / prefix, postfix evaluation

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


# ---------- Two stacks in one array (multiple stacks) ----------
class TwoStacks:
    def __init__(self, size):
        self.arr = [None] * size
        self.top1, self.top2 = -1, size      # stack 1 grows right, stack 2 grows left

    def push1(self, x):
        if self.top1 + 1 == self.top2:
            print("Overflow"); return
        self.top1 += 1
        self.arr[self.top1] = x

    def push2(self, x):
        if self.top2 - 1 == self.top1:
            print("Overflow"); return
        self.top2 -= 1
        self.arr[self.top2] = x

    def pop1(self):
        x = self.arr[self.top1]; self.top1 -= 1; return x

    def pop2(self):
        x = self.arr[self.top2]; self.top2 += 1; return x


# ---------- Expression conversion ----------
PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_to_postfix(exp):
    st = Stack()
    out = ""
    for ch in exp:
        if ch.isalnum():                     # operand goes straight to output
            out += ch
        elif ch == "(":
            st.push(ch)
        elif ch == ")":
            while st.peek() != "(":
                out += st.pop()
            st.pop()                         # discard "("
        else:                                # operator
            while (not st.is_empty() and st.peek() != "(" and
                   (PREC[st.peek()] > PREC[ch] or
                    (PREC[st.peek()] == PREC[ch] and ch != "^"))):   # ^ is right-associative
                out += st.pop()
            st.push(ch)
    while not st.is_empty():
        out += st.pop()
    return out


def infix_to_prefix(exp):
    # reverse, swap brackets, convert to postfix (^ handled as left-assoc here), reverse again
    rev = ""
    for ch in exp[::-1]:
        rev += "(" if ch == ")" else ")" if ch == "(" else ch
    st = Stack()
    out = ""
    for ch in rev:
        if ch.isalnum():
            out += ch
        elif ch == "(":
            st.push(ch)
        elif ch == ")":
            while st.peek() != "(":
                out += st.pop()
            st.pop()
        else:
            while (not st.is_empty() and st.peek() != "(" and
                   (PREC[st.peek()] > PREC[ch] or (PREC[st.peek()] == PREC[ch] and ch == "^"))):
                out += st.pop()
            st.push(ch)
    while not st.is_empty():
        out += st.pop()
    return out[::-1]


def evaluate_postfix(exp):                    # space-separated tokens, e.g. "5 3 + 2 *"
    st = Stack()
    for tok in exp.split():
        if tok.lstrip("-").isdigit():
            st.push(int(tok))
        else:
            b, a = st.pop(), st.pop()        # second operand is popped first
            if tok == "+": st.push(a + b)
            elif tok == "-": st.push(a - b)
            elif tok == "*": st.push(a * b)
            elif tok == "/": st.push(a / b)
            elif tok == "^": st.push(a ** b)
    return st.pop()


for e in ("A+B*C", "(A+B)*C", "A+B*(C^D-E)", "A^B^C"):
    print(f"{e:<14} postfix: {infix_to_postfix(e):<12} prefix: {infix_to_prefix(e)}")
print("5 3 + 2 * =", evaluate_postfix("5 3 + 2 *"))
print("6 2 / 3 4 * + =", evaluate_postfix("6 2 / 3 4 * +"))

ts = TwoStacks(5)
ts.push1(1); ts.push1(2); ts.push2(9); ts.push2(8)
print("TwoStacks array:", ts.arr, " pop1:", ts.pop1(), " pop2:", ts.pop2())
```

## Queues
File: `unit3-stack-queue-linkedlist/queues.py`

```python
# Unit III: Linear queue, Circular queue, Priority queue

# ---------- Linear queue (array with front and rear) ----------
class LinearQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue full")              # can be "full" even with free space at front
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.q[self.rear] = x

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue empty")
            return None
        x = self.q[self.front]
        self.front += 1
        return x


# ---------- Circular queue (fixes the wasted space) ----------
class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, x):
        if self.is_full():
            print("Queue full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size      # wrap around
        self.q[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("Queue empty")
            return None
        x = self.q[self.front]
        if self.front == self.rear:                  # last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return x

    def display(self):
        if self.is_empty():
            print("Queue empty"); return
        i, out = self.front, []
        while True:
            out.append(self.q[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("Circular queue:", out)


# ---------- Priority queue (lower number = higher priority) ----------
class PriorityQueue:
    def __init__(self):
        self.items = []                              # kept sorted by priority

    def enqueue(self, x, priority):
        i = 0
        while i < len(self.items) and self.items[i][1] <= priority:   # same priority keeps FIFO
            i += 1
        self.items.insert(i, (x, priority))

    def dequeue(self):
        return self.items.pop(0)[0] if self.items else None


lq = LinearQueue(3)
for x in (1, 2, 3):
    lq.enqueue(x)
print("Linear dequeue:", lq.dequeue())
lq.enqueue(4)                                         # shows the linear queue problem

cq = CircularQueue(3)
for x in (1, 2, 3):
    cq.enqueue(x)
print("Circular dequeue:", cq.dequeue())
cq.enqueue(4)                                         # reuses the freed slot
cq.display()

pq = PriorityQueue()
pq.enqueue("normal patient", 3)
pq.enqueue("emergency", 1)
pq.enqueue("checkup", 5)
pq.enqueue("serious", 2)
print("Priority order:", [pq.dequeue() for _ in range(4)])
# Applications: CPU scheduling, Dijkstra / Prim, hospital triage, printer jobs
```

## Call center queue (lab B3)
File: `unit3-stack-queue-linkedlist/call_center_queue.py`

```python
# Lab B3 (syllabus list): Call center call queue
# addCall(customerID, callTime), answerCall(), viewQueue(), isQueueEmpty()

class CallQueue:
    def __init__(self):
        self.calls = []

    def addCall(self, customerID, callTime):
        self.calls.append((customerID, callTime))       # enqueue at rear
        print(f"Call from {customerID} ({callTime} min) added")

    def answerCall(self):
        if self.isQueueEmpty():
            print("No calls waiting")
            return
        cid, t = self.calls.pop(0)                      # dequeue from front
        print(f"Answered call from {cid} ({t} min)")

    def viewQueue(self):
        if self.isQueueEmpty():
            print("Queue is empty")
            return
        for i, (cid, t) in enumerate(self.calls, 1):
            print(f"  {i}. Customer {cid} - {t} min")

    def isQueueEmpty(self):
        return len(self.calls) == 0


cq = CallQueue()
while True:
    print("\n1.Add Call  2.Answer Call  3.View Queue  4.Is Empty?  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        cq.addCall(input("Customer ID: "), int(input("Call time (minutes): ")))
    elif ch == 2:
        cq.answerCall()
    elif ch == 3:
        cq.viewQueue()
    elif ch == 4:
        print("Empty" if cq.isQueueEmpty() else "Not empty")
    elif ch == 5:
        break
    else:
        print("Invalid choice")
```

## Linked lists (singly, doubly, circular)
File: `unit3-stack-queue-linkedlist/linked_lists.py`

```python
# Unit III: Singly, Doubly and Circular linked lists
# Primitive operations: create, traverse, search, insert, delete, sort, concatenate (+ reverse)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, values):
        for v in values:
            self.insert_end(v)

    def traverse(self):
        temp, out = self.head, []
        while temp:
            out.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(out) + " -> None")

    def search(self, key):
        temp, pos = self.head, 0
        while temp:
            if temp.data == key:
                return pos
            temp, pos = temp.next, pos + 1
        return -1

    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_at(self, pos, x):            # pos 0 = beginning
        if pos == 0:
            self.insert_begin(x)
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Position out of range"); return
            temp = temp.next
        if temp is None:
            print("Position out of range"); return
        new = Node(x)
        new.next = temp.next
        temp.next = new

    def delete(self, key):
        if self.head and self.head.data == key:
            self.head = self.head.next
            return True
        prev = self.head
        while prev and prev.next:
            if prev.next.data == key:
                prev.next = prev.next.next
                return True
            prev = prev.next
        return False

    def sort(self):                         # bubble sort by swapping data
        i = self.head
        while i:
            j = i.next
            while j:
                if i.data > j.data:
                    i.data, j.data = j.data, i.data
                j = j.next
            i = i.next

    def concatenate(self, other):
        if self.head is None:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        self.head = prev


# ---------- Doubly linked list ----------
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = DNode(x)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def delete(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            return False
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next           # deleting head
        if temp.next:
            temp.next.prev = temp.prev
        return True

    def display(self):
        temp, fwd, last = self.head, [], None
        while temp:
            fwd.append(str(temp.data))
            last = temp
            temp = temp.next
        back = []
        while last:
            back.append(str(last.data))
            last = last.prev
        print("Forward :", " <-> ".join(fwd))
        print("Backward:", " <-> ".join(back))


# ---------- Circular singly linked list ----------
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            new.next = new                  # points to itself
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    def delete(self, key):
        if self.head is None:
            return False
        cur, prev = self.head, None
        while True:
            if cur.data == key:
                if prev is None:            # deleting head
                    if cur.next == self.head:
                        self.head = None
                        return True
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = cur.next
                    last.next = self.head
                else:
                    prev.next = cur.next
                return True
            prev, cur = cur, cur.next
            if cur == self.head:
                return False

    def display(self):
        if self.head is None:
            print("Empty"); return
        temp, out = self.head, []
        while True:
            out.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(out) + " -> (back to head)")


s = SinglyLinkedList()
s.create([40, 10, 30])
s.insert_begin(5); s.insert_end(50); s.insert_at(2, 25)
s.traverse()
print("search 30 at position", s.search(30))
s.delete(10); s.traverse()
s.sort(); s.traverse()
t = SinglyLinkedList(); t.create([60, 70])
s.concatenate(t); s.traverse()
s.reverse(); s.traverse()

d = DoublyLinkedList()
for x in (1, 2, 3, 4):
    d.insert_end(x)
d.delete(1); d.delete(3)
d.display()

c = CircularLinkedList()
for x in (7, 8, 9):
    c.insert_end(x)
c.delete(7)
c.display()
```

## Stack and queue using a linked list
File: `unit3-stack-queue-linkedlist/stack_queue_using_linked_list.py`

```python
# Unit III case study: Stack and Queue implemented with linked lists (no size limit)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:                  # push/pop at head -> O(1)
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print("Stack underflow")
            return None
        x = self.top.data
        self.top = self.top.next
        return x

    def display(self):
        temp, out = self.top, []
        while temp:
            out.append(temp.data)
            temp = temp.next
        print("Stack (top first):", out)


class LinkedQueue:                  # enqueue at rear, dequeue at front -> both O(1)
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, x):
        new = Node(x)
        if self.rear is None:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue underflow")
            return None
        x = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return x

    def display(self):
        temp, out = self.front, []
        while temp:
            out.append(temp.data)
            temp = temp.next
        print("Queue (front first):", out)


st = LinkedStack()
for x in (1, 2, 3):
    st.push(x)
st.display()
print("popped", st.pop())
st.display()

q = LinkedQueue()
for x in ("a", "b", "c"):
    q.enqueue(x)
q.display()
print("dequeued", q.dequeue())
q.display()
```

# Unit IV – Hashing

## Extendible hashing (lab C3)
File: `unit4-hashing/extendible_hashing.py`

```python
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
```

## Dictionary with hashing and rehashing
File: `unit4-hashing/dictionary_hash.py`

```python
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
```

# Unit V – Graphs and trees

## Prim, Kruskal, Dijkstra (lab D2)
File: `unit5-graphs-trees/mst_and_shortest_path.py`

```python
# Unit V: Minimum Spanning Tree (Prim, Kruskal) and shortest path (Dijkstra)
# Lab D2 (pizza delivery): locations = nodes, travel time = edge weight.
# Prim/Kruskal give the cheapest network of roads that reaches every customer;
# Dijkstra gives the fastest time from the shop to each customer (GPS case study).

INF = float("inf")
places = ["Shop", "A", "B", "C", "D"]
n = len(places)
# undirected weighted edges (u, v, minutes)
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5), (2, 3, 8), (2, 4, 10), (3, 4, 2)]

cost = [[INF] * n for _ in range(n)]           # adjacency (cost) matrix
for u, v, w in edges:
    cost[u][v] = cost[v][u] = w


def prim(start=0):                              # grow one tree, always take the cheapest edge out of it
    in_tree = [False] * n
    key = [INF] * n                             # cheapest edge connecting node to the tree
    parent = [-1] * n
    key[start] = 0
    for _ in range(n):
        u = -1
        for v in range(n):                      # pick the closest node not yet in the tree
            if not in_tree[v] and (u == -1 or key[v] < key[u]):
                u = v
        in_tree[u] = True
        for v in range(n):                      # update neighbours
            if not in_tree[v] and cost[u][v] < key[v]:
                key[v] = cost[u][v]
                parent[v] = u
    total = 0
    print("Prim MST:")
    for v in range(n):
        if parent[v] != -1:
            print(f"  {places[parent[v]]} - {places[v]} : {cost[v][parent[v]]}")
            total += cost[v][parent[v]]
    print("  Total =", total)                   # O(V^2) with a matrix


def find(parent, x):                            # union-find: root of x's set
    while parent[x] != x:
        x = parent[x]
    return x


def kruskal():                                  # sort all edges, add if it doesn't make a cycle
    parent = list(range(n))
    total = 0
    print("Kruskal MST:")
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(parent, u), find(parent, v)
        if ru != rv:                            # different sets -> no cycle
            parent[ru] = rv
            total += w
            print(f"  {places[u]} - {places[v]} : {w}")
    print("  Total =", total)                   # O(E log E)


def dijkstra(src=0):                            # shortest time from src to every node
    dist = [INF] * n
    done = [False] * n
    prev = [-1] * n
    dist[src] = 0
    for _ in range(n):
        u = -1
        for v in range(n):
            if not done[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        done[u] = True
        for v in range(n):
            if cost[u][v] != INF and dist[u] + cost[u][v] < dist[v]:
                dist[v] = dist[u] + cost[u][v]   # relax the edge
                prev[v] = u
    print(f"Dijkstra from {places[src]}:")
    for v in range(n):
        path, x = [], v
        while x != -1:
            path.append(places[x])
            x = prev[x]
        print(f"  {places[v]:<5} time {dist[v]:>2}  path {' -> '.join(reversed(path))}")


prim()
kruskal()
dijkstra()
```

## Binary tree traversals
File: `unit5-graphs-trees/binary_tree_traversals.py`

```python
# Unit V: Binary tree - recursive and NON-recursive traversals, height, leaves, mirror, copy
#
#            1
#          /   \
#         2     3
#        / \     \
#       4   5     6

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)
root.right.right = Node(6)


# ---------- Recursive ----------
def inorder(r):
    return inorder(r.left) + [r.data] + inorder(r.right) if r else []


def preorder(r):
    return [r.data] + preorder(r.left) + preorder(r.right) if r else []


def postorder(r):
    return postorder(r.left) + postorder(r.right) + [r.data] if r else []


# ---------- Non-recursive (using a stack) ----------
def inorder_iter(r):
    st, out, cur = [], [], r
    while cur or st:
        while cur:                      # go as far left as possible
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        out.append(cur.data)
        cur = cur.right
    return out


def preorder_iter(r):
    if r is None:
        return []
    st, out = [r], []
    while st:
        cur = st.pop()
        out.append(cur.data)
        if cur.right:                   # push right first so left is processed first
            st.append(cur.right)
        if cur.left:
            st.append(cur.left)
    return out


def postorder_iter(r):                  # two-stack method
    if r is None:
        return []
    s1, s2 = [r], []
    while s1:
        cur = s1.pop()
        s2.append(cur.data)
        if cur.left:
            s1.append(cur.left)
        if cur.right:
            s1.append(cur.right)
    return s2[::-1]


def level_order(r):                     # BFS with a queue
    q, out = [r], []
    while q:
        cur = q.pop(0)
        out.append(cur.data)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return out


# ---------- Other operations ----------
def height(r):
    return 0 if r is None else 1 + max(height(r.left), height(r.right))


def count_leaves(r):
    if r is None:
        return 0
    if r.left is None and r.right is None:
        return 1
    return count_leaves(r.left) + count_leaves(r.right)


def mirror(r):
    if r:
        r.left, r.right = mirror(r.right), mirror(r.left)
    return r


def copy(r):
    if r is None:
        return None
    new = Node(r.data)
    new.left, new.right = copy(r.left), copy(r.right)
    return new


print("Inorder   :", inorder(root), inorder_iter(root))
print("Preorder  :", preorder(root), preorder_iter(root))
print("Postorder :", postorder(root), postorder_iter(root))
print("Level     :", level_order(root))
print("Height =", height(root), " Leaves =", count_leaves(root))
m = mirror(copy(root))
print("Mirror inorder:", inorder(m), " original unchanged:", inorder(root))

# Properties: max nodes at level i = 2^i (root level 0); max nodes in height h = 2^h - 1;
# leaves = nodes with 2 children + 1.
# General tree -> binary tree: left pointer = first child, right pointer = next sibling.
```

## Expression tree from prefix (lab D4)
File: `unit5-graphs-trees/expression_tree.py`

```python
# Lab D4 (syllabus list): Expression tree from a PREFIX expression, e.g. +--a*bc/def
# Traverse it with NON-recursive postorder, then delete the whole tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def build_from_prefix(exp):
    # Scan right to left: operand -> push node; operator -> pop two, make them its children
    st = []
    for ch in reversed(exp):
        node = Node(ch)
        if ch in "+-*/^":
            node.left = st.pop()        # first pop is the LEFT operand when scanning right-to-left
            node.right = st.pop()
        st.append(node)
    return st.pop()


def postorder_nonrecursive(root):      # two stacks
    if root is None:
        return ""
    s1, s2 = [root], []
    while s1:
        cur = s1.pop()
        s2.append(cur)
        if cur.left:
            s1.append(cur.left)
        if cur.right:
            s1.append(cur.right)
    return "".join(n.data for n in reversed(s2))


def inorder(r):                         # fully bracketed infix, to check the tree
    if r is None:
        return ""
    if r.left is None:
        return r.data
    return "(" + inorder(r.left) + r.data + inorder(r.right) + ")"


def delete_tree(root):                  # postorder delete: children before parent
    if root is None:
        return 0
    count = delete_tree(root.left) + delete_tree(root.right)
    root.left = root.right = None
    del root
    return count + 1


exp = input("Prefix expression (e.g. +--a*bc/def): ").strip() or "+--a*bc/def"
root = build_from_prefix(exp)
print("Infix    :", inorder(root))
print("Postfix  :", postorder_nonrecursive(root))
print("Deleted", delete_tree(root), "nodes")
root = None
print("Tree is now", "empty" if root is None else "not empty")
```

## City population BST (lab D5)
File: `unit5-graphs-trees/city_population_bst.py`

```python
# Lab D5 (syllabus list): City names + populations stored in a BST (ordered by city name)
# Add, delete, update population, display ascending/descending, max comparisons to search

class Node:
    def __init__(self, city, pop):
        self.city = city
        self.pop = pop
        self.left = self.right = None


def insert(root, city, pop):
    if root is None:
        return Node(city, pop)
    if city < root.city:
        root.left = insert(root.left, city, pop)
    elif city > root.city:
        root.right = insert(root.right, city, pop)
    else:
        print("City already exists")
    return root


def delete(root, city):
    if root is None:
        print("City not found")
        return None
    if city < root.city:
        root.left = delete(root.left, city)
    elif city > root.city:
        root.right = delete(root.right, city)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        s = root.right
        while s.left:
            s = s.left
        root.city, root.pop = s.city, s.pop
        root.right = delete(root.right, s.city)
    return root


def search(root, city):                 # returns (node, comparisons used)
    comps = 0
    while root:
        comps += 1
        if city == root.city:
            return root, comps
        root = root.left if city < root.city else root.right
    return None, comps


def height(root):                       # max comparisons for any search = height
    return 0 if root is None else 1 + max(height(root.left), height(root.right))


def ascending(r):
    if r:
        ascending(r.left)
        print(f"  {r.city:<12}{r.pop}")
        ascending(r.right)


def descending(r):
    if r:
        descending(r.right)
        print(f"  {r.city:<12}{r.pop}")
        descending(r.left)


root = None
while True:
    print("\n1.Add  2.Delete  3.Update population  4.Ascending  5.Descending  6.Search  7.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        root = insert(root, input("City: "), int(input("Population: ")))
    elif ch == 2:
        root = delete(root, input("City: "))
    elif ch == 3:
        node, _ = search(root, input("City: "))
        if node:
            node.pop = int(input("New population: "))
            print("Updated")
        else:
            print("City not found")
    elif ch == 4:
        ascending(root)
    elif ch == 5:
        descending(root)
    elif ch == 6:
        node, c = search(root, input("City: "))
        print(f"Found {node.city}: {node.pop}" if node else "Not found", f"({c} comparisons)")
        print("Maximum comparisons for any city =", height(root))
    elif ch == 7:
        break
    else:
        print("Invalid choice")
```

## Propositional formula tree (lab D6)
File: `unit5-graphs-trees/propositional_formula_tree.py`

```python
# Lab D6 (syllabus list): Read a propositional calculus formula and build its binary tree
# Operators by precedence (high to low):  ~ (not)   & (and)   | (or)   > (implies)
# Variables are single letters. Example: (p&q)|~r>s
# Each character is read once -> building the tree is O(n) time, O(n) space.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Parser:                           # recursive descent: one function per precedence level
    def __init__(self, s):
        self.s = s.replace(" ", "")
        self.i = 0

    def peek(self):
        return self.s[self.i] if self.i < len(self.s) else None

    def take(self):
        ch = self.s[self.i]
        self.i += 1
        return ch

    def implies(self):                  # right-associative: a > b > c = a > (b > c)
        left = self.disj()
        if self.peek() == ">":
            self.take()
            return Node(">", left, self.implies())
        return left

    def disj(self):
        left = self.conj()
        while self.peek() == "|":
            self.take()
            left = Node("|", left, self.conj())
        return left

    def conj(self):
        left = self.neg()
        while self.peek() == "&":
            self.take()
            left = Node("&", left, self.neg())
        return left

    def neg(self):
        if self.peek() == "~":
            self.take()
            return Node("~", None, self.neg())     # unary: only a right child
        if self.peek() == "(":
            self.take()
            node = self.implies()
            self.take()                             # ")"
            return node
        return Node(self.take())                    # variable


def show(r, indent=""):                 # sideways tree: right subtree on top
    if r:
        show(r.right, indent + "      ")
        print(indent + r.data)
        show(r.left, indent + "      ")


def to_infix(r):
    if r is None:
        return ""
    if r.data == "~":
        return "~" + to_infix(r.right)
    if r.left is None:
        return r.data
    return "(" + to_infix(r.left) + " " + r.data + " " + to_infix(r.right) + ")"


formula = input("Formula (e.g. (p&q)|~r>s): ").strip() or "(p&q)|~r>s"
tree = Parser(formula).implies()
print("Fully bracketed:", to_infix(tree))
print("Tree (rotated 90 degrees, root on the left):")
show(tree)
```

## Huffman coding
File: `unit5-graphs-trees/huffman_coding.py`

```python
# Unit V case study: ZIP/GZIP-style compression with a Huffman tree
# Repeatedly join the two LEAST frequent nodes (greedy). Frequent characters get shorter codes.

class Node:
    def __init__(self, freq, ch=None, left=None, right=None):
        self.freq = freq
        self.ch = ch
        self.left = left
        self.right = right


def build_huffman(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    nodes = [Node(f, c) for c, f in freq.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda n: n.freq)         # a priority queue would be O(log n) per step
        a = nodes.pop(0)
        b = nodes.pop(0)
        nodes.append(Node(a.freq + b.freq, None, a, b))
    return nodes[0], freq


def make_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    if node.ch is not None:                     # leaf
        codes[node.ch] = code or "0"
    else:
        make_codes(node.left, code + "0", codes)
        make_codes(node.right, code + "1", codes)
    return codes


def decode(root, bits):
    out, cur = "", root
    for b in bits:
        cur = cur.left if b == "0" else cur.right
        if cur.ch is not None:
            out += cur.ch
            cur = root
    return out


text = "abracadabra"
root, freq = build_huffman(text)
codes = make_codes(root)
for c in sorted(codes, key=lambda c: -freq[c]):
    print(f"  '{c}' freq {freq[c]}  code {codes[c]}")
encoded = "".join(codes[c] for c in text)
print("Encoded:", encoded)
print(f"Bits: {len(encoded)} vs {len(text) * 8} uncompressed")
print("Decoded:", decode(root, encoded))
```
