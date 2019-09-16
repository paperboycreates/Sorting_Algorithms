# ==================================================================== #
# File Name: Insertion_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Insertion Sort Algorthim
# ==================================================================== #

def insertion_sort(unsortedList):

    # run through entire array
    for i in range(1, len(unsortedList)):
        key = unsortedList[i]
        j = i - 1
        # moves the key through i-1 to 0 to find position where key < positon
        while j >= 0 and unsortedList[j] > key:
             unsortedList[j+1] = unsortedList[j]
             j = j - 1
        unsortedList[j+1] = key

# Quick Test
def main():    

    testArray = [18, 14, 4, 7, 12, 2, 3, 6, 100, 40, 5, 1]
    insertion_sort(testArray)   
    print (testArray)

# Runs Main Test
main()