# GB5: Real-time event processing using a Queue (FIFO)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, x):            # add at rear
        self.items.append(x)

    def dequeue(self):               # remove from front (oldest)
        return self.items.pop(0)

    def remove(self, x):             # cancel an unprocessed event
        if x in self.items:
            self.items.remove(x)
            return True
        return False


q = Queue()

while True:
    print("\n1.Add Event  2.Process Next Event  3.Display Pending  4.Cancel Event  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        e = input("Event name: ")
        q.enqueue(e)
        print("Added:", e)
    elif ch == 2:
        if q.is_empty():
            print("No events to process")
        else:
            print("Processed:", q.dequeue())
    elif ch == 3:
        print("Pending events (front -> rear):", q.items if not q.is_empty() else "none")
    elif ch == 4:
        e = input("Event to cancel: ")
        print("Cancelled:", e if q.remove(e) else "event not found / already processed")
    elif ch == 5:
        break
    else:
        print("Invalid choice")
