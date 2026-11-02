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
