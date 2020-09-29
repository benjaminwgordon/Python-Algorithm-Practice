def linearSearch(arr, k):
    for index,value in enumerate(arr):
        if value == k:
            return index
    return -1


arr = [1,5,3,8,2,6,0,6,9,3,5,6,7,8,3,4,2,5,2,8]
for i in range(0,10):
    print(linearSearch(arr,i))