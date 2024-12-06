# Program for merge sort

# Array definition
arr = [4, 6, 20, 1, 8, 16, 10, 11, 11, 18, 5, 13, 19, 14, 17, 2, 15, 11, 11, 11, 7, 3, 12, 9]
#arr = [5,2,8,3,6,1,4,9,7]
#arr = [1,2]

# Print array
def printarr(arr):
    fin = ""
    for k in range(len(arr)):
        fin = fin + " | " + str(arr[k])

    print(fin)


# Function for merge sort
def mergesort(arr):
    
    length = len(arr)
        
    if(len(arr) == 1):
        return arr
    
    if(len(arr) > 1):
        mid = int(length/2)
        
        left = mergesort(arr[0:mid])
        right =  mergesort(arr[mid:length])

        i, j = 0, 0
        newarr = []
        while(i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                newarr.append(left[i])
                i += 1
            else:
                newarr.append(right[j])
                j += 1
        
        while(i < len(left)):
            newarr.append(left[i])
            i += 1

        while(j < len(right)):
            newarr.append(right[j])
            j += 1
        
        return newarr


printarr(arr)
arr = mergesort(arr)
printarr(arr)
