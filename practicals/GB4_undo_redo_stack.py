# GB4: Undo / Redo for a text editor using two stacks

undo_stack = []      # every change made, latest on top
redo_stack = []      # changes that were undone, latest on top


def make_change(text):
    undo_stack.append(text)          # push
    redo_stack.clear()               # a new change kills the redo history
    print("Change added:", text)


def undo():
    if not undo_stack:
        print("Nothing to undo")
        return
    change = undo_stack.pop()        # pop latest change
    redo_stack.append(change)        # keep it for redo
    print("Undone:", change)


def redo():
    if not redo_stack:
        print("Nothing to redo")
        return
    change = redo_stack.pop()
    undo_stack.append(change)
    print("Redone:", change)


def display():
    print("Document:", " ".join(undo_stack) if undo_stack else "(empty)")
    print("Undo stack:", undo_stack)
    print("Redo stack:", redo_stack)


while True:
    print("\n1.Make Change  2.Undo  3.Redo  4.Display Document  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        make_change(input("Enter text: "))
    elif ch == 2:
        undo()
        display()
    elif ch == 3:
        redo()
        display()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
