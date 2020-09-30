def binarySearch(arr,k):
    """
    Use case: 
        searching a sorted array for a value
    Best case:
        on any sorted array, binary search is preferred over linear search
    Time Complexity
        Best case: O(1) -- k happens to be the middle element
        Average case: O(log(n))-- repeated halving of search set creates a base 2 log
        Worst case: O(log(n)) -- repeated halving of search set creates a base 2 log
    Space complexity: 
        O(1) -- three pointers (low, mid, high)
    """
    lowIndex = 0
    highIndex = len(arr) - 1

    while(lowIndex <= highIndex):
        midIndex = (lowIndex + highIndex) // 2
        if k == arr[midIndex]:
            return midIndex
        elif k > arr[midIndex]:
            lowIndex = midIndex + 1
        else:
            highIndex = midIndex - 1
    return -1