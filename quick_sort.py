def particion(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pi = particion(arr, low, high) # pi -> partition index
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    example_array = [485, 348, 22, -2, -345, 430, 23, 44, 345, 88, 
        320, 5, 32, 65, 2365, 2342, -354, 0, 203, -43, 12]
    n = len(example_array)
    
    quick_sort(example_array, 0, n-1)

    print("Array ordenado: ")
    print(' '.join(str(n) for n in example_array))
