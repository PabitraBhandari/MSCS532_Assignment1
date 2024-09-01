#Name: Pabitra Bhandari
#Assignment 1 
#Algorithms and Data Structures
#Date: 09/01/2024
#To Do: Sorting array into monotonically decreasing order using Insertion Sort algorithm.

#defining the function.
def decreasing_Order_InsertionSort(array):
   
   #creating the range function using for loop.
    for i in range(1, len(array)):
        out = array[i]
        
        j = i - 1

        #executing while loop as long as the condition is true.
        while j >= 0 and array[j] < out:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = out

#condition to execute main method.
if __name__ == "__main__":

    #declaring the array to be sorted.
    array = [99,0,10,35,87,89,54,38,1,6,77,22,45]

    #calling the function.
    decreasing_Order_InsertionSort(array)

    #printing the result:sorted array.
    print("Insertion array in decreasing order is:")
    print(array)

