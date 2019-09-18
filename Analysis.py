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
import time
import random
import matplotlib.pyplot as plt

from Merge_Sort import mergeSort
from Counting_Sort import counting_Sort
from Insertion_Sort import insertion_sort

# funct to init arr of length n with rand values [0..n]
def initList(n):
    newList = []
    for i in range(n):
        rand = random.randint(0, n)
        newList.append(rand)
    return newList

# funct to check if arr is sorted
def isSorted(newList):
    if (len(newList) < 2):
        return True
    for i in range(len(newList)):
        if (i + 1 < len(newList) and newList[i] > newList[i + 1]):
            return False
    return True

def createGraph(n, totalTimeMerge, totaleTimeCount, totalTimeInsert, timeMerge, timeCount,timeInsert):
    # create arr of length n with each n as element
    newList = []
    time = []
    timeInterval = float(n) / totalTimeInsert
    for i in range(0,4):
        time.append(i * timeInterval)
    for i in range(n):
        newList.append(i)

    # plot the num of elems over time
    #plt.plot(newList, time)

    # multiple line plot
    plt.plot(timeMerge, time)
    plt.plot(timeCount, time)
    plt.plot(timeInsert, time)
    #plt.legend()

    plt.xlabel('num of elements')
    plt.ylabel('time (s)')
    plt.show()

startTimeMerge = endTimeMerge = totalTimeMerge = 0
startTimeCount = endTimeCount = totalTimeCount = 0
startTimeInsert = endTimeInsert = totalTimeInsert = 0

# check times
n = 10000
unsortedList1 = initList(n)
unsortedList2 = initList(n)
unsortedList3 = initList(n)

# merge
start = time.time()
sortedList = mergeSort(unsortedList1)
total = time.time() - start
print("merge: " + str(total))

# counting
start = time.time()
sortedList = counting_Sort(unsortedList2)
total = time.time() - start
print("counting: " + str(total))

# insert
start = time.time()
sortedList = insertion_sort(unsortedList3)
total = time.time() - start
print("insert: " + str(total))

"""
timeMerge = []
timeCount = []
timeInsert = []


n = 1000
listSize = 10
for i in range(0,9):

    unsortedList = initList(listSize)

    startTimeMerge = time.time()
    sortedList = mergeSort(unsortedList)
    totalTimeMerge = time.time() - startTimeMerge
    timeMerge.append(totalTimeMerge)

    startTimeCount = time.time()
    sortedList = counting_Sort(unsortedList)
    totalTimeCount = time.time() - startTimeCount
    timeCount.append(totalTimeCount)


    if listSize <= 100000:
        startTimeInsert = time.time()
        sortedList = insertion_sort(unsortedList)
        totalTimeInsert = time.time() - startTimeInsert
        timeInsert.append(totalTimeInsert)

    listSize = 10 * listSize



# start clock and perform sort
#startTime = datetime.now()
#endTime = datetime.now()

# get total time and display
#totalTime = endTime - startTime
#print(isSorted(sortedList))
#print(totalTime)

# plot graph
createGraph(n, totalTimeMerge, totalTimeCount, totalTimeInsert, timeMerge, timeCount, timeInsert)
"""