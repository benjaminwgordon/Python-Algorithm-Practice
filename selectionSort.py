import random
import math

def selectionSort(arr):
    for i in range(0,len(arr)):
        min = i
        for j in range (i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr


print(selectionSort([math.floor(random.random() * 1000) for i in range(1000)]))