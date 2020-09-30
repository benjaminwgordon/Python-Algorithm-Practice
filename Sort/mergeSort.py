def mergeSort(arr):
    """
    Use case: 
        sorting an array 
    Best use case:
        Merge sort is a general purpose sort for arrays, that works better than quicksort when working with larger arrays
    Time Complexity
        Best case: O(n * Log(n)) -- Merge sort must always traverse to full depth and rebuild, thus n * Log(n)
        Average case: O(n * Log(n)) -- Merge sort must always traverse to full depth and rebuild, thus n * Log(n)
        Worst case: O(n * Log(n)) -- Merge sort must always traverse to full depth and rebuild, thus n * Log(n)
    Space complexity: 
        O(n) -- each element duplicated once while breaking array down into subarrays
    """
    if len(arr) == 1:
        return arr
    else:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)

def merge(left, right):
    out = []
    while (len(left) != 0 and len(right) != 0):
        if left[0] <= right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    else:
        if len(left) == 0:
            out.extend(right)
            return out
        else:
            out.extend(left)
            return out