def selectionSort(arr):
    """
    Use case: 
        sorting an array
    Best use case:
        selectionSort is similar to insertionSort, but performs worse across all cases (on arrays)
    Time Complexity
        Best case: O(n^2) -- runs n many iterations of (iterate over n - m operations)
        Average case: O(n^2) -- runs n many iterations of (iterate over n - m operations)
        Worst case: O(n^2) -- runs n many iterations of (iterate over n - m operations)
    Space complexity: 
        O(1) -- pointers
    """
    for i in range(0,len(arr)):
        min = i
        for j in range (i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr