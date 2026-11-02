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
