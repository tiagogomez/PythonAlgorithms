def selectionSort(arr):
    newArray = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr)   # Selecciona el elemento más pequeño
        newArray.append(arr.pop(smallestIndex)) # Agrega el elemento a un nuevo array y lo saca del viejo
    return newArray

def findSmallest(arr):
    smallestValue = arr[0]
    smallestIndex = 0   # Selecciona el primer elemento
    for i in range(1, len(arr)): # Compara el primer elemento con el segundo
        if arr[i] < smallestValue:
            smallestValue = arr[i]
            smallestIndex = i
    return smallestIndex

result = selectionSort([5,3,6,2,10])
print(result)