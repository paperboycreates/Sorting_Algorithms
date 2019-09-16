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

listSize = 1000
randomIntList = [0] * (listSize)

for x in range(listSize):
  randomIntList[x] = random.randint(1,listSize)


startTime = 0 
endTime = 0
totalTime = 0

startTime = datetime.now()
sortedList = counting_Sort(randomIntList)
endTime - datetime.now()

totalTime = endTime - startTime
print (sortedList)
print(totalTime)



#TODO: Figue out a way to manage data without killing the process
#TODO: Graphic?




#TODO: Number Randomizer
#TODO: make Massive Arrays Case Statement.

