# BUBBLE SORT FUNCTION
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def minMax3(a, b, c):
    max = 0
    min = 0
    if (a > b and a > c):
        max = a
    if (b > a and b > c):
        max = b
    if (c > a and c > b):
        max = c
    if (a < b and a < c):
        min = a
    if (b < a and b < c):
        min = b
    if (c < a and c < b):
        min = c
    print(f"min= {min}\n max={max}")
