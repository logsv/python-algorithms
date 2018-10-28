import random
def generate_rand_list(rng):
    # generate a list with random value
    arr_list = []
    for iterations in range(100):
        arr_list.append(random.randint(0, rng))
    print("List of size:  {}".format(rng))
    return arr_list

def insertion_sort(rng):
    # insertion sort
    arr_list = generate_rand_list(rng)
    for i in range(0, rng-1):
        j = i + 1
        while j > 0 and arr_list[j-1] > arr_list[j]:
            arr_list[j], arr_list[j-1] = arr_list[j-1], arr_list[j]
            j -= 1
    # print
    print("Sorted List with size: {}".format(rng))
    print(arr_list)

if __name__ == '__main__':
    insertion_sort(10)
    insertion_sort(50)