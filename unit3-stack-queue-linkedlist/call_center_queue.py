# Lab B3 (syllabus list): Call center call queue
# addCall(customerID, callTime), answerCall(), viewQueue(), isQueueEmpty()

class CallQueue:
    def __init__(self):
        self.calls = []

    def addCall(self, customerID, callTime):
        self.calls.append((customerID, callTime))       # enqueue at rear
        print(f"Call from {customerID} ({callTime} min) added")

    def answerCall(self):
        if self.isQueueEmpty():
            print("No calls waiting")
            return
        cid, t = self.calls.pop(0)                      # dequeue from front
        print(f"Answered call from {cid} ({t} min)")

    def viewQueue(self):
        if self.isQueueEmpty():
            print("Queue is empty")
            return
        for i, (cid, t) in enumerate(self.calls, 1):
            print(f"  {i}. Customer {cid} - {t} min")

    def isQueueEmpty(self):
        return len(self.calls) == 0


cq = CallQueue()
while True:
    print("\n1.Add Call  2.Answer Call  3.View Queue  4.Is Empty?  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        cq.addCall(input("Customer ID: "), int(input("Call time (minutes): ")))
    elif ch == 2:
        cq.answerCall()
    elif ch == 3:
        cq.viewQueue()
    elif ch == 4:
        print("Empty" if cq.isQueueEmpty() else "Not empty")
    elif ch == 5:
        break
    else:
        print("Invalid choice")
