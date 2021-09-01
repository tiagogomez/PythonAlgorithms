def quickSort(array):
    if len(array) < 2:  # Caso base, un array con 0 o 1 elemento no se debe ordenar
        return array
    else:   # Caso recursivo
        pivot = array[0]    # Elemento a comparar

        less = [i for i in array[1:] if i <= pivot] # Elementos más pequeños que el pivote
        greater = [i for i in array[1:] if i > pivot] # Elementos más grandes que el pivote

        return quickSort(less) + [pivot] + quickSort(greater)

result = quickSort([10, 5, 2, 3])
print(result)