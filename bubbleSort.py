import math
import random

def bubbleSort(arr):
    """BubbleSort Implementation: sorts input List"""
    isSorted = False
    while not isSorted:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        isSorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                isSorted = False
                break
    else:
        return arr