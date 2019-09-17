# ==================================================================== #
# File Name: Merge_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Merge Sort Algorthim
# ==================================================================== #

def mergeSort(newList):
    if (len(newList) > 1):
        # get the middle element of mid (floored) and split
        mid = len(newList) // 2
        left = newList[0:mid]
        right = newList[mid:len(newList)]

        # recursively call mergeSort on both halves
        mergeSort(left)
        mergeSort(right)

        merge(newList, left, right)
        return newList

def merge(newList, left, right):
    i = j = k = 0
    # simultaneously traverse left and right, getting smallest
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            newList[k] = left[i]
            i += 1
            k += 1
        else:
            newList[k] = right[j]
            j += 1
            k += 1

    # check both lists for anything left
    while (i < len(left)):
        newList[k] = left[i]
        i += 1
        k += 1
    while (j < len(right)):
        newList[k] = right[j]
        j += 1
        k += 1