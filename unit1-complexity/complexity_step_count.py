# Unit I: Step count method - count how many times the basic operation runs
# Linear O(n), Quadratic O(n^2), Cubic O(n^3), Logarithmic O(log n)

def linear(n):
    steps = 0
    for i in range(n):
        steps += 1
    return steps


def quadratic(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps


def cubic(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                steps += 1
    return steps


def logarithmic(n):
    steps = 0
    i = n
    while i > 1:            # i halves each time -> log2(n) iterations
        i //= 2
        steps += 1
    return steps


print(f"{'n':>5}{'log n':>8}{'n':>8}{'n^2':>10}{'n^3':>12}")
for n in (8, 16, 32, 64):
    print(f"{n:>5}{logarithmic(n):>8}{linear(n):>8}{quadratic(n):>10}{cubic(n):>12}")

# Step count for sum of array:
#   total = 0                1
#   for x in arr:            n + 1
#       total += x           n
#   return total             1
#   ---------------------------------
#   T(n) = 2n + 3  ->  O(n)
#
# Big-O = upper bound (worst case), Omega = lower bound (best case),
# Theta = tight bound (upper and lower are the same order).
