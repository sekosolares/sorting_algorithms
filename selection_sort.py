# Buscar numero menor en el array
# Crear dos subarrays para llevar el control del algoritmo
# Imprimir el resultado del ordenamiento

import sys

def selection_sort(arr):
    # Recorrer todo el array
    for i in range(len(arr)):
        # Encontrar valor minimo restante dentro del array desordenado
        index_desordenado = i
        print(arr)
        for j in range(i+1, len(arr)):
            if arr[index_desordenado] > arr[j]:
                index_desordenado = j
        # Ya encontrado el minimo elemento, cambiar 1er valor de array desordenado
        arr[i], arr[index_desordenado] = arr[index_desordenado], arr[i]


if __name__ == "__main__":
    example_input = [15, 33, 2, 13, 46, 777, 23, 9, 23, 43, 0]

    selection_sort(example_input)

    print("Array ordenado es:")

    print(' '.join(str(elem) for elem in example_input))
