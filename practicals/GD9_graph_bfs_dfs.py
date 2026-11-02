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
