# ==================================================================== #
# File Name: Counting_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Counting Sort Algorthim
# ==================================================================== #

def counting_Sort(unsortedList):
    
    #intiazlie count
    maxValue = max(unsortedList)+ 1
    count = [0] * (maxValue)

    # find freq of numbers in unsorted
    for i in unsortedList:
        count[i] += 1

    # removes 0 indexing
    count [0] = count[0] - 1

    # arrange count for unsortedList index
    for i in range(1, maxValue):
        count[i] = count[i] + count[i-1]        

    sortedList = [None] * len(unsortedList)
   
    # build sorted list
    for j in reversed(unsortedList):
        sortedList[count[j]] = j
        count[j] = count[j] - 1

    return sortedList

# Quick Test
def main():    

    testArray = [18, 14, 4, 7, 12, 2, 3, 6, 100, 40, 5, 1]
    sorted = counting_Sort(testArray)   
    print(sorted)

# Runs Main Test
main()