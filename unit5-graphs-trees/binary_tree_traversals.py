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
