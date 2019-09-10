# ==================================================================== #
# File Name: Insertion_Sort.py
# Authors: Jacob Sheets & Jake Allinson
# Date Created: 10 Sept 2019
# Version: 0.0.1

# Copyright: Copyright 2019, Sorting_Algorthims
# Course: CS3410 Cedarville University

# Description: Insertion Sort Algorthim
# ==================================================================== #

def insertion_sort_build():
    sortArray = []


def insertion_sort(sortArray):
    j = 2
    for j in sortArray:
        key = sortArray[j]
        i = j - 1
        while i > 0 and sortArray[i] > key:
             sortArray[i] = sortArray[i+1]
             i = i - 1
        sortArray[i+1] = key

def main():