def binarySearch(arr,k):
    """Finds elem k in sorted array arr"""
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


print(binarySearch([1,3,5,6,7,9,11,14,26], 26))