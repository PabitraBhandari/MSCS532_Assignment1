#Name: Pabitra Bhandari
#Assignment 1 
#Algorithms and Data Structures
#Date: 09/01/2024
#To Do: Sorting array into monotonically decreasing order instead of increasing using Insertion Sort algorithm.

def decreasingOrderInsertionSort(array):
   
    for i in range(1, len(array)):
        out = array[i]
        
        j = i - 1
        while j >= 0 and array[j] < out:
            array[j + 1] = array[j]
            j = j- 1
        array[j + 1] = out

