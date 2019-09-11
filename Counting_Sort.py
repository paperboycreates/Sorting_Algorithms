# ==================================================================== #
# File Name: Counting_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Counting Sort Algorthim
# ==================================================================== #


def counting_Sort(unSorted, sorted, count):
    #intiazlie count
    i = 0
    for i in range(0, k):
        count[i] = 0
    #creat counts
    j =1
    for j in range(0, len(unSorted)):
        count[unSorted[j]] = count[unSorted[j]]+1
    #creat running sum
    i = 1
    for i in range(0,k):
        count[i] = count[i]+count[i-1]
    #place elements
    j = len(unSorted)
    for j range(j, 1, -1):
        sorted[count[unSorted[j]]] = unSorted[j]
        count[unSorted[j]] = count[unSorted[j]]-1

# Quick Test
def main():    

    testArray = [18, 14, 4, 7, 12, 2, 3, 6, 100, 40, 5, 1]
    counting_Sort(testArray)   
    print (testArray)

# Runs Main Test
main()