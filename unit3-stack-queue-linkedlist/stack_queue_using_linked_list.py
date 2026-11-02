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
