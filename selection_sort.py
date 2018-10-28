# selection sort
lst = [1,10,5,4,3,2,8,9,6,3,17,1,5,15,13,12]

n = len(lst)
for i in range(0, n-1):
    minIndex = i # index for min value
    for j in range(i+1, n):
        if lst[minIndex] > lst[j]:
            minIndex = j  # change the index for min value
    if i != minIndex:
        lst[i], lst[minIndex] =  lst[minIndex], lst[i]

# print
print(lst)
