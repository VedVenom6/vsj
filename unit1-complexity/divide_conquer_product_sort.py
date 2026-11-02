# Unit I case study: E-commerce product sorting using Divide and Conquer (Merge sort)
# Divide the list in half, sort each half recursively, then merge.  T(n) = 2T(n/2) + n = O(n log n)

def merge_sort(products, key):
    if len(products) <= 1:                       # base case
        return products
    mid = len(products) // 2
    left = merge_sort(products[:mid], key)       # divide + conquer
    right = merge_sort(products[mid:], key)
    return merge(left, right, key)               # combine


def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:        # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


products = [
    {"name": "Laptop", "price": 55000, "rating": 4.4},
    {"name": "Mouse", "price": 700, "rating": 4.1},
    {"name": "Phone", "price": 18000, "rating": 4.6},
    {"name": "Earbuds", "price": 1500, "rating": 3.9},
    {"name": "Monitor", "price": 12000, "rating": 4.3},
]

print("By price (low to high):")
for p in merge_sort(products, "price"):
    print(f"  {p['name']:<8} Rs {p['price']}")

print("By rating (high to low):")
for p in reversed(merge_sort(products, "rating")):
    print(f"  {p['name']:<8} {p['rating']}")
