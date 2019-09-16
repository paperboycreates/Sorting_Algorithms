# ==================================================================== #
# File Name: Merge_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Merge Sort Algorthim
# ==================================================================== #

import random 

def mergeSort(arr):
    if (len(arr) > 1):
        # get the middle element of mid (floored) and split
        mid = len(arr) // 2
        left = arr[0:mid]
        right = arr[mid:len(arr)]

        # recursively call mergeSort on both halves
        mergeSort(left)
        mergeSort(right)

        merge(arr, left, right)

def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    # simultaneously traverse left and right getting smallest
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    # check both arrays for anything left
    while (i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1

    while (j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1

def initArr(n):
    arr = []
    for i in range(n):
        rand = random.randint(0, n)
        arr.append(rand)
    return arr

def isSorted(arr):
    if (len(arr) < 2):
        return True
    i = 0
    for i in range(len(arr)):
        if (i + 1 < len(arr) and arr[i] > arr[i + 1]):
            return False
    return True  


# generate arr of length n and merge
arr = initArr(1000000)
# print(arr)

mergeSort(arr)
# print(arr)
print(isSorted(arr))