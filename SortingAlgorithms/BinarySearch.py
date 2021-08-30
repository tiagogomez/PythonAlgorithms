def binarySearch(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else: #guess < item:
            low = mid + 1
    return None

myList = [1,3,5,7,9]

result1 = binarySearch(myList,3)
print(result1)

result2 = binarySearch(myList,-1)
print(result2)

#Orden de magnitud O(log n)

# Ordenes de magnitud de menor a mayor
# O(log n), O(n), O(n * log n), O(n^2), O(n!)