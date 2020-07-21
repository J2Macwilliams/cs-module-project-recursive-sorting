# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    return merged_arr
    # a = 0
    # b = 0
    # for i in range(0, elements):
    #     if a == len(arrA) :
    #         merged_arr[i] = arrB[b]
    #         b += 1
    #     elif b == len(arrB) :
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     elif arrA[a] < arrB[b]:
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     else:
    #         merged_arr[i] = arrB[b]
    #         b += 1
    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    low = 0
    high = len(arr) 
    mid = (low + high) // 2
    # split into 2 initial arrays
    if len(arr) > 1:
        A = merge_sort(arr[:mid])
        B = merge_sort(arr[mid:])
        arr = merge(A, B)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

