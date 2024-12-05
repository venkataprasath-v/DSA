# Program for quick sort

# Array definition
arr = [4, 6, 20, 1, 8, 16, 10, 11, 11, 18, 5, 13, 19, 14, 17, 2, 15, 11, 11, 11, 7, 3, 12, 9]

# Print array
def printarr(arr):
    fin = ""
    for k in range(len(arr)):
        fin = fin + " | " + str(arr[k])

    print(fin)


# Function for Quick sort 
def quicksort(arr, left, right):

    origleft, origright = left, right

    pivot = arr[right]
    
    if(left == right):
        return
    
    while(left < right):
        if(arr[left] < pivot):
            left += 1
        if(arr[right] > pivot and left < right):
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
        if(arr[left] == arr[right]):
            break
    
    if(left - origleft > 1):
        quicksort(arr, origleft, left-1)

    if(origright - right > 1):
        quicksort(arr, right+1, origright)
    

printarr(arr)
quicksort(arr, 0, len(arr)-1)
printarr(arr)