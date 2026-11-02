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
