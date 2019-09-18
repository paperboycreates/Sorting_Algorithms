# ==================================================================== #
# File Name: Analysis.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 2.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Sorting Algorthim Analysizer
# ==================================================================== #

from datetime import datetime
import time
import random
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np

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
# Used for debuging
def isSorted(newList):
    if (len(newList) < 2):
        return True
    for i in range(len(newList)):
        if (i + 1 < len(newList) and newList[i] > newList[i + 1]):
            return False
    return True

# ==================================================================== #
# Main # 
# ==================================================================== #

testInterval = [10, 25, 50, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
# Number of Elements highest list
n = max(testInterval)

timeCount = []
timeMerge = []
timeInsert = []

for i in testInterval:
    # ==================================================================== #
    # Counting Sort O(n) #
    # ==================================================================== #
    startTime = endTime = totalTime = 0
    unsortedList = initList(i)

    # start clock and perform sort
    startTime = time.time()
    sortedList = countingSort(unsortedList)
    totalTime = time.time() - startTime
    timeCount.append(totalTime)

    # ==================================================================== #
    # Merge Sort O(nlgn) #
    # ==================================================================== #
    startTime = endTime = totalTime = 0
    unsortedList = initList(i)

    # start clock and perform sort
    startTime = time.time()
    sortedList = mergeSort(unsortedList)
    totalTime = time.time() - startTime
    timeMerge.append(totalTime)

    # ==================================================================== #
    # Insertion Sort O(n^2) #
    # ==================================================================== #
    if i <= 10000:
        startTime = endTime = totalTime = 0
        unsortedList = initList(i)

        # start clock and perform sort
        startTimeInsert = time.time()
        sortedList = insertionSort(unsortedList)
        totalTimeInsert = time.time() - startTimeInsert
        timeInsert.append(totalTimeInsert)

    else: 
        # To fill in chart with an estimated value for n^2 without computing data
        expGrowth = totalTimeInsert*totalTimeInsert
        timeInsert.append(expGrowth)

# ==================================================================== #
# GRAPH SMOOTHER #
xTime = np.linspace(min(testInterval), max(testInterval), 300)

countSpl= make_interp_spline(testInterval, timeCount, k=3)
countSmooth = countSpl(xTime)
mergeSpl = make_interp_spline(testInterval, timeMerge, k=3)
mergeSmooth = mergeSpl(xTime)
insertSpl = make_interp_spline(testInterval, timeInsert, k=3)
insertSmooth = insertSpl(xTime)
# ==================================================================== #

# Graph Limits & Labels
plt.ylim(0,15) 
plt.xlim(0,1000000) 
plt.xlabel('num of elements')
plt.ylabel('time (s)')

# multiple line plot
plt.plot(xTime, countSmooth, color='green', label='countSort')
plt.plot(xTime, mergeSmooth, color='blue', label='mergeSort')
plt.plot(xTime, insertSmooth, color='red', label='insertSort')

# Plot 
plt.legend()
plt.show()
