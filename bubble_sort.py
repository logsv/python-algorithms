# bubble sort
# ----------------
arr = [6, 1, 2, 5, 4, 7, 9, 10, 2, 15, 18, 12, 14]
n = len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)

# Optimizing bubble sort
# -----------------
# optimized by observing that the n-th pass finds the n-th largest element and puts it into its final place.
# So, the inner loop can avoid looking at the last n − 1 items when running for the n-th time
arr = [6, 1, 2, 5, 4, 7, 9, 10, 2, 15, 18, 12, 14]
n1 = n2 = len(arr)
for i in range(n1):
    for j in range(n2-1):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    n2 -= 1

print(arr)


# --------------------
# a worst case 50% improvement in comparison count
arr = [6, 1, 2, 5, 4, 7, 9, 10, 2, 15, 18, 12, 14]
n1 = n2 = len(arr)
for i in range(n1):
    for j in range(n2-1):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            sortn = j+1
    n2 = sortn

print(arr)
