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
