# BUBBLE SORT FUNCTION
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubbleSort([1, 5, 7, 2, 9]))
