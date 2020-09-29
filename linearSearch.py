def linearSearch(arr, k):
    """Linear Search Implementation: Finds element k in List arr"""
    for index,value in enumerate(arr):
        if value == k:
            return index
    return -1