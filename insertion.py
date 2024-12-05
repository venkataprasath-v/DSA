# Insertion sort

# Array definition
arr = [4,7,2,9,1,3,8,6,5]


# Function for printing the array
def printarr():
    fin = ""
    for k in range(len(arr)):
        fin = fin + " | " + str(arr[k])

    print(fin)


# Insertion sort
for i in range(1,len(arr)):
    printarr()
    j = i
    temp = arr[i]
    while(j != 0 and temp < arr[j-1]):
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = temp
printarr()
         




