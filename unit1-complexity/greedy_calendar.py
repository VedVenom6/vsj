# Unit I case study: Google Calendar style scheduling using the Greedy strategy
# Activity selection: fit the MAXIMUM number of non-overlapping meetings.
# Greedy choice: always pick the meeting that ENDS earliest.  Time O(n log n) for the sort.

meetings = [
    ("Standup", 9, 10),
    ("Design review", 9, 12),
    ("Lunch", 12, 13),
    ("Client call", 10, 11),
    ("Lab", 11, 14),
    ("Code review", 13, 15),
    ("1:1", 15, 16),
]

meetings.sort(key=lambda m: m[2])        # sort by end time

chosen = []
last_end = 0
for name, start, end in meetings:
    if start >= last_end:                # doesn't overlap the last chosen meeting
        chosen.append((name, start, end))
        last_end = end

print("Selected meetings:")
for name, s, e in chosen:
    print(f"  {s:>2}:00 - {e:>2}:00  {name}")
print("Total:", len(chosen))
