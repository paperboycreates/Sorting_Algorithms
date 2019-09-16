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
from Counting_Sort import counting_Sort
from Insertion_Sort import insertion_sort
# from Merge_Sort import mergeSort

#TODO: Figure how to get start time
#TODO: Manage Time

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

startTime = endTime = totalTime = 0
n = 100
unsortedList = initList(n)

# start clock and perform sort
startTime = datetime.now()
sortedList = counting_Sort(unsortedList) # fix each sort to take unsorted list
endTime = datetime.now()

totalTime = endTime - startTime
print(isSorted(sortedList))
print(totalTime)



#TODO: Figue out a way to manage data without killing the process
#TODO: Graphic?




#TODO: Number Randomizer
#TODO: make Massive Arrays Case Statement.

