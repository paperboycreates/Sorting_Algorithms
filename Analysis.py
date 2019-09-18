# ==================================================================== #
# File Name: Analysis.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Sorting Algorthim Analysizer
# ==================================================================== #

from datetime import datetime
import random

from Counting_Sort import countingSort
from Insertion_Sort import insertionSort
from Merge_Sort import mergeSort

# funct to init list of length n with rand values [0..n]
def initList(n):
    newList = []
    for i in range(n):
        rand = random.randint(0, n)
        newList.append(rand)
    return newList

# funct to check if list is sorted
def isSorted(newList):
    if (len(newList) < 2):
        return True
    for i in range(len(newList)):
        if (i + 1 < len(newList) and newList[i] > newList[i + 1]):
            return False
    return True

testInterval = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
# Number of Elements highest list
n = max(testInterval)

timeCount = []
timeMerge = []
timeInsert = []




for i in testInterval:
    # ==================================================================== #
    # Counting Sort O(n)
    # ==================================================================== #
    startTime = endTime = totalTime = 0
    unsortedList = initList(n)

    # start clock and perform sort
    startTime = time.time()
    sortedList = countingSort(unsortedList)
    totalTime = time.time() - startTime
    timeCount.append(totalTime)

    # print(sortedList)
    # get total time and display
    # print("Counting Sort")
    # print(isSorted(sortedList))
    # print(totalTime)
    # print()

    # ==================================================================== #
    # Merge Sort O(nlgn)
    # ==================================================================== #

    startTime = endTime = totalTime = 0
    unsortedList = initList(n)

    # start clock and perform sort
    startTime = time.time()
    sortedList = mergeSort(unsortedList)
    totalTime = time.time() - startTime
    timeMerge.append(totalTime)

    # print(sortedList)
    # get total time and display
    # print("Merge Sort")
    # print(isSorted(sortedList))
    # print(totalTime)
    # print()

    # ==================================================================== #
    # Insertion Sort O(n^2)
    # ==================================================================== #
    if i >= 10000:
        startTime = endTime = totalTime = 0
        unsortedList = initList(n)

        # start clock and perform sort
        startTimeInsert = time.time()
        sortedList = insertionSort(unsortedList)
        totalTimeInsert = time.time() - startTimeInsert
        timeInsert.append(totalTimeInsert)

        # print(sortedList)
        # print("Insertion Sort")
        # print(isSorted(sortedList))
        # print(totalTime)
        # print()
