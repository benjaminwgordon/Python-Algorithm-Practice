def mergeSort(arr):
    """MergeSort Implementation: Sorts given List arr"""
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