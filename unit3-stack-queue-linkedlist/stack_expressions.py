# Unit III: Stack, multiple stacks, infix -> postfix / prefix, postfix evaluation

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


# ---------- Two stacks in one array (multiple stacks) ----------
class TwoStacks:
    def __init__(self, size):
        self.arr = [None] * size
        self.top1, self.top2 = -1, size      # stack 1 grows right, stack 2 grows left

    def push1(self, x):
        if self.top1 + 1 == self.top2:
            print("Overflow"); return
        self.top1 += 1
        self.arr[self.top1] = x

    def push2(self, x):
        if self.top2 - 1 == self.top1:
            print("Overflow"); return
        self.top2 -= 1
        self.arr[self.top2] = x

    def pop1(self):
        x = self.arr[self.top1]; self.top1 -= 1; return x

    def pop2(self):
        x = self.arr[self.top2]; self.top2 += 1; return x


# ---------- Expression conversion ----------
PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_to_postfix(exp):
    st = Stack()
    out = ""
    for ch in exp:
        if ch.isalnum():                     # operand goes straight to output
            out += ch
        elif ch == "(":
            st.push(ch)
        elif ch == ")":
            while st.peek() != "(":
                out += st.pop()
            st.pop()                         # discard "("
        else:                                # operator
            while (not st.is_empty() and st.peek() != "(" and
                   (PREC[st.peek()] > PREC[ch] or
                    (PREC[st.peek()] == PREC[ch] and ch != "^"))):   # ^ is right-associative
                out += st.pop()
            st.push(ch)
    while not st.is_empty():
        out += st.pop()
    return out


def infix_to_prefix(exp):
    # reverse, swap brackets, convert to postfix (^ handled as left-assoc here), reverse again
    rev = ""
    for ch in exp[::-1]:
        rev += "(" if ch == ")" else ")" if ch == "(" else ch
    st = Stack()
    out = ""
    for ch in rev:
        if ch.isalnum():
            out += ch
        elif ch == "(":
            st.push(ch)
        elif ch == ")":
            while st.peek() != "(":
                out += st.pop()
            st.pop()
        else:
            while (not st.is_empty() and st.peek() != "(" and
                   (PREC[st.peek()] > PREC[ch] or (PREC[st.peek()] == PREC[ch] and ch == "^"))):
                out += st.pop()
            st.push(ch)
    while not st.is_empty():
        out += st.pop()
    return out[::-1]


def evaluate_postfix(exp):                    # space-separated tokens, e.g. "5 3 + 2 *"
    st = Stack()
    for tok in exp.split():
        if tok.lstrip("-").isdigit():
            st.push(int(tok))
        else:
            b, a = st.pop(), st.pop()        # second operand is popped first
            if tok == "+": st.push(a + b)
            elif tok == "-": st.push(a - b)
            elif tok == "*": st.push(a * b)
            elif tok == "/": st.push(a / b)
            elif tok == "^": st.push(a ** b)
    return st.pop()


for e in ("A+B*C", "(A+B)*C", "A+B*(C^D-E)", "A^B^C"):
    print(f"{e:<14} postfix: {infix_to_postfix(e):<12} prefix: {infix_to_prefix(e)}")
print("5 3 + 2 * =", evaluate_postfix("5 3 + 2 *"))
print("6 2 / 3 4 * + =", evaluate_postfix("6 2 / 3 4 * +"))

ts = TwoStacks(5)
ts.push1(1); ts.push1(2); ts.push2(9); ts.push2(8)
print("TwoStacks array:", ts.arr, " pop1:", ts.pop1(), " pop2:", ts.pop2())
