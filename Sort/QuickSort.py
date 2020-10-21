

def quicksort(arr, low, high):
    """
    Use case: 
        Sorting an array
    Best use case:
        Smaller arrays (MergeSort takes over for bigger arrays, and distribution sorts take over for arrays made up of specific data types)
        Especially advantageous where smaller space complexity is an advantage, or on smaller arrays where it runs faster than MergeSort with non-contrived inputs
    Time Complexity
        Best case: O(n*log(n)) -- 
        Average case: O(n*log(n)) -- 
        Worst case: O(n^2) -- Contrived cases where the data is especially unbalanced in a way that makes partition selection a problem
    Space complexity: 
        O(log(n)) -- repeated assignment of pointers for each recursive call
    Stable: No
    """

    #we have a base case here of low >= high, but we dont need to specify it because we dont need to return it
    # Why?  The partition function is doing in place changes on the array, so we dont need to return any data
    # Since there is no code left to run, there is an implicit empty return
    if low < high:
        partitionIndex = partition(arr, low, high)

        quicksort(arr, low, partitionIndex - 1)
        quicksort(arr, partitionIndex + 1, high)

def partition(arr, low, high):
    smallerThanPivotIndex = low - 1
    pivot = arr[high] 

    print("pre-partition", arr[low:high + 1])

    for j in range(low, high):  #iterating by index
        if arr[j] <= pivot:
            #since this element is smaller than the pivot, we need it to be on the left side of the pivot (Note, the element on either side of the pivot are not sorted yet)
            smallerThanPivotIndex += 1

            #swap the current element with the current index of the smaller-side of the pivot
            temp = arr[smallerThanPivotIndex]
            arr[smallerThanPivotIndex] = arr[j]
            arr[j] = temp

    #once we are done, we need to move the pivot to its correct position in the middle of the array
    temp = arr[high]
    arr[high] = arr[smallerThanPivotIndex+1]
    arr[smallerThanPivotIndex+1] = temp
    print("post-partition",
     arr[low:smallerThanPivotIndex+1], 
     arr[smallerThanPivotIndex+1], 
     arr[smallerThanPivotIndex + 2 : high + 1], 
     "\n")
    return (smallerThanPivotIndex+1)


arr = [8,4,7,5,9,3,6,8,5,7,4,8,5,2,1,3,5,6,9,8,7,4,2,5,4,8,6,8,7,2,6,8]
print(arr)
quicksort(arr, 0, len(arr)-1)
print(arr)

defaultSorted = [8,4,7,5,9,3,6,8,5,7,4,8,5,2,1,3,5,6,9,8,7,4,2,5,4,8,6,8,7,2,6,8]
defaultSorted.sort()
print(defaultSorted == arr)
print()