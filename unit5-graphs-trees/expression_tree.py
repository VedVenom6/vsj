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
