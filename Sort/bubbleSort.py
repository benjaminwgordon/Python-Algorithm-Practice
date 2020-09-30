def bubbleSort(arr):
    """
    Use case: 
        Sorting an array
    Best use case:
        bubblesort has extremely small overhead, 
        thus it is comparably fast or faster than other sorting algorithms (except insertionSort) when working with tiny arrays
    Time Complexity
        Best case: O(n) -- array is already sorted
        Average case: O(n^2) -- each iteration makes a number of swaps equal to the length of the array, and required n many iterations
        Worst case: O(n^2) -- each iteration makes a number of swaps equal to the length of the array, and required n many iterations
    Space complexity: 
        O(1) -- two pointers
    """
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