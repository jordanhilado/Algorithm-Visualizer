def heaping(arr, n, i): 
    largest = i 
    left = 2 * i + 1    
    right = 2 * i + 2     
    #Compare the largest element to the element on left
    if left < n and arr[i] < arr[left]: 
        largest = left 
    #Compare the largest element to the element on right
    if right < n and arr[largest] < arr[right]: 
        largest = right  
    # swap to get the largest element to the top
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
        heaping(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr)  
    for i in range(n//2 - 1, -1, -1): 
        heaping(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heaping(arr, i, 0) 

#Code to intake list to sort and call the functions to sort
array_size = int(input("How many elements do you wish to sort? "))
a = []
print("Please start entering the elements to sort, press enter after each element : ")
for j in range(0, array_size):
  temp = int(input())
  a.append(temp)
print("List to sort is: ", a)

arr=a
heapSort(arr) 
#print the array
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
