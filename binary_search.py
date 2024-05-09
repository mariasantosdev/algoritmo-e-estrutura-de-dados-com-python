def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess > item:
            high = middle - 1
        elif item == guess:
            return middle
        else:
            low = middle + 1

    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
