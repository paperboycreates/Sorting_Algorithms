# ==================================================================== #
# File Name: Insertion_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 1.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Insertion Sort Algorthim
# ==================================================================== #

def insertionSort(unsortedList):

    # run through entire array
    for i in range(1, len(unsortedList)):
        key = unsortedList[i]
        j = i - 1
       
        # moves the key through i-1 to 0 to find position where key < positon
        while j >= 0 and unsortedList[j] > key:
             unsortedList[j+1] = unsortedList[j]
             j = j - 1
        unsortedList[j+1] = key
    
    return unsortedList