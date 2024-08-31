#Name: Pabitra Bhandari
#Assignment 1 
#Algorithms and Data Structures
#Date: 09/01/2024
#To Do: Sorting array into monotonically decreasing order using Insertion Sort algorithm.

def decreasing_Order_InsertionSort(array):
   
    for i in range(1, len(array)):
        out = array[i]
        
        j = i - 1
        while j >= 0 and array[j] < out:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = out

if __name__ == "_mainfunc_":
    array = [99,0,10,35,87,89,54,38,1,6,77,22,45]
    decreasing_Order_InsertionSort(array)
    print("Insertion array in decreasing order is:")
    print(array)

