def bubble_sort(arr):
    n = len(arr)
    cambios = []
    cambios.append(str(arr))
    for i in range(n):
        print(arr)
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if str(arr) in cambios:
            break
        cambios.append(str(arr))


if __name__ == "__main__":    
    example_input = [12, 32, 43, 234, 235, 11, 32, 76, 357, 37]

    bubble_sort(example_input)
    print("Arreglo ordenado de forma Ascendente es:")

    print(' '.join(str(n) for n in example_input))
