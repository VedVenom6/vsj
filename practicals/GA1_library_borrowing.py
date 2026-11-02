# GA1: Library borrowing records
# Average, highest/lowest, members with 0 borrows, mode (most frequent borrow count)
# Every operation is written with plain loops (no max/min/sum) so you can explain it.

def average(counts):
    total = 0
    for c in counts:                 # one pass over n members
        total += c
    return total / len(counts)       # Time O(n), Space O(1)


def highest_lowest(names, counts):
    hi = lo = 0                      # index of highest and lowest so far
    for i in range(1, len(counts)):
        if counts[i] > counts[hi]:
            hi = i
        if counts[i] < counts[lo]:
            lo = i
    return names[hi], counts[hi], names[lo], counts[lo]   # Time O(n), Space O(1)


def count_zero(counts):
    zero = 0
    for c in counts:
        if c == 0:
            zero += 1
    return zero                      # Time O(n), Space O(1)


def mode(counts):
    freq = {}                        # borrow count -> how many times it appears
    for c in counts:
        freq[c] = freq.get(c, 0) + 1
    best = counts[0]
    for c in freq:
        if freq[c] > freq[best]:
            best = c
    return best, freq[best]          # Time O(n), Space O(k), k = distinct counts


n = int(input("Number of members: "))
names = []
counts = []
for i in range(n):
    name = input(f"Member {i + 1} name: ")
    c = int(input(f"Books borrowed by {name}: "))
    names.append(name)
    counts.append(c)

while True:
    print("\n1.Average  2.Highest & Lowest  3.Members with 0 books  4.Mode  5.Complexity  6.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        print("Average books borrowed =", round(average(counts), 2))
    elif ch == 2:
        hn, hc, ln, lc = highest_lowest(names, counts)
        print(f"Highest: {hn} ({hc} books)   Lowest: {ln} ({lc} books)")
    elif ch == 3:
        print("Members who borrowed 0 books =", count_zero(counts))
    elif ch == 4:
        m, f = mode(counts)
        print(f"Most frequent borrow count = {m} (appears {f} times)")
    elif ch == 5:
        print("Average        : Time O(n)  Space O(1)")
        print("Highest/Lowest : Time O(n)  Space O(1)")
        print("Count zero     : Time O(n)  Space O(1)")
        print("Mode           : Time O(n)  Space O(k)  (dictionary of k distinct counts)")
    elif ch == 6:
        break
    else:
        print("Invalid choice")
