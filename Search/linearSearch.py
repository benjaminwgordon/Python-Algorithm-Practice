def linearSearch(arr, k):
    """
    Use case: 
        searching an array for a value
    Best use case:
        linear search is on unsorted data arrays, 
        binary search would always be preferred for sorted arrays
    Time Complexity
        Best case: O(1) -- k happens to be the first element
        Average case: O(n) -- mean number of checks is 1/2 of all elements, simplifies to n
        Worst case: O(n) -- element is last element, all elements must be checked 
    Space complexity: 
        O(1) -- one pointer
    """
    for index,value in enumerate(arr):
        if value == k:
            return index
    return -1