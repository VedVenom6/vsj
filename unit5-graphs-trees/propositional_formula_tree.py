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
