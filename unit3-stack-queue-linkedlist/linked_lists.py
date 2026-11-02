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
