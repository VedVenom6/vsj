# GB6: Student Record Management System using a Singly Linked List
# Node stores Roll No, Name, Marks. Add, Delete, Update, Search, Sort, Display asc/desc.

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                return temp
            temp = temp.next
        return None

    def add(self, roll, name, marks):           # insert at end
        if self.search(roll):
            print("Roll number already exists")
            return
        new = Node(roll, name, marks)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, roll):
        if self.head is None:
            return False
        if self.head.roll == roll:              # deleting the first node
            self.head = self.head.next
            return True
        prev = self.head
        while prev.next and prev.next.roll != roll:
            prev = prev.next
        if prev.next is None:
            return False
        prev.next = prev.next.next              # unlink the node
        return True

    def update(self, roll, name, marks):
        node = self.search(roll)
        if node:
            node.name = name
            node.marks = marks
            return True
        return False

    def sort(self, key, descending=False):     # bubble sort by swapping node data
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                a = getattr(temp, key)
                b = getattr(temp.next, key)
                if (a > b and not descending) or (a < b and descending):
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next

    def display(self):
        if self.head is None:
            print("No records")
            return
        print(f"{'Roll':<6}{'Name':<15}{'Marks':<6}")
        temp = self.head
        while temp:
            print(f"{temp.roll:<6}{temp.name:<15}{temp.marks:<6}")
            temp = temp.next


s = StudentList()

while True:
    print("\n1.Add  2.Delete  3.Update  4.Search  5.Sort & Display  6.Display  7.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        r = int(input("Roll No: "))
        n = input("Name: ")
        m = float(input("Marks: "))
        s.add(r, n, m)
    elif ch == 2:
        r = int(input("Roll No to delete: "))
        print("Deleted" if s.delete(r) else "Not found")
    elif ch == 3:
        r = int(input("Roll No to update: "))
        n = input("New name: ")
        m = float(input("New marks: "))
        print("Updated" if s.update(r, n, m) else "Not found")
    elif ch == 4:
        node = s.search(int(input("Roll No to search: ")))
        print(f"Found: {node.roll} {node.name} {node.marks}" if node else "Not found")
    elif ch == 5:
        k = input("Sort by (roll/marks): ").strip()
        if k not in ("roll", "marks"):
            print("Type roll or marks")
            continue
        order = input("Order (asc/desc): ").strip()
        s.sort(k, order == "desc")
        s.display()
    elif ch == 6:
        s.display()
    elif ch == 7:
        break
    else:
        print("Invalid choice")
