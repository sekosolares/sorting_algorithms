# Buscar numero menor en el array
# Crear dos subarrays para llevar el control del algoritmo
# Imprimir el resultado del ordenamiento

from datetime import datetime

def selection_sort(arr):
    # Recorrer todo el array
    for i in range(len(arr)):
        # Encontrar valor minimo restante dentro del array desordenado
        index_desordenado = i
        # print(arr)
        for j in range(i+1, len(arr)):
            if arr[index_desordenado] > arr[j]:
                index_desordenado = j
        # Ya encontrado el minimo elemento, cambiar 1er valor de array desordenado
        arr[i], arr[index_desordenado] = arr[index_desordenado], arr[i]


if __name__ == "__main__":
    example_input = [3, 94, 86, 82, 90, 10, 87, 36, 61, 8, 17, 15, 22, 10, 23, 78, 25, 2, 30, 45, 98, 43, 98, 59, 53, 57, 2, 64, 1, 41, 32, 58, 19, 99, 60, 74, 48, 80, 44, 25, 68, 1, 89, 77, 60, 25, 99, 30, 76, 32, 57, 82, 52, 44, 72, 87, 34, 87, 65, 30, 54, 6, 31, 33, 44, 44, 42, 82, 90, 17, 9, 98, 28, 86, 69, 3, 17, 8, 45, 98, 12, 47, 95, 43, 72, 39, 41, 82, 74, 56, 65, 79, 50, 26, 67, 100, 24, 67, 38, 57]

    initial_time = datetime.now()

    selection_sort(example_input)

    print("Array ordenado es:")

    print(' '.join(str(elem) for elem in example_input))
    print(datetime.now() - initial_time)
